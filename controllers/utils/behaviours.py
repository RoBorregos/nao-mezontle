# Set positions to motors directly to perform movements.

class Behaviours():

    def __init__(self, robot, time_step):
        self.time_step = time_step
        
        self.joints = joints = ['LKneePitch', 'RKneePitch', 'LAnklePitch', 'RAnklePitch', 'RHipPitch', 'LHipPitch', 'RHipRoll', 'LHipRoll', 'LHipYawPitch', 'RHipYawPitch', 'LShoulderRoll', 'RShoulderRoll', 'RShoulderPitch', 'LShoulderPitch', 'LElbowRoll', 'RElbowRoll', 'LElbowYaw', 'RElbowYaw', 'LPhalanx1', 'RPhalanx1', 'LPhalanx2', 'RPhalanx2', 'LPhalanx3', 'RPhalanx3', 'LPhalanx4', 'RPhalanx4', 'LPhalanx5', 'RPhalanx5', 'LPhalanx6', 'RPhalanx6', 'LPhalanx7', 'RPhalanx7', 'LPhalanx8', 'RPhalanx8', 'HeadPitch', 'HeadYaw', 'LAnkleRoll', 'LWristYaw', 'RAnkleRoll', 'RWristYaw']
        
        # self.shoulder_joints = ['RShoulderRoll', 'LShoulderRoll', 'RShoulderPitch', 'LShoulderPitch']
        # self.elbow_joints = ['RElbowRoll', 'LElbowRoll', 'RElbowYaw', 'LElbowYaw']

        self.motors = {}

        for joint in self.joints:
            motor = robot.getDevice(joint)
            position_sensor = motor.getPositionSensor()
            position_sensor.enable(time_step)
            self.motors[joint] = motor

    def base_position(self):
        """Position when moving"""
        self.motors['RShoulderRoll'].setPosition(-0.4)
        self.motors['LShoulderRoll'].setPosition(0.4)
        self.motors['RShoulderPitch'].setPosition(0.7)
        self.motors['LShoulderPitch'].setPosition(0.7)
        self.motors['RElbowRoll'].setPosition(0.8)
        self.motors['LElbowRoll'].setPosition(-0.8)
        self.motors['RElbowYaw'].setPosition(0.0)
        self.motors['LElbowYaw'].setPosition(0.0)

    def punch_position_legs(self):
        #RKneePitch,LKneePitch,RAnklePitch,LAnklePitch,RAnkleRoll,LAnkleRoll,RHipPitch,LHipPitch,RHipRoll,LHipRoll,RHipYawPitch,LHipYawPitch
        #0.6096,0.6096,-0.1677,-0.1677,0.0,-0.0,-0.0,-0.0,-0.2096,0.2096,-0.7298,-0.7298
        self.motors['RKneePitch'].setPosition(0.6096)
        self.motors['LKneePitch'].setPosition(0.6096)
        self.motors['RAnklePitch'].setPosition(-0.1677)
        self.motors['LAnklePitch'].setPosition(-0.1677)
        self.motors['RAnkleRoll'].setPosition(0.0)
        self.motors['LAnkleRoll'].setPosition(-0.0)
        self.motors['RHipPitch'].setPosition(-0.0)
        self.motors['LHipPitch'].setPosition(-0.0)
        self.motors['RHipRoll'].setPosition(-0.2096)
        self.motors['LHipRoll'].setPosition(0.2096)
        self.motors['RHipYawPitch'].setPosition(-0.7298)
        self.motors['LHipYawPitch'].setPosition(-0.7298)

    
    def safe_position (self):
        hip_pitch = 0.48
        ankle_pitch = -1.19
        knee_pitch = 1.5
        hip_yaw_pitch = -1.0
        hip_roll = -0.6

        self.motors['LHipPitch'].setPosition(hip_pitch)
        self.motors['RHipPitch'].setPosition(hip_pitch)

        self.motors['LAnklePitch'].setPosition(ankle_pitch)
        self.motors['RAnklePitch'].setPosition(ankle_pitch)
        
        self.motors['RKneePitch'].setPosition(knee_pitch)
        self.motors['LKneePitch'].setPosition(knee_pitch)

        self.motors['RHipYawPitch'].setPosition(hip_yaw_pitch)
        self.motors['LHipYawPitch'].setPosition(hip_yaw_pitch)

        self.motors['RHipRoll'].setPosition(hip_roll * -1)
        self.motors['LHipRoll'].setPosition(hip_roll)
        