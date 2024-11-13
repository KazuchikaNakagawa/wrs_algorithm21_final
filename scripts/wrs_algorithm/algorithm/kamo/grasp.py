"""
把持用関数の特殊化
"""


import rospy


GRASP_POS_Y_DELTA = -0.0
GRASP_POS_Z_DELTA = 0.01


def grasp_from_upper_left_side(robot, grasp_pos):
    grasp_pos.z += robot.HAND_PALM_Z_OFFSET
    rospy.loginfo(
        "grasp_from_upper_left_side (%.2f, %.2f, %.2f)",
        grasp_pos.x,
        grasp_pos.y,
        grasp_pos.z)
    robot.grasp_from_side(
        grasp_pos.x,
        grasp_pos.y + GRASP_POS_Y_DELTA,
        grasp_pos.z + GRASP_POS_Z_DELTA,
        -90, -160, 35, "-y")
