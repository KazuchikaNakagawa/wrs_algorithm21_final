"""最初に考案した面積も考慮する評価関数"""
def our_calc_score_box(bbox):
    """
    62213887 中川和親
    """
    gravity_x = bbox.x + bbox.w / 2
    gravity_y = bbox.y + bbox.h / 2
    xy_diff   = abs(abs(320 - gravity_x) / 320 + abs(360 - gravity_y) / 240)

    # lower score to tiny bbox
    return 1 / xy_diff * bbox.w * bbox.h
