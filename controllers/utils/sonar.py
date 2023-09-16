
'''
This module provides a sensor class using the RunningAverage class.
'''

from .running_average import RunningAverage


class Sonar():
    '''Class that provides an interface to use the sonar sensor.'''

    def __init__(self, robot, time_step, history_steps=10):
        self.right_sonar = robot.getDevice('Sonar/Right')
        self.left_sonar = robot.getDevice('Sonar/Left')
        print("robot: ", robot)
        self.right_sonar.enable(time_step)
        self.left_sonar.enable(time_step)

        self.average_left = RunningAverage(dimensions=1, history_steps=history_steps)
        self.average_right = RunningAverage(dimensions=1, history_steps=history_steps)

    def get_value_right(self):
        '''Returns the right sonar value.'''
        return self.right_sonar.getValue()
    
    def get_value_left(self):
        '''Returns the left sonar value.'''
        return self.left_sonar.getValue()

    def get_average_right(self):
        return self.average_right.average
   
    def get_average_left(self):
        return self.average_left.average

    def update_averages(self):
        values_r = self.get_value_right()
        values_l = self.get_value_left()
        self.average_left.update_average(values_r)
        self.average_right.update_average(values_l)

    def get_new_averages(self):
        '''Updates the averages and returns them.'''
        self.update_averages()

        # right, left
        # Note: right and left when seeing the robot's front.
        return [self.get_average_right(), self.get_average_left()]
