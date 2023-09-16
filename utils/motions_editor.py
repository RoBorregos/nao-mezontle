def generate_motion(times, values):
    """Helper function to generate files that can be used to tune joint positions."""
    joints = ['LKneePitch', 'RKneePitch', 'LAnklePitch', 'RAnklePitch', 'RHipPitch', 'LHipPitch', 'RHipRoll', 'LHipRoll', 'LHipYawPitch', 'RHipYawPitch', 'LShoulderRoll', 'RShoulderRoll', 'RShoulderPitch', 'LShoulderPitch', 'LElbowRoll', 'RElbowRoll', 'LElbowYaw', 'RElbowYaw', 'LPhalanx1', 'RPhalanx1', 'LPhalanx2', 'RPhalanx2', 'LPhalanx3', 'RPhalanx3', 'LPhalanx4', 'RPhalanx4', 'LPhalanx5', 'RPhalanx5', 'LPhalanx6', 'RPhalanx6', 'LPhalanx7', 'RPhalanx7', 'LPhalanx8', 'RPhalanx8', 'HeadPitch', 'HeadYaw', 'LAnkleRoll', 'LWristYaw', 'RAnkleRoll', 'RWristYaw']

    # Map of each joint to its open and closed values
    # joint_name: [openValue, closedValue]
    values = {'LKneePitch': [-0.09, 2.11], 'RKneePitch': [-0.09, 2.11], 'LAnklePitch': [0.92, -1.19], 'RAnklePitch': [0.92, -1.19], 'RHipPitch': [0.48, -1.77], 'LHipPitch': [0.48, -1.77], 'RHipRoll': [-0.74, 0.45], 'LHipRoll': [0.79, -0.38], 'LHipYawPitch': [-1.15, 0.74], 'RHipYawPitch': [-1.15, 0.74], 'LShoulderRoll': [1.33, -0.31], 'RShoulderRoll': [-1.33, 0.31], 'RShoulderPitch': [-2.09, 2.09], 'LShoulderPitch': [-2.09, 2.09], 'LElbowRoll': [0, -1.54], 'RElbowRoll': [0, 1.54], 'LElbowYaw': [2.09, -2.09], 'RElbowYaw': [-2.09, 2.09], 'LPhalanx1': [1, 0], 'RPhalanx1':[1, 0], 'LPhalanx2':[1, 0], 'RPhalanx2':[1, 0], 'LPhalanx3':[1, 0], 'RPhalanx3':[1, 0], 'LPhalanx4':[1, 0], 'RPhalanx4':[1, 0], 'LPhalanx5':[1, 0], 'RPhalanx5':[1, 0], 'LPhalanx6':[1, 0], 'RPhalanx6':[1, 0], 'LPhalanx7':[1, 0], 'RPhalanx7':[1, 0], 'LPhalanx8':[1, 0], 'RPhalanx8':[1, 0], 'HeadPitch': [-0.67, 0.51], 'HeadYaw': [2.09, -2.09], 'LAnkleRoll': [0.77, -0.4], 'LWristYaw': [1.82, -1.82], 'RAnkleRoll': [-0.77, 0.4], 'RWristYaw': [-1.82, 1.82]} 



