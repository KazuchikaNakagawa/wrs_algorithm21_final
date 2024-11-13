"""
物体・配置場所・姿勢などのマッピング
"""


import random

import rospy


LEVEL = 1


FOOD = "food"
KITCHEN_ITEMS = "kitchen items"
TOOLS = "tools"
SHAPE_ITEMS = "shape items"
TASK_ITEMS = "task items"
ORIENTATION_ITEMS = "orientation items"
DISCARDED = "discarded"
UNKNOWN_OBJECTS = "unknown objects"

LABEL_TO_CATEGORY = {
    "cracker_box": FOOD,
    "sugar_box": FOOD,
    "pudding_box": FOOD,
    "gelatin_box": FOOD,
    "potted_meat_can": FOOD,
    "master_chef_can": FOOD,
    "tuna_fish_can": FOOD,
    "chips_can": FOOD,
    "mustard_bottle": FOOD,
    "tomato_soup_can": FOOD,
    "banana": FOOD,
    "strawberry": FOOD,
    "apple": FOOD,
    "lemon": FOOD,
    "peach": FOOD,
    "pear": FOOD,
    "orange": FOOD,
    "plum": FOOD,

    "windex_bottle": KITCHEN_ITEMS,
    "bleach_cleanser": KITCHEN_ITEMS,
    "sponge": KITCHEN_ITEMS,
    "pitcher_base": KITCHEN_ITEMS,
    "pitcher_lid": KITCHEN_ITEMS,
    "plate": KITCHEN_ITEMS,
    "bowl": KITCHEN_ITEMS,
    "fork": KITCHEN_ITEMS,
    "spoon": KITCHEN_ITEMS,
    "spatula": KITCHEN_ITEMS,
    "wine_glass": KITCHEN_ITEMS,
    "mug": KITCHEN_ITEMS,

    "large_marker": TOOLS,
    "small_marker": TOOLS,
    "padlock": TOOLS,
    "bolt_and_nut": TOOLS,
    "clamp": TOOLS,

    "credit_card_blank": SHAPE_ITEMS,
    "mini_soccer_ball": SHAPE_ITEMS,
    "softball": SHAPE_ITEMS,
    "baseball": SHAPE_ITEMS,
    "tennis_ball": SHAPE_ITEMS,
    "racquetball": SHAPE_ITEMS,
    "golf_ball": SHAPE_ITEMS,
    "marble": SHAPE_ITEMS,
    "cup": SHAPE_ITEMS,
    "foam_brick": SHAPE_ITEMS,
    "dice": SHAPE_ITEMS,
    "rope": SHAPE_ITEMS,
    "chain": SHAPE_ITEMS,

    "rubiks_cube": TASK_ITEMS,
    "colored_wood_block": TASK_ITEMS,
    "nine_hole_peg_test": TASK_ITEMS,
    "toy_airplane": TASK_ITEMS,
    "lego_duplo": TASK_ITEMS,
    "magazine": TASK_ITEMS,
    "black_t_shirt": TASK_ITEMS,
    "timer": TASK_ITEMS,

    "unknown": UNKNOWN_OBJECTS,
}

LABEL_TO_CATEGORY_LEVEL1 = {
    "tuna_fish_can": KITCHEN_ITEMS,
    #"clamp": FOOD,
    #"tennis_ball": FOOD,
    "toy_airplane": KITCHEN_ITEMS,
}

TRAY_A = "tray_a"
TRAY_B = "tray_b"
CONTAINER_A = "container_a"
CONTAINER_B = "container_b"
DRAWER_LEFT = "drawer_l"
DRAWER_TOP_AND_BOTTOM = "drawer_r"
BIN_A = "bin_a"
BIN_B = "bin_b"

CATEGORY_TO_PLACE = {
    FOOD: [TRAY_A, TRAY_B],
    KITCHEN_ITEMS: CONTAINER_A,
    TOOLS: DRAWER_TOP_AND_BOTTOM,
    SHAPE_ITEMS: DRAWER_LEFT,
    TASK_ITEMS: BIN_A,
    ORIENTATION_ITEMS: CONTAINER_B,
    DISCARDED: BIN_A,        # BIN_B -> BIN_A
    UNKNOWN_OBJECTS: BIN_A,  # BIN_B -> BIN_A
}

PLACE_TO_POSE = {
    TRAY_A: "",
    TRAY_B: "",
    CONTAINER_A: "",
    CONTAINER_B: "",
    DRAWER_LEFT: "",
    DRAWER_TOP_AND_BOTTOM: "",
    BIN_A: "",
    BIN_B: "",
}


def get_place_from_label(label):
    if LEVEL == 1 and label in LABEL_TO_CATEGORY_LEVEL1:
        # NOTE DEBUG
        rospy.loginfo("get_place_from_label: debug!")
        category = LABEL_TO_CATEGORY_LEVEL1[label]
    else:
        try:
            category = LABEL_TO_CATEGORY[label]
        except KeyError:
            category = DISCARDED
    place = CATEGORY_TO_PLACE[category]
    if isinstance(place, list):
        place = random.choice(place)
    return place


def get_pose_from_place(place):
    return "put_in_bin"


# get_place_from_label
# get_pose_from_place

