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
Demonstrates the gait manager (inverse kinematics + simple ellipsoid path).
"""

from controller import Robot, Motion
import sys
sys.path.append('..')
# Eve's locate_opponent() is implemented in this module:
from utils.image_processing import ImageProcessing as IP
from utils.fall_detection import FallDetection
from utils.gait_manager import GaitManager
from utils.camera import Camera
import mediapipe as mp
import cv2
import numpy as np

# Calling the pose solution from MediaPipe
mp_pose = mp.solutions.pose

# Calling the solution for image drawing from MediaPipe
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

class RoBorregos (Robot):
    SMALLEST_TURNING_RADIUS = 0.1
    SAFE_ZONE = 0.75
    TIME_BEFORE_DIRECTION_CHANGE = 200  # 8000 ms / 40 ms

    def __init__(self):
        Robot.__init__(self)
        self.time_step = int(self.getBasicTimeStep())

        self.camera = Camera(self)
        self.fall_detector = FallDetection(self.time_step, self)
        self.gait_manager = GaitManager(self, self.time_step)
        self.heading_angle = 3.14 / 2
        # Time before changing direction to stop the robot from falling off the ring
        self.counter = 0

    def run(self):
        head_init = Motion('../motions/HeadDown.motion')
        head_init.setLoop(False)
        head_init.play()
        with mp_pose.Pose(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as pose:
            while self.step(self.time_step) != -1:
                # We need to update the internal theta value of the gait manager at every step:
                t = self.getTime()
                self.gait_manager.update_theta()
                self.poseEstimator(pose)
                self.getRingThreshold(self.camera.get_image())
                # cv2.imwrite('image.png', self.camera.get_image())
                if 0.3 < t < 2:
                    self.start_sequence()
                elif t > 2:
                    self.fall_detector.check()
                    self.walk()

    def getRingThreshold(self, img):
        # (hMin = 17 , sMin = 61, vMin = 189), (hMax = 29 , sMax = 76, vMax = 255)
        # LAB_THRESHOLD = (71, 90, -10, 6, 15, 72)
        # image = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        # mask = cv2.inRange(image, (LAB_THRESHOLD[0], LAB_THRESHOLD[2], LAB_THRESHOLD[4]), (LAB_THRESHOLD[1], LAB_THRESHOLD[3], LAB_THRESHOLD[5]))
        # cv2.imshow('mask', mask)
        lower = np.array([17, 61, 189])
        upper = np.array([29, 76, 255])
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower, upper)
        cv2.imshow('mask', mask)
        # return mask

    def poseEstimator(self, pose):
        """Estimates the oponents's pose using the camera."""
        img = self.camera.get_image()
        imageCopy = img.copy()
        imageCopy = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imageCopy = cv2.resize(imageCopy, (480, 640))
        results = pose.process(imageCopy)
        imageCopy.flags.writeable = True
        image_w = cv2.cvtColor(imageCopy, cv2.COLOR_RGB2BGR)
        mp_drawing.draw_landmarks(
            image_w,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
        cv2.imshow('MediaPipe Pose', image_w)
        

    def start_sequence(self):
        """At the beginning of the match, the robot walks forwards to move away from the edges."""
        self.gait_manager.command_to_motors(heading_angle=0)

    def walk(self):
        """Walk towards the opponent like a homing missile."""
        normalized_x = self._get_normalized_opponent_x()
        # We set the desired radius such that the robot walks towards the opponent.
        # If the opponent is close to the middle, the robot walks straight.
        desired_radius = (self.SMALLEST_TURNING_RADIUS / normalized_x) if abs(normalized_x) > 1e-3 else None
        # TODO: position estimation so that if the robot is close to the edge, it switches dodging direction
        if self.counter > self.TIME_BEFORE_DIRECTION_CHANGE:
            self.heading_angle = - self.heading_angle
            self.counter = 0
        self.counter += 1
        self.gait_manager.command_to_motors(desired_radius=desired_radius, heading_angle=self.heading_angle)

    def _get_normalized_opponent_x(self):
        """Locate the opponent in the image and return its horizontal position in the range [-1, 1]."""
        img = self.camera.get_image()
        _, _, horizontal_coordinate = IP.locate_opponent(img)
        if horizontal_coordinate is None:
            return 0
        return horizontal_coordinate * 2 / img.shape[1] - 1


# create the Robot instance and run main loop
wrestler = RoBorregos()
wrestler.run()