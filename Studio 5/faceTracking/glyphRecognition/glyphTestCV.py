# Modified By: Callam Josef Jackson-Sem
# Project: Johnny 5 Robot
# Purpose Of File: Testing OpenCV's capabilities, in this case, the glyph recognition feature as well as shape tracking
# Description: This file implements the webCam to track a series of shapes and patterns, or more specifically, glyphs. It is
# meant to operate similar to the face tracking application in which it would recognize a shape/glyph and tell the user its position
# in terms of the x and y axis. However, this feature is now for archiving purposes as it is still quite buggy.


import cv2# cv2 is imported to enable the use of OpenCV's tools and commands
# the from lines are importing the files within the directory in order to use outside functions.
from glyphfunctions import *
from webcam import Webcam

webcam = Webcam()
webcam.start()

# Constants are being established to avoid any repeatition.
QUADRILATERAL_POINTS = 4
SHAPE_RESIZE = 100.0
BLACK_THRESHOLD = 100
WHITE_THRESHOLD = 155

while True:

    # Stage 1: Read an image from our webcam
    image = webcam.get_current_frame()

    # Stage 2: Detect edges in image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5,5), 0)
    edges = cv2.Canny(gray, 100, 200)

    # Stage 3: Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

    for contour in contours:

        # Stage 4: Shape check
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.01*perimeter, True)

        if len(approx) == QUADRILATERAL_POINTS:

            # Stage 5: Perspective warping
            topdown_quad = get_topdown_quad(gray, approx.reshape(4, 2))

            # Stage 6: Border check
            resized_shape = resize_image(topdown_quad, SHAPE_RESIZE)
            if resized_shape[0, 5] > BLACK_THRESHOLD: continue

            # Stage 7: Glyph pattern
            glyph_pattern = get_glyph_pattern(resized_shape, BLACK_THRESHOLD, WHITE_THRESHOLD)
            glyph_found, glyph_rotation, glyph_substitute = get_glyph_pattern(glyph_pattern, BLACK_THRESHOLD, WHITE_THRESHOLD)

            if glyph_found:
                GLYPH_PATTERN = [0, 1, 0, 1, 0, 0, 0, 1, 1]
            

    cv2.imshow('Glyph Window', image)
    cv2.waitKey(10)
