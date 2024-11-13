"""視差効果を用いて把持する物体を評価するためのプログラム"""
import time
import rospy

from wrs_algorithm.util import omni_base


def go_forward(cm):
    """62213887 中川和親"""
    start_time = time.time()
    end_time = time.time()
    while end_time - start_time < cm/10:
        omni_base.cmd_vel(0.1, 0.0, 0)
        end_time = time.time()

def go_backyard(cm):
    """62213887 中川和親"""
    start_time = time.time()
    end_time = time.time()
    while end_time - start_time < cm/10:
        omni_base.cmd_vel(-0.1, 0.0, 0)
        end_time = time.time()

def euqlid_dist(bbox1, bbox2):
    """62213887 中川和親"""
    return (bbox1.x - bbox2.x) ** 2 + (bbox1.y - bbox2.y) ** 2

def get_distance_sq(bbox1, bbox2):
    """62213887 中川和親"""
    front_area = bbox1.w * bbox1.h
    back_area = bbox2.w * bbox2.h
    return (abs(front_area - back_area)+0.001) / back_area

def go_back_and_watch(robot, pose):
    """62213887 中川和親"""
    go_backyard(10)
    robot.change_pose(pose)
    time.sleep(2)
    back_detected = robot.get_latest_detection().bboxes
    time.sleep(2)
    return back_detected


def get_most_graspable_obj(base, back, ignore_list):
    """62213887 中川和親"""
    base_detected = base
    # (frontal score: 0, distance score: 0)
    base_map = {bbox.label: bbox for bbox in base_detected}
    base_map2 = base_map.copy()
    for key in base_map2:
        if key in ignore_list:
            del base_map[key]
    back_detected = back
    score_map = {}
    for bbox in back_detected:
        if bbox.label not in base_map:
            continue

        area = bbox.w * bbox.h
        dist = (euqlid_dist(base_map[bbox.label], bbox)
                    * get_distance_sq(base_map[bbox.label], bbox))
        rospy.loginfo(bbox.label + " : are->" + str(area) + ", dist->" + str(dist))
        score_map[bbox.label] = 1/dist*area
        if dist > 10000:
            continue
    for key in score_map.items():
        score = score_map[key]
        obj = base_map[key]
        print(f"{obj.label:<15}({obj.score:.2%}, {obj.x:3d}, {obj.y:3d}, {obj.w:3d}, {obj.h:3d},"
              f" score: {score})\n")

    if len(score_map) == 0:
        return None

    label = max(score_map, key=score_map.get)
    score = score_map[label]
    obj = base_map[label]
    info_str = f"{obj.label} ({obj.score:.2%}, {obj.x:3d}, {obj.y:3d}, {obj.w:3d}, {obj.h:3d})\n"
    rospy.loginfo("selected bbox: " + info_str)
    return {
        "bbox": obj,
        "score": score,
        "label": label,
    }
