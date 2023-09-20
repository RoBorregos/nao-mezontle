# Used to log joint position for motion creation.

class LogPosition():

    def __init__(self, robot, time_step):
        joints = ['LKneePitch', 'RKneePitch', 'LAnklePitch', 'RAnklePitch', 'RHipPitch', 'LHipPitch', 'RHipRoll', 'LHipRoll', 'LHipYawPitch', 'RHipYawPitch', 'LShoulderRoll', 'RShoulderRoll', 'RShoulderPitch', 'LShoulderPitch', 'LElbowRoll', 'RElbowRoll', 'LElbowYaw', 'RElbowYaw', 'LPhalanx1', 'RPhalanx1', 'LPhalanx2', 'RPhalanx2', 'LPhalanx3', 'RPhalanx3', 'LPhalanx4', 'RPhalanx4', 'LPhalanx5', 'RPhalanx5', 'LPhalanx6', 'RPhalanx6', 'LPhalanx7', 'RPhalanx7', 'LPhalanx8', 'RPhalanx8', 'HeadPitch', 'HeadYaw', 'LAnkleRoll', 'LWristYaw', 'RAnkleRoll', 'RWristYaw']

        self.time_step = time_step

        self.motors = {}
        self.positions = {}

        for joint in joints:
            motor = robot.getDevice(joint)
            position_sensor = motor.getPositionSensor()
            position_sensor.enable(time_step)
            self.motors[joint] = motor
            self.positions[joint] = position_sensor


    def log_position(self):
        """Position when moving"""
        self.rigid_position()
        print("Log position: ")
        for joint in self.motors:
            print(f'{joint[0:4]}:{round(self.positions[joint].getValue(), 2)}', end=", ")

        print("\n")


    def rigid_position(self):
        """Stop joint movement"""
        for joint in self.motors:
            max_pos = self.motors[joint].getMaxPosition()
            min_pos = self.motors[joint].getMinPosition()
            position = max(min(self.positions[joint].getValue(), max_pos), min_pos)
            self.motors[joint].setPosition(position)