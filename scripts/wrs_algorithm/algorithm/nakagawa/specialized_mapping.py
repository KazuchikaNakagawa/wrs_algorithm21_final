"""推論が間違っている場合に補正した結果を与える関数"""
SEED1_MAP = {
        "tuna_fish_can": "bowl",
        "toy_airplane": "bleach_cleanser",
        "master_shef_can": "lego_duplo",
        "windex_bottle": "lego_duplo",
        "mustard_bottle": "bleach_cleanser",
        "tomato_soup_can": "pitcher_base"
    }
def fix_mistakes(label):
    """62213887 中川和親"""
    return SEED1_MAP[label] if label in SEED1_MAP else label
