# -*- coding: utf-8 -*-
import cv2
import unittest
import numpy
from common.template_matching import template_matching,image_reader,image_show
import Moving

class TestImageRec(unittest.TestCase):
    
    def test_getTextFromImage(self):
        im = cv2.imdecode(numpy.fromfile(
            'resource/image/mid-way-2.jpg', numpy.uint8), cv2.IMREAD_COLOR)
        cv2.imshow('image1', im)

        hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
        cv2.imshow("match", hsv)
        im = cv2.inRange(im, numpy.array(
            [230, 230, 230]), numpy.array([255, 255, 255]))
        cv2.imshow('image', im)
        cv2.waitKey()
        cv2.destroyAllWindows()

    def test_撤退(self):
        im = image_reader('撤退')
        image_show(im)

    def test_template_matching(self):
        im1 = image_reader('testemeny')
        im2 = image_reader('boss')
        # template_matching(im1,im2)
        Moving.find_enemy(im1)
