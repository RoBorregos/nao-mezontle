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
# comment de la suerte 1
# pa ti

"""
Demonstrates the gait manager (inverse kinematics + simple ellipsoid path).
"""

from controller import Robot, Motion
import sys

sys.path.append('..')
# Eve's locate_opponent() is implemented in this module:
from utils.sonar import Sonar
# from utils.move_routine import MoveRoutine
from utils.image_processing import ImageProcessing as IP
from utils.fall_detection import FallDetection
from utils.gait_manager import GaitManager
from utils.camera import Camera
from utils.motion_library import MotionLibrary
from utils.pose_estimator import PoseEstimator
from utils.current_motion_manager import CurrentMotionManager
from utils.behaviours import Behaviours
import cv2
import numpy as np
import time


GHOUL_READY = True
PUNCH_READY = True

class RoBorregos (Robot):
    SMALLEST_TURNING_RADIUS = 0.1
    SAFE_ZONE = 0.75
    TIME_BEFORE_DIRECTION_CHANGE = 200  # 8000 ms / 40 ms

    def __init__(self):
        Robot.__init__(self)
        self.time_step = int(self.getBasicTimeStep())

        self.sonar = Sonar(self, self.time_step)
        self.camera = Camera(self)
        self.fall_detector = FallDetection(self.time_step, self)
        self.gait_manager = GaitManager(self, self.time_step)
        self.behaviours = Behaviours(self, self.time_step)
        self.current_motion = CurrentMotionManager()
        self.library = MotionLibrary()
        self.heading_angle = 3.14 / 2
        self.PE = PoseEstimator(self, self.time_step)
        self.starting_color = 'blue'
        self.last_seen = None

        self.last_state = None
        self.last_state_change = None
        self.change_time = 0.1

        self.last_handle = None
        self.current_handle = None

        self.last_change = time.time()
        self.TIMEOUT = 0.5
        self.last_rotation = time.time()
        self.last_search = time.time()
        
        # Time before changing direction to stop the robot from falling off the ring
        self.counter = 0

    def run(self):

        while self.step(self.time_step) != -1:
            # We need to update the internal theta value of the gait manager at every step:
            t = self.getTime()
            self.gait_manager.update_theta()
            if 0.3 < t < 0.5:
                self.start_sequence()
            elif t > 1:
                self.fall_detector.check()
                self.stay_in_zone()

    def handle_state_change(self, current_state):
        if self.last_state != current_state:
            self.last_state_change = time.time()
            
        self.last_state = current_state

        return time.time() - self.last_state_change > self.change_time
        
    def is_nao_near(self):
        img = self.camera.get_image()
        horizontal_coordinate,w,_,_,area = IP.nao_detection(img, starting_color=self.starting_color)

        if horizontal_coordinate is None:
            return False

        print("Sonar: ", self.sonar.get_new_averages()[0])
        print("Area:", area)
        print("Width:", w)
        print("Diff:", w - horizontal_coordinate)
        if area > 15000 and self.sonar.get_new_averages()[0] < 0.26 or w - horizontal_coordinate > 165:
            return True
        return False

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

    def stay_in_zone(self):
        # self.current_motion.play_sync(self.library.get('ArmsUp'), self, self.time_step)
        # self.current_motion.play_sync(self.library.get('SafePosition'), self, self.time_step)
        # self.behaviours.safe_position()
        # print("Punch sequence")
        # self.behaviours.punch_position_legs()
        # while self.step(self.time_step) != -1:
        #     pass
        #     self.current_motion.play_sync(self.library.get('ArmsUp'), self, self.time_step)


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
        # TO-DO: Considerar el caso de estar en la orilla del ring.    
        # elif height > 80:
        #     #pa delante
        #     print("Forward")
        #     self.gait_manager.command_to_motors(desired_radius=0, heading_angle=0)
                
        else:
            # Buscar al oponente.
            if horizontal_coordinate is None:

                print("Search")
                if self.handle_state_change('search'):
                    if time.time() - self.last_search > 0.005:
                        self.last_search = time.time()


                        normalized_x = self._get_normalized_opponent_x()
                        desired_radius = (self.SMALLEST_TURNING_RADIUS / normalized_x) if abs(normalized_x) > 1e-3 else None
                        # Girar hacia el último lado que se vio.
                        if self.last_seen is None:
                            print("Search 1")
                            self.gait_manager.command_to_motors(desired_radius=0.01, heading_angle=1.57)
                        elif self.last_seen < img.shape[1]/2:
                            print("Search 2")
                            self.gait_manager.command_to_motors(desired_radius=-0.01, heading_angle=1.57)
                        else:
                            print("Search 3")
                            self.gait_manager.command_to_motors(desired_radius=0.01, heading_angle=1.57)

            # comment de la suerte
            # Atacar al oponente.
            else:

                print("Attack")
                
                self.current_handle = self.handle_state_change('attack')
                if self.current_handle:
                    print("Attacking...")
                    if  self.is_nao_near() and PUNCH_READY:
                        # self.behaviours.safe_position()
                        # self.current_motion.play_sync(self.library.get('SafePosition'), self, self.time_step)
                        print("Punch sequence")
                        # self.behaviours.punch_position_legs()
                        self.last_change = time.time()
                        while self.step(self.time_step) != -1:
                            if self.fall_detector.check():
                                print("Fallen")
                                break
                            if self.is_nao_near():                                     
                                
                                self.current_motion.play_sync(self.library.get('ArmsUp3'), self, self.time_step)
                                self.last_change = time.time()
                                
                                if time.time() - self.last_rotation > 1:
                                    while time.time() - self.last_change < self.TIMEOUT:
                                    #if time.time() - self.last_change > self.TIMEOUT:
                                        print("Rotating")
                                        self.gait_manager.command_to_motors(desired_radius=0.01, heading_angle=1.57)
                                        #self.last_change = time.time()
                                    self.last_rotation = time.time()
                                    
                                #self.current_motion.play_sync(self.library.get('ArmsUp'), self, self.time_step)
                            else:
                                print("Nao not near")
                                self.last_change = time.time()
                                break

                        # self.current_motion.play_sync(self.library.get('SafePosition'), self, self.time_step)

                    print("Walking...")
                    self.walk()

                if self.last_handle != self.current_handle:
                    self.last_handle = self.current_handle

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
       

        
        if GHOUL_READY:
            motion = Motion('../motions/Ghoul3.motion')  # look into this text file, it's easy to understand
            motion.setLoop(False)
            motion.play()

            
            start_time = time.time()
            while self.step(self.time_step) != -1 and time.time() - start_time < 1.6:
                pass
            
            #motion = Motion('../motions/GetUpFront.motion')  # look into this text file, it's easy to understand
            motion.setLoop(False)
            motion.play()

            start_time = time.time()
            while self.step(self.time_step) != -1 and time.time() - start_time < 1.5:
                pass
        # else:
        #     self.safe_position()


        self.headMotor = self.getDevice(f'HeadPitch')
        self.headMotor.setPosition(0.50)
        self.headMotor = self.getDevice(f'HeadYaw')
        self.headMotor.setPosition(0.0)



    def walk(self):
        """Walk towards the opponent like a homing missile."""
        self.behaviours.base_position()

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