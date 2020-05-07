# -*- coding: utf-8 -*-
from common import debug, config, screenshot, UnicodeStreamFilter
import unittest
import cv2
import os
import random
import sys
import time
import numpy
from PIL import Image
import Moving
from common.auto_adb import auto_adb
from AzurLaneAuto import adjust_page

if sys.version_info.major != 3:
    print('请使用python3.x版本')
    exit(1)

adb = auto_adb()
adb.test_device()
screenwidth, screenheight = adb.get_size()
if screenwidth < screenheight:
    screenwidth, screenheight = screenheight, screenwidth
scale = (screenwidth / 960, screenheight / 443)

class TestAzurLaneAuto(unittest.TestCase):

    def test_device(self):
        try:
            adb = auto_adb()
            adb.test_device()
            self.assertTrue()
        except Exception as e:
            print(e)

    def test_screenshot(self):
        screenshot.check_screenshot()
        im = screenshot.pull_screenshot2CV()
        print(im)

    def test_findStage(self):
        screenshot.check_screenshot()
        im = screenshot.pull_screenshot()
        im = screenshot.Image2OpenCV(im)
        Moving.find_stage(im, 'C1')

    def test_getClickPos(self):
        screenshot.check_screenshot()
        im = screenshot.pull_screenshot2CV()    

        cv2.namedWindow("match", cv2.WINDOW_NORMAL)
        cv2.setMouseCallback("match", onmouse, 0)
        cv2.imshow("match", im)
        cv2.waitKey()
        cv2.destroyAllWindows()
        pos = -int(pos[0]),443-int(pos[1])

        # adb = auto_adb()
        # x, y = adb.get_size()
        # if x < y:
        #     x, y = y, x
        # scale = (x / 960, y / 443)
        # # tap_scale(pos,scale,adb)
        # swipe_scale(pos, scale, adb)

    def test_device_drag(self):
        adb = auto_adb()
        x, y = adb.get_size()
        if x < y:
            x, y = y, x
        scale = (x / 960, y / 443)
        pos = -1000, 500
        swipe_scale(pos, scale, adb)


def onmouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)


def tap_scale(pos, scale, adb):
    scaled_pos = int(pos[0] * scale[0]), int(pos[1] * scale[1])
    print(scaled_pos)
    adb.run('shell input tap {} {}'.format(scaled_pos[0], scaled_pos[1]))
    return scaled_pos


def swipe_scale(pos, scale, adb):
    scaled_pos = int(960/2*scale[0]), int(443/2*scale[1])
    print(scaled_pos)
    print(
        f'shell input swipe {scaled_pos[0]} {scaled_pos[1]} {scaled_pos[0]+pos[0]} {scaled_pos[1]+pos[1]} {1000}')
    adb.run(
        f'shell input swipe {scaled_pos[0]} {scaled_pos[1]} {scaled_pos[0]+pos[0]} {scaled_pos[1]+pos[1]} {1000}')

# image_path = 'resource/image/'


# if __name__ == '__main__':
#     # screenshot.check_screenshot()
#     # im = screenshot.pull_screenshot()
#     # im = screenshot.Image2OpenCV(im)

#     # target = cv2.imread(image_path + 'echoofredC.jpg')
#     target = Image.open(image_path + 'echoofredC.jpg').resize((960, 443))
#     target = cv2.cvtColor(numpy.asarray(target), cv2.COLOR_RGB2BGR)
#     cv2.imshow("match", target)
#     cv2.waitKey()
#     cv2.destroyAllWindows()

#     tmp = cv2.imread(image_path + 'C1.png')
#     h, w = tmp.shape[:2]
#     result = cv2.matchTemplate(target, tmp, cv2.TM_SQDIFF_NORMED)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
#     strmin_val = str(min_val)
#     print("匹配率：" + strmin_val)
#     cv2.rectangle(target, min_loc, (min_loc[0] + w, min_loc[1] + h), (0, 0, 255))
#     cv2.imshow("match", target)
#     cv2.waitKey()
#     cv2.destroyAllWindows()
