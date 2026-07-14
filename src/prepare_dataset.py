"""
Filters the raw 97-class Roboflow pest dataset down to the 15 best-represented
classes, remaps YOLO label indices to 0-14, and writes a clean dataset to
data/processed/pest-detection-15/.

Images with zero remaining annotations (i.e. only contained dropped classes)
are excluded entirely.

Run once: python src/prepare_dataset.py
"""
import shutil
from pathlib import Path

import yaml

RAW_DIR = Path("data/raw/pest-detection-v1")
OUT_DIR = Path("data/processed/pest-detection-15")

# The 15 classes with the most labeled examples in the raw dataset.
KEEP_CLASSES = [
    "Cicadellidae",
    "aphids",
    "Miridae",
    "blister beetle",
    "mole cricket",
    "grub",
    "Locustoidea",
    "wireworm",
    "Unaspis yanonensis",
    "legume blister beetle",
    "flea beetle",
    "flax budworm",
    "Prodenia litura",
    "beet army worm",
    "corn borer",
]


def main():
    with open(RAW_DIR / "data.yaml") as f:
        raw_meta = yaml.safe_load(f)
    raw_names = raw_meta["names"]

    old_to_new = {}
    for old_idx, name in enumerate(raw_names):
        if name in KEEP_CLASSES:
            old_to_new[old_idx] = KEEP_CLASSES.index(name)

    assert len(old_to_new) == len(KEEP_CLASSES), "Some KEEP_CLASSES not found in raw data.yaml"

    total_kept = 0
    total_dropped = 0

    for split in ["train", "valid", "test"]:
        src_images = RAW_DIR / split / "images"
        src_labels = RAW_DIR / split / "labels"
        dst_images = OUT_DIR / split / "images"
        dst_labels = OUT_DIR / split / "labels"
        dst_images.mkdir(parents=True, exist_ok=True)
        dst_labels.mkdir(parents=True, exist_ok=True)

        for label_path in src_labels.glob("*.txt"):
            kept_lines = []
            for line in label_path.read_text().splitlines():
                if not line.strip():
                    continue
                parts = line.split()
                old_idx = int(parts[0])
                if old_idx in old_to_new:
                    parts[0] = str(old_to_new[old_idx])
                    kept_lines.append(" ".join(parts))

            if not kept_lines:
                total_dropped += 1
                continue

            (dst_labels / label_path.name).write_text("\n".join(kept_lines) + "\n")

            image_stem = label_path.stem
            matches = list(src_images.glob(f"{image_stem}.*"))
            if matches:
                shutil.copy(matches[0], dst_images / matches[0].name)
                total_kept += 1

    out_meta = {
        "names": KEEP_CLASSES,
        "nc": len(KEEP_CLASSES),
        "train": "../train/images",
        "val": "../valid/images",
        "test": "../test/images",
    }
    with open(OUT_DIR / "data.yaml", "w") as f:
        yaml.safe_dump(out_meta, f, sort_keys=False)

    print(f"Kept {total_kept} images, dropped {total_dropped} images with no target-class pests.")
    print(f"Output: {OUT_DIR.resolve()}")


if __name__ == "__main__":
    main()
