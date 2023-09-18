# Copyright 1996-2023 Cyberbotics Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This module provides functions to work with images coming from the NAO's cameras.
"""

import numpy as np
import cv2


class ImageProcessing():

    @staticmethod
    def color_detection(image, starting_color='red'):

        hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        #0-179, 0-255 and 0-255 Hue, saturation, value
        bounds_blue = [(100, 100, 80),(120, 255, 255)]
        bounds_white = [(20, 5, 200),(120, 50, 240)]
        bounds_red = [(170, 140, 140),(179, 255, 255)]

        mask_blue = cv2.inRange(hsv_img, bounds_blue[0], bounds_blue[1])
        mask_white = cv2.inRange(hsv_img, bounds_white[0], bounds_white[1])
        mask_red = cv2.inRange(hsv_img, bounds_red[0], bounds_red[1])

        mask_blue = np.array(mask_blue)
        mask_white = np.array(mask_white)
        mask_red = np.array(mask_red)


        masked_blue = cv2.bitwise_and(image, image, mask=mask_blue)
        masked_white = cv2.bitwise_and(image, image, mask=mask_white)
        masked_red = cv2.bitwise_and(image, image, mask=mask_red)

        if (starting_color == 'red'):
            color_image = cv2.bitwise_or(masked_blue, masked_white)
        else:
            color_image = cv2.bitwise_or(masked_red, masked_white)

        

        blur = cv2.GaussianBlur(color_image, (0, 0), 3)
        #cv2.imwrite(os.path.join(results_dir, file), blur)

        gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

        b = cv2.cvtColor(masked_blue, cv2.COLOR_BGR2GRAY)
        w = cv2.cvtColor(masked_white, cv2.COLOR_BGR2GRAY)
        r = cv2.cvtColor(masked_red, cv2.COLOR_BGR2GRAY)

        blue_contours, _ = cv2.findContours(b, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        red_contours, _ = cv2.findContours(r, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if (blue_contours == None):
            return None, None, None, None
        contours, _ = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        largest_contour = contours[0]
        x_min = color_image.shape[0]
        x_max = 0

        flag = False
        if starting_color == 'red':
            color_contours = blue_contours
        else:
            color_contours = red_contours

        

        for cont in contours:
            x,y,w,h = cv2.boundingRect(cont)
            xf = x + w
            yf = y + h

            for color in color_contours:
                xb,yb,wb,hb = cv2.boundingRect(color)

                if (xb >= x and xb + wb <= xf and yb >= y and yb + hb <= yf):
                    largest_contour = cont
                    x_min = min(x_min,xb)
                    x_max = max(x_max,xb + wb)
                    flag = True

            if flag:
                break

        if not flag:
            return None, None, None, None

  

        x,y,w,h = cv2.boundingRect(largest_contour)
        #cv2.drawContours(color_image,contours[0],-1,(0,0,205),2,cv2.LINE_AA)
        color_image = cv2.rectangle(color_image,(x_min,y),(x_max,y+h),(255,0,0),2)
        return x_min, x_max, y, y+h
    
    @staticmethod
    def get_largest_contour(image):
        """Get the largest contour in an image."""
        contours, _ = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        if len(contours) == 0:
            return None
        return contours[0]

    @staticmethod
    def get_contour_centroid(contour):
        """Get the centroid of a contour."""
        M = cv2.moments(contour)
        if M['m00'] != 0:
            vertical_coordinate = int(M['m01'] / M['m00'])
            horizontal_coordinate = int(M['m10'] / M['m00'])
        else:
            # if the contour has an area of 0, the centroid cannot be computed this way
            # we use the mean of the contour points instead
            vertical_coordinate, horizontal_coordinate = np.mean(contour, axis=0)[0]
        return int(vertical_coordinate), int(horizontal_coordinate)

    @classmethod
    def locate_opponent(cls, img):
        """Image processing demonstration to locate the opponent robot in an image."""
        # we suppose the robot to be located at a concentration of multiple color changes (big Laplacian values)
        laplacian = cv2.Laplacian(img, cv2.CV_8U, ksize=3)
        # those spikes are then smoothed out using a Gaussian blur to get blurry blobs
        blur = cv2.GaussianBlur(laplacian, (0, 0), 2)
        # we apply a threshold to get a binary image of potential robot locations
        gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY)
        # the binary image is then dilated to merge small groups of blobs together
        closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15)))
        # the robot is assumed to be the largest contour
        largest_contour = cls.get_largest_contour(closing)
        if largest_contour is not None:
            # we get its centroid for an approximate opponent location
            vertical_coordinate, horizontal_coordinate = cls.get_contour_centroid(largest_contour)
            img = cv2.line(img, (vertical_coordinate-50,horizontal_coordinate), (vertical_coordinate+50,horizontal_coordinate), color=(250, 250, 0), thickness=3)
            img = cv2.line(img, (vertical_coordinate,horizontal_coordinate-50), (vertical_coordinate,horizontal_coordinate+50), color=(250, 250, 0), thickness=3)
            img = cv2.circle(img, (vertical_coordinate,horizontal_coordinate), 40, (0,0,250), 5)
            cv2.imshow('mask', img)
            return largest_contour, vertical_coordinate, horizontal_coordinate
        else:
            # if no contour is found, we return None
            return None, None, None
