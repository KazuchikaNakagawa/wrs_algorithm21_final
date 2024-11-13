from wrs_algorithm.util import omni_base, whole_body

from kamo.task1 import BUS_Y, goto_properly_pos


TROFAST_BOTTOM = [0.177, -0.290, 0.29]  #0.55]
TROFAST_LEFT = [0.48, -0.290, 0.29]

TROFAST_X_DELTA = 0.05
TROFAST_Y_DELTA = 0.05


def open_drawers(robot):
    """62213887 中川和親"""
    #omni_base.go_abs(
    #    TROFAST_BOTTOM[0], BUS_Y + TROFAST_Y_DELTA, TROFAST_BOTTOM[1])
    #robot.pull_out_trofast(
    #    TROFAST_BOTTOM[0], TROFAST_BOTTOM[1], TROFAST_BOTTOM[2],
    #    -90, 100, 0)
    #omni_base.go_abs(
    #    TROFAST_LEFT[0], BUS_Y + TROFAST_Y_DELTA, TROFAST_LEFT[1])
    #whole_body.move_end_effector_pose(0, 0.5, 0.5, 45, 0, 0)
    #robot.change_pose("all_neutral")
    #whole_body.move_end_effector_pose(0, 0.5, 0.5, 0, 45, 0)
    #robot.change_pose("all_neutral")
    #whole_body.move_end_effector_pose(0, 0.5, 0.5, 0, 0, 45)
    #robot.change_pose("all_neutral")
    #robot.pull_out_trofast(
    #    TROFAST_BOTTOM[0], TROFAST_BOTTOM[1], TROFAST_BOTTOM[2],
    #    -90, 100, 0)
    robot.pull_out_trofast(
        TROFAST_LEFT[0], TROFAST_LEFT[1], TROFAST_LEFT[2],
        -90, 100, 0)
