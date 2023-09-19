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
import time

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
        self.starting_color = 'blue'
        self.last_seen = None

        
        # Time before changing direction to stop the robot from falling off the ring
        self.counter = 0

    def run(self):
        while self.step(self.time_step) != -1:
            # We need to update the internal theta value of the gait manager at every step:
            t = self.getTime()
            self.gait_manager.update_theta()
            if 0.3 < t < 1:
                self.start_sequence()
            elif t > 1:
                self.fall_detector.check()
                self.stay_in_zone()

    def stay_in_zone(self):

                
        side_max = 80
        side_mid = 48
        side_min = 10
        diagonal_max = 90

        x,y,w,height,ringstatus = IP.getRingBox(self,self.camera.get_image())

        img = self.camera.get_image()
        horizontal_coordinate,w,_,_,_ = IP.nao_detection(img, starting_color=self.starting_color)
        
        if horizontal_coordinate is not None:
            self.last_seen = horizontal_coordinate
        
        if not ringstatus or height < 5:
            # Prevenir Salirse del Ring.
            print("Backwards")
            self.gait_manager.command_to_motors(desired_radius=0, heading_angle=3.14159) 
        # TO-DO: Considerar el caso de acercase al centro del ring.    
        # elif height > 80:
        #     #pa delante
        #     print("Forward")
        #     self.gait_manager.command_to_motors(desired_radius=0, heading_angle=0)
                
        else:
            # Buscar al oponente.
            if horizontal_coordinate is None:

                print("Search")
                # Girar hacia el último lado que se vio.
                if self.last_seen is None:
                    self.gait_manager.command_to_motors(desired_radius=0.1, heading_angle=self.heading_angle)
                elif self.last_seen < img.shape[1]/2:
                    self.gait_manager.command_to_motors(desired_radius=0, heading_angle=3.14159)
                else:
                    self.gait_manager.command_to_motors(desired_radius=0, heading_angle=0)
                    
            # Atacar al oponente.
            else:
                print("Attack")
                self.walk()
         

    # Find out current robot's color.
    def get_robot_color(self):
        hc_blue = None
        hc_red = None
        start_time = time.time()
        while hc_blue is None and hc_red is None and time.time() - start_time < 3:
            img = self.camera.get_image()
            hc_blue,_,_,_,a_blue = IP.nao_detection(img, starting_color='blue')
            hc_red,_,_,_,a_red = IP.nao_detection(img, starting_color='red')

        if hc_blue is None and hc_red is None:
            self.starting_color = 'red'

        if hc_blue is None:
            self.starting_color = 'red'
        elif hc_red is not None:
            if a_blue > a_red:
                self.starting_color = 'blue'
            else:
                self.starting_color = 'red'
        elif hc_red is None:
            self.starting_color = 'blue'


    def start_sequence(self):
        """At the beginning of the match, the robot walks forwards to move away from the edges."""
        self.get_robot_color()

        self.headMotor = self.getDevice(f'HeadPitch')
        self.headMotor.setPosition(0.40)

        self.safe_position()
        
    def safe_position(self):
        hip_pitch = -1.6
        ankle_pitch = -0.6
        knee_pitch = 1.8
        hip_roll = 0.2
        ankle_roll = -0.39

        # self.LhipRoll = self.getDevice(f'LHipRoll')
        # self.LhipRoll.setPosition(hip_roll)
        
        # self.RhipRoll = self.getDevice(f'RHipRoll')
        # self.RhipRoll.setPosition(-hip_roll)

        # self.LankleRoll = self.getDevice(f'LAnkleRoll')
        # self.LankleRoll.setPosition(ankle_roll)

        # self.RankleRoll = self.getDevice(f'RAnkleRoll')
        # self.RankleRoll.setPosition(-ankle_roll)

        self.LhipPitch = self.getDevice(f'LHipPitch')
        self.LhipPitch.setPosition(hip_pitch)

        self.RhipPitch = self.getDevice(f'RHipPitch')
        self.RhipPitch.setPosition(hip_pitch)

        self.LKneePitch = self.getDevice(f'LKneePitch')
        self.LKneePitch.setPosition(knee_pitch)

        self.RKneePitch = self.getDevice(f'RKneePitch')
        self.RKneePitch.setPosition(knee_pitch)

        self.LAnklePitch = self.getDevice(f'LAnklePitch')
        self.LAnklePitch.setPosition(ankle_pitch)

        self.RAnklePitch = self.getDevice(f'RAnklePitch')
        self.RAnklePitch.setPosition(ankle_pitch)

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
        
        horizontal_coordinate,w,_,_,_ = IP.nao_detection(img) 

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