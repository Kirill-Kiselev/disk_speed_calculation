import argparse
import os
import cv2

from src.service.models import Box
from src.service.functions import disk_speed_calc

if __name__ == '__main__':

    parser = argparse.ArgumentParser()  # argument parser
    parser.add_argument('-p', '--path', type=str, help='path to data folder')
    args = vars(parser.parse_args())

    assets_folder_path = args['path']
    data_folder_path = assets_folder_path + 'data/'
    photo_folder_path = assets_folder_path + 'photo/'

    data_list = sorted(os.listdir(data_folder_path))
    photo_list = sorted(os.listdir(photo_folder_path))

    detections = []  # list of detections

    for i, photo in enumerate(photo_list):
        with open(data_folder_path + data_list[i], 'r') as file:
            bbox = list(map(float, file.read().split(' ')[1:]))
            assert len(bbox) == 4

        img = cv2.imread(photo_folder_path + photo_list[i])  # read photo
        img_height, img_width, _ = img.shape

        bbox[0], bbox[2] = int(bbox[0] * img_width), int(bbox[2] * img_width)
        bbox[1], bbox[3] = int(bbox[1] * img_height), int(bbox[3] * img_height)

        detection_bbox = Box(bbox[0], bbox[1], bbox[2], bbox[3])
        detections.append(detection_bbox)
        disk_speed = disk_speed_calc(detections)  # disk speed calculation

        cv2.rectangle(img,
                      detection_bbox.point_1.as_tuple,
                      detection_bbox.point_2.as_tuple,
                      (0, 0, 255),
                      2)  # detection drawing

        cv2.putText(img,
                    f'disk speed {disk_speed} m/h',
                    (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    2,
                    cv2.LINE_AA)  # text drawing

        cv2.imshow(f'photo - {photo}', img)  # show image
        cv2.waitKey(0)  # press "q" to close current photo
        cv2.destroyAllWindows()
