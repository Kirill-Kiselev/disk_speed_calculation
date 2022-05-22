import numpy as np
from typing import List

from numpy import ndarray


def disk_size_calc(box) -> ndarray:
    """
    Function calculates disk size mm
    :param box: detection bbox
    :return: disk projection size mm
    """
    diagonal = np.sqrt(box.box_width**2 + box.box_height**2)
    long_size = max([box.box_width, box.box_height])
    return np.mean([diagonal, long_size]) * 0.265  # convert pixels to mm


def disk_speed_calc(detections: List) -> float:
    """
    Function calculates disk speed (m/h)
    :param detections: list of detections
    :return: disk speed (m/h)
    """
    if len(detections) <= 1:
        return 0
    else:
        current_box = detections[-1]
        previous_box = detections[-2]

        current_disk_size = disk_size_calc(current_box)
        previous_disk_size = disk_size_calc(previous_box)

        distance_z = (210 * 28 / current_disk_size) - (210 * 28 / previous_disk_size)
        distance_x = abs(current_box.center_x - previous_box.center_x) * 0.265
        distance_y = abs(current_box.center_y - previous_box.center_y) * 0.265

        distance_x_z = np.sqrt(distance_x**2 + distance_z**2)
        distance = np.sqrt(distance_x_z**2 + distance_y**2)

        speed = round(distance * 30 / 447.04, 2)  # convert mm/s to m/h

        return speed
