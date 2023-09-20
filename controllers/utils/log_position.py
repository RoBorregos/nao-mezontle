# Used to log joint position for motion creation.

from controller import AnsiCodes
import sys

class LogPosition():

    # log_groups = [knees, ankles, hip, shoulders, arms, hands, head], 1 to log, 0 to ignore
    def __init__(self, robot, time_step, log_groups=[0, 0, 0, 0, 0, 0, 0]):
        
        if len(log_groups) != 7:
            print("ERROR: Invalid number of log groups in LogPosition.__init__")
            print("Only seven values are accepted, one for each joint group.")
            return
        
        # [knees, ankles, hip, shoulders, arms, hands, head]
        joint_groups = self.joint_groups()

        self.joints = []

        for i in range(len(log_groups)):
            if log_groups[i] == 1:
                for joint in joint_groups[i]:
                    self.joints.append(joint)

        self.time_step = time_step

        self.motors = {}
        self.positions = {}

        for joint in self.joints:
            motor = robot.getDevice(joint)
            position_sensor = motor.getPositionSensor()
            position_sensor.enable(time_step)
            self.motors[joint] = motor
            self.positions[joint] = position_sensor


    def log_position(self, log_joint_names=False):
        self.rigid_position()
        print("Log position: ")

        log_output = ""
        for joint in self.joints:
            if log_joint_names:
                log_output += f'{joint}:{round(self.positions[joint].getValue(), 4)},'
            else:
                log_output += f'{round(self.positions[joint].getValue(), 4)},'

        print(AnsiCodes.BLUE_FOREGROUND + log_output[:-1] + AnsiCodes.RESET)
        print("\n")


    def rigid_position(self):
        """Stop joint movement"""
        for joint in self.motors:
            max_pos = self.motors[joint].getMaxPosition()
            min_pos = self.motors[joint].getMinPosition()
            position = max(min(self.positions[joint].getValue(), max_pos), min_pos)
            self.motors[joint].setPosition(position)
    
    def log_header(self):
        """Function to load the .motion header, considering selected joints"""

        joints_str = ""
        for joint in self.joints:
            joints_str += f"{joint},"

        print(AnsiCodes.BLUE_FOREGROUND + "##WEBOTS_MOTION,V1.0," + joints_str[:-1] + AnsiCodes.RESET + "\n")

    
    def joint_groups(self):
        knees = [
        "RKneePitch",
        "LKneePitch",
        ]
        ankles = [
            "RAnklePitch",
            "LAnklePitch",
            "RAnkleRoll",
            "LAnkleRoll",
        ]
        hip = [
            "RHipPitch",
            "LHipPitch",
            "RHipRoll",
            "LHipRoll",
            "RHipYawPitch",
            "LHipYawPitch",
        ]
        shoulders = [
            "RShoulderRoll",
            "LShoulderRoll",
            "RShoulderPitch",
            "LShoulderPitch",
        ]
        arms = [
            "RElbowRoll",
            "LElbowRoll",
            "RElbowYaw",
            "LElbowYaw",
        ]
        hands = [
            "RWristYaw",
            "LWristYaw",
            "RPhalanx1",
            "LPhalanx1",
            "RPhalanx2",
            "LPhalanx2",
            "RPhalanx3",
            "LPhalanx3",
            "RPhalanx4",
            "LPhalanx4",
            "RPhalanx5",
            "LPhalanx5",
            "RPhalanx6",
            "LPhalanx6",
            "RPhalanx7",
            "LPhalanx7",
            "RPhalanx8",
            "LPhalanx8",
        ]
        head = [
            "HeadPitch",
            "HeadYaw",
        ]

        return [knees, ankles, hip, shoulders, arms, hands, head]
    