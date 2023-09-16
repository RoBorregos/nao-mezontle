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

"""Minimalist controller example for the Robot Wrestling Tournament.
   Demonstrates how to play a simple motion file."""

from controller import Robot
import sys
sys.path.append('..')

from utils.image_processing import ImageProcessing as IP
from utils.fall_detection import FallDetection
from utils.gait_manager import GaitManager
from utils.camera import Camera
from utils.sonar import Sonar
from utils.move_routine import MoveRoutine

class Wrestler (Robot):
    def __init__(self):
        Robot.__init__(self)
        self.time_step = int(self.getBasicTimeStep())
        self.camera = Camera(self)
        self.fall_detector = FallDetection(self.time_step, self)
        self.gait_manager = GaitManager(self, self.time_step)
        self.sonar = Sonar(self, self.time_step)

    def run(self):
        #self.singleMovemement = MoveRoutine(self.time_step, self)
        print("Test in opponent")
        while self.step(self.time_step) != -1:
            right, left = self.sonar.get_new_averages()
            print("r: " + str(right) + " l: " + str(left))
        
        #self.singleMovemement.exec()
        # motion = Motion('../motions/GetUp2.motion')  # look into this text file, it's easy to understand
        # motion.setLoop(True)
        # motion.play()
        # time_step = int(self.getBasicTimeStep())  # retrieves the WorldInfo.basicTimeTime (ms) from the world file
        # while self.step(time_step) != -1:  # runs the hand wave motion in a loop until Webots quits
        #     pass


# create the Robot instance and run main loop
wrestler = Wrestler()
wrestler.run()
