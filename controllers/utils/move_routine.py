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

'''Routine to detect a fall and recover from it.'''

from .accelerometer import Accelerometer
from .motion_library import MotionLibrary
from .finite_state_machine import FiniteStateMachine
from .current_motion_manager import CurrentMotionManager


class MoveRoutine:
    def __init__(self, time_step, robot):
        self.time_step = time_step
        self.robot = robot
        self.current_motion = CurrentMotionManager()
        self.library = MotionLibrary()

    def exec(self):
        '''Exec single movement.'''
        
        self.current_motion.play_sync(self.library.get('GenUp'), self.robot, self.time_step)

        # self.current_motion.play_sync(self.library.get('Ghoul3'), self.robot, self.time_step)
        # self.current_motion.play_sync(self.library.get('GetUpFront'), self.robot, self.time_step)
        
        print("Finished move routine")
        while self.robot.step(self.time_step) != -1:
            pass