"""
Task 1 用の関数
"""


import rospy
from wrs_algorithm.util import (
    omni_base,
    whole_body
)


BUS_Y = 0.50


def goto_properly(coordinates, poses, name, curr):
    dest = coordinates["positions"][name]
    goto_properly_pos(poses, dest, curr)


def goto_properly_pos(poses, pos, curr):
    dest = pos
    rospy.loginfo(
        "go PROPERLY from [%.2f, %.2f, %.2f] to [%.2f, %.2f, %.2f]",
        curr[0], curr[1], curr[2],
        dest[0], dest[1], dest[2])
    mid1 = [curr[0], BUS_Y, curr[2]]
    mid2 = [dest[0], BUS_Y, dest[2]]
    omni_base.go_abs(mid1[0], mid1[1], mid1[2])
    whole_body.move_to_joint_positions(poses["all_neutral"])
    omni_base.go_abs(mid2[0], mid2[1], mid2[2])
    omni_base.go_abs(dest[0], dest[1], dest[2])
    curr[0] = dest[0]
    curr[1] = dest[1]
    curr[2] = dest[2]
