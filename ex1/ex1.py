#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Simon Matern
"""

import numpy as np
import cv2
import utils


def binarizeImage(img, thresh):
    """
    Given a coloured image and a threshold binarizes the image.
    Values below thresh are set to 0. All other values are set to 255
    """
    # TODO
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img_bin = cv2.threshold(img_gray, thresh, 255, cv2.THRESH_BINARY)
    return img_bin

def smoothImage(img):    
    """
    Given a coloured image apply a blur on the image, e.g. Gaussian blur
    """
    kernel = np.matrix([
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]
    ])
    kernel = kernel / 25
    img = cv2.filter2D(img, -1, kernel)
    return img

def doSomething(img):
    """
    Given a coloured image apply any image manipulation. Be creative!
    """
    img = cv2.Sobel(img, ddepth=-1, ksize=3, dx=1, dy=0)
    return img


def processImage(img):
    """
    Given an coloured image applies the implemented smoothing and binarization.
    """
    # TODO
    img = smoothImage(img)
    img = binarizeImage(img, 125)
    return img


if __name__=="__main__":
    img = cv2.imread("test.jpg")
    utils.show(img)
    
    img1 = smoothImage(img)
    utils.show(img1)
    #cv2.imwrite("result1.jpg", img1)
    
    img2 = binarizeImage(img, 125)
    utils.show(img2)
    #cv2.imwrite("result2.jpg", img2)
   
    img3 = processImage(img)
    utils.show(img3)
    #cv2.imwrite("result3.jpg", img3)
    
    img4 = doSomething(img)
    utils.show(img4)
    #cv2.imwrite("result4.jpg", img4)
