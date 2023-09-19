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

from controller import Robot
import sys

sys.path.append('..')
# Eve's locate_opponent() is implemented in this module:
from utils.image_processing import ImageProcessing as IP
from utils.fall_detection import FallDetection
from utils.gait_manager import GaitManager
from utils.camera import Camera
from utils.pose_estimator import PoseEstimator
import cv2
import numpy as np

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
        self.PE = PoseEstimator(self, self.time_step)
        
        
        # Time before changing direction to stop the robot from falling off the ring
        self.counter = 0

    def run(self):
        while self.step(self.time_step) != -1:
            # We need to update the internal theta value of the gait manager at every step:

            

            #self.getRingThreshold(self.camera.get_image())
            
            t = self.getTime()
            self.gait_manager.update_theta()
            if 0.3 < t < 1:
                self.start_sequence()
            elif t > 1:
                self.fall_detector.check()
                self.stay_in_zone()
                #self.walk()
            
            
    


    def stay_in_zone(self):
        side_max = 80
        side_mid = 48
        side_min = 10
        diagonal_max = 90

        x,y,w,height = IP.getRingBox(self,self.camera.get_image())

        img = self.camera.get_image()
        horizontal_coordinate,w,_,_ = IP.nao_detection(img)
        
  
        print(x)
                        
        if height < 5:
            #pa tras
            self.gait_manager.command_to_motors(desired_radius=0, heading_angle=3.14159) 
        
        elif height > 60:
            #pa delante
            self.gait_manager.command_to_motors(desired_radius=0, heading_angle=0)
                
        else:
            #buscar
            if horizontal_coordinate is None:
                print("No opponent found")
                self.gait_manager.command_to_motors(desired_radius=0.1, heading_angle=self.heading_angle)
            
            #atacarrr
            else:
                print("Opponent found")
                self.walk()
            
            

        



    def start_sequence(self):
        """At the beginning of the match, the robot walks forwards to move away from the edges."""
        #self.gait_manager.command_to_motors(heading_angle=0)

    def walk(self):
        """Walk towards the opponent like a homing missile."""
        

        normalized_x = self._get_normalized_opponent_x()
        #print(normalized_x)
        # We set the desired radius such that the robot walks towards the opponent.
        # If the opponent is close to the middle, the robot walks straight.
        desired_radius = (self.SMALLEST_TURNING_RADIUS / normalized_x) if abs(normalized_x) > 1e-3 else None
        # TODO: position estimation so that if the robot is close to the edge, it switches dodging direction

        if self.counter > self.TIME_BEFORE_DIRECTION_CHANGE:
            self.heading_angle = - self.heading_angle
            self.counter = 0
        self.counter += 1
        self.gait_manager.command_to_motors(desired_radius=desired_radius, heading_angle=0)

    


    
    def _get_normalized_opponent_x(self):
        """Locate the opponent in the image and return its horizontal position in the range [-1, 1]."""
        img = self.camera.get_image()
        
        horizontal_coordinate,w,_,_ = IP.nao_detection(img)
        

        if horizontal_coordinate is None:
            return 0
        else:
            horizontal_coordinate = (horizontal_coordinate + w) / 2
            return horizontal_coordinate * 2 / img.shape[1] -1
        # _, _, horizontal_coordinate = IP.locate_opponent(img)
        # if horizontal_coordinate is None:
        #     return 0
        # return horizontal_coordinate * 2 / img.shape[1] - 1
    
    


# create the Robot instance and run main loop
wrestler = RoBorregos()
print('Starting the robot...')
wrestler.run()