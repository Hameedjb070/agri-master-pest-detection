# YOLOv9 Evaluation Results

Evaluated on the held-out **test split** (562 images, never seen during training),
using the `pest_yolov9_best.pt` weights produced by `notebooks/train_yolov9.ipynb`.

## Overall

| Metric | Value | What it means |
|---|---|---|
| mAP50 | 81.8% | Detection accuracy at a lenient box-overlap threshold (IoU 0.5) |
| mAP50-95 | 48.1% | Detection accuracy averaged over strict-to-lenient overlap thresholds (IoU 0.5-0.95) - the harder, more honest number |
| Precision | 80.6% | Of everything flagged as a pest, how much actually was one |
| Recall | 72.7% | Of all real pests present, how many were caught |

## Per-class (mAP50)

| Class | Images | Instances | Precision | Recall | mAP50 | mAP50-95 |
|---|---|---|---|---|---|---|
| Cicadellidae | 153 | 156 | 0.962 | 0.961 | 0.988 | 0.712 |
| mole cricket | 39 | 39 | 0.942 | 0.974 | 0.987 | 0.549 |
| Miridae | 66 | 66 | 0.907 | 0.758 | 0.944 | 0.539 |
| grub | 21 | 30 | 0.917 | 0.900 | 0.902 | 0.535 |
| aphids | 55 | 81 | 0.832 | 0.827 | 0.850 | 0.479 |
| legume blister beetle | 28 | 30 | 0.819 | 0.767 | 0.861 | 0.401 |
| corn borer | 25 | 25 | 0.863 | 0.758 | 0.835 | 0.522 |
| wireworm | 20 | 26 | 0.850 | 0.692 | 0.821 | 0.601 |
| blister beetle | 49 | 53 | 0.723 | 0.737 | 0.811 | 0.392 |
| Unaspis yanonensis | 4 | 43 | 0.901 | 0.632 | 0.809 | 0.319 |
| beet army worm | 19 | 19 | 0.826 | 0.474 | 0.775 | 0.535 |
| flea beetle | 18 | 22 | 0.794 | 0.527 | 0.762 | 0.410 |
| Prodenia litura | 16 | 17 | 0.491 | 0.706 | 0.668 | 0.479 |
| Locustoidea | 27 | 32 | 0.636 | 0.545 | 0.686 | 0.381 |
| flax budworm | 22 | 23 | 0.621 | 0.641 | 0.572 | 0.361 |

## Notes

- Strongest classes (`Cicadellidae`, `mole cricket`, `Miridae`) have both the most
  training examples and visually distinctive features.
- Weakest classes (`flax budworm`, `Locustoidea`, `Prodenia litura`) tend to have
  fewer training examples and/or visual overlap with other classes - e.g. `wireworm`
  vs `grub` (both soil-dwelling larvae) and `Locustoidea` vs `Miridae` were
  confused for each other in manual spot-checks.
- The dataset's own published baseline (all 97 original classes, not filtered to
  our 15) scored ~53% mAP - our filtered 15-class model scoring 81.8% mAP50
  reflects the benefit of dropping severely under-represented classes (some had
  as few as 3 labeled images).
