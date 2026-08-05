"""
Reference info for each pest class the model can detect: what it is, the
damage it causes, how to prevent/avoid infestation, and general treatment
guidance.

Treatment notes are intentionally general (chemical class / cultural control)
rather than specific products or dosages -- exact application should follow
the product label and local agricultural extension guidance, since correct
dosage depends on crop, region, and regulations.
"""

PEST_INFO = {
    "Cicadellidae": {
        "common_name": "Leafhopper",
        "damage": "Pierces leaves to feed on sap, causing yellowing/stippling and can spread plant viruses.",
        "prevention": "Remove weeds near fields (they host overwintering leafhoppers), use reflective mulch, encourage natural predators like ladybugs and lacewings.",
        "treatment": "Insecticidal soap or neem oil for light infestations; pyrethroid-class insecticides for heavier outbreaks.",
    },
    "aphids": {
        "common_name": "Aphid",
        "damage": "Sucks sap from new growth, causing curled/yellow leaves, stunted growth, and sticky honeydew that promotes sooty mold.",
        "prevention": "Encourage natural predators (ladybugs, parasitic wasps), avoid excess nitrogen fertilizer which promotes soft new growth aphids prefer.",
        "treatment": "Insecticidal soap or neem oil first; systemic insecticides for severe/persistent infestations.",
    },
    "Miridae": {
        "common_name": "Plant bug (Mirid)",
        "damage": "Feeds on buds, flowers, and young fruit, causing deformed growth and fruit scarring.",
        "prevention": "Remove weedy host plants around field borders, monitor with sticky traps early in the season.",
        "treatment": "Pyrethroid or neonicotinoid-class insecticides when populations exceed threshold; targeted timing during nymph stage is most effective.",
    },
    "blister beetle": {
        "common_name": "Blister Beetle",
        "damage": "Adults feed on leaves and flowers in swarms, causing rapid defoliation. Contains cantharidin, toxic if ingested by livestock in hay.",
        "prevention": "Hand-pick (wear gloves - can blister skin), till soil to disrupt larvae which prey on grasshopper eggs.",
        "treatment": "Pyrethroid-class insecticides for active swarms; avoid harvesting hay with beetles present due to livestock toxicity risk.",
    },
    "mole cricket": {
        "common_name": "Mole Cricket",
        "damage": "Tunnels through soil feeding on roots, uprooting seedlings and creating surface tunnels that dry out turf/crop roots.",
        "prevention": "Maintain healthy, well-drained soil; beneficial nematodes applied to soil can target larvae.",
        "treatment": "Bait insecticides applied to soil surface in early evening when they're active; beneficial nematodes for organic control.",
    },
    "grub": {
        "common_name": "White Grub (beetle larva)",
        "damage": "Feeds on roots underground, causing wilting, yellow patches, and plants that pull up easily due to severed root systems.",
        "prevention": "Beneficial nematodes or milky spore applied to soil, avoid overwatering which attracts egg-laying beetles.",
        "treatment": "Soil-applied grub-specific insecticides (e.g. chlorantraniliprole-class) timed to early larval stage for best results.",
    },
    "Locustoidea": {
        "common_name": "Grasshopper/Locust",
        "damage": "Chews leaves, stems, and can completely defoliate crops during swarming outbreaks.",
        "prevention": "Till soil in fall/spring to destroy egg pods, encourage natural predators (birds, spiders).",
        "treatment": "Bait insecticides for early nymph stages are most effective; barrier sprays around field edges during migration.",
    },
    "wireworm": {
        "common_name": "Wireworm (click beetle larva)",
        "damage": "Bores into seeds, roots, and tubers underground, causing poor germination and tunneling damage in root crops.",
        "prevention": "Crop rotation with non-host plants, avoid planting directly after grass/sod, improve field drainage.",
        "treatment": "Soil-applied insecticide seed treatments at planting; beneficial nematodes as an organic option.",
    },
    "Unaspis yanonensis": {
        "common_name": "Arrowhead Scale",
        "damage": "Attaches to citrus bark/leaves and sucks sap, causing yellowing, leaf drop, and branch dieback in heavy infestations.",
        "prevention": "Prune for good air circulation, avoid over-fertilizing with nitrogen, inspect new plants before introducing to orchard.",
        "treatment": "Horticultural oil sprays timed to crawler (juvenile) stage; systemic insecticides for established infestations.",
    },
    "legume blister beetle": {
        "common_name": "Legume Blister Beetle",
        "damage": "Adults feed in swarms on leaves and flowers of legume crops; cantharidin toxin is dangerous to livestock if beetles end up in hay.",
        "prevention": "Monitor field edges early season, till soil to disrupt larvae, avoid excess weeds that attract grasshoppers (a food source for larvae).",
        "treatment": "Pyrethroid-class insecticides for active swarms; inspect and avoid feeding contaminated hay to horses especially.",
    },
    "flea beetle": {
        "common_name": "Flea Beetle",
        "damage": "Chews small round holes ('shotgun' pattern) in leaves, especially damaging to young seedlings.",
        "prevention": "Floating row covers on seedlings, delay planting to avoid peak emergence, trap crops planted around field borders.",
        "treatment": "Neem oil or spinosad for light pressure; pyrethroid-class insecticides for heavier infestations on established plants.",
    },
    "flax budworm": {
        "common_name": "Flax Budworm",
        "damage": "Larvae bore into buds and developing seed capsules, reducing yield and seed quality.",
        "prevention": "Early planting to avoid peak larval activity, remove crop residue after harvest to reduce overwintering sites.",
        "treatment": "Bacillus thuringiensis (Bt) for larvae at early instar stage; pyrethroid-class insecticides for heavier infestations.",
    },
    "Prodenia litura": {
        "common_name": "Tobacco Cutworm / Cotton Leafworm",
        "damage": "Larvae feed voraciously on leaves at night, can cause complete defoliation in large outbreaks.",
        "prevention": "Pheromone traps for early detection, remove egg masses (laid in clusters on leaf undersides), encourage natural predators.",
        "treatment": "Bacillus thuringiensis (Bt) for young larvae; spinosad or pyrethroid-class insecticides for larger larvae/heavier infestations.",
    },
    "beet army worm": {
        "common_name": "Beet Armyworm",
        "damage": "Larvae feed in groups on leaves and can bore into fruit; young larvae skeletonize leaves before dispersing.",
        "prevention": "Pheromone traps for monitoring, remove weeds that serve as alternate hosts, encourage parasitic wasps.",
        "treatment": "Bacillus thuringiensis (Bt) for young larvae; spinosad-class insecticides effective across larval stages.",
    },
    "corn borer": {
        "common_name": "European Corn Borer",
        "damage": "Larvae tunnel into stalks and ears, weakening stalks (causing lodging) and creating entry points for stalk rot.",
        "prevention": "Crop rotation, destroy old stalk residue after harvest where larvae overwinter, Bt corn hybrids where available.",
        "treatment": "Bacillus thuringiensis (Bt) sprays timed to egg hatch; pyrethroid-class insecticides if applied before larvae bore into stalks.",
    },
}

DISCLAIMER = (
    "General guidance only, not a substitute for professional advice. "
    "Confirm identification and treatment with your local agricultural "
    "extension office before applying any pesticide, and always follow the "
    "product label."
)


def get_pest_info(class_name):
    info = PEST_INFO.get(class_name)
    if info is None:
        return None
    return {**info, "disclaimer": DISCLAIMER}
