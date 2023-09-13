# Choregraphe simplified export in Python.

def moveup():
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.08, 0.48, 1, 1.12, 1.24, 1.36])
    keys.append([0.487771, 0.16563, 0.210117, -0.10282, -0.122762, 0.512643])

    names.append("HeadYaw")
    times.append([0.08, 0.48, 1, 1.12, 1.24, 1.36])
    keys.append([-0.0245859, -0.159578, -0.162646, 0.0183661, -4.19617e-05, -0.021518])

    names.append("LAnklePitch")
    times.append([0.08, 0.48, 1, 1.12, 1.24, 1.36])
    keys.append([-1.13674, 0.0674542, 0.391128, 0.31903, 0.501576, 0.501576])

    names.append("LAnkleRoll")
    times.append([0.08, 0.48, 1, 1.12, 1.24, 1.36])
    keys.append([0.00924586, 0.165714, -0.05058, -0.00609397, 0.00464392, 0.00464392])

    names.append("LElbowRoll")
    times.append([0.08, 0.48, 1, 1.12, 1.24, 1.36])
    keys.append([-0.0720561, -0.116542, -0.302157, -0.355846, -0.415673, -0.0429101])

    names.append("LElbowYaw")
    times.append([0.08, 0.48, 1, 1.12, 1.24, 1.36])
    keys.append([-1.48649, -1.23031, -1.21037, -1.21344, -1.55092, -1.55092])

    names.append("LHand")
    times.append([0.08, 0.48, 1, 1.12, 1.24, 1.36])
    keys.append([0.0264, 0.0264, 0.0296, 0.0264, 0.0264, 0.0264])

    names.append("LHipPitch")
    times.append([0.08, 0.48, 1, 1.12, 1.24, 1.36])
    keys.append([0.193327, -1.53589, -1.30846, -1.10751, -0.722472, -0.724006])

    names.append("LHipRoll")
    times.append([0.08, 0.48, 1, 1.12, 1.24, 1.36])
    keys.append([-0.0689882, -0.231591, -0.153358, -0.170232, -0.113474, -0.113474])

    names.append("LHipYawPitch")
    times.append([0.08, 0.48, 1, 1.12, 1.24, 1.36])
    keys.append([-0.0260359, -0.0413762, -0.0444441, -0.052114, 0.0614019, 0.0614019])

    names.append("LKneePitch")
    times.append([0.08, 0.48, 1, 1.12, 1.24, 1.36])
    keys.append([0.130348, 0.523053, 0.490837, 0.523053, 0.682588, 0.682588])

    names.append("LShoulderPitch")
    times.append([0.08, 0.48, 1, 1.12, 1.24, 1.36])
    keys.append([-1.50336, 1.28852, 2.01257, 2.01716, 1.9957, 2.06472])

    names.append("LShoulderRoll")
    times.append([0.08, 0.48, 1, 1.12, 1.24, 1.36])
    keys.append([0.107338, 0.11194, -0.036858, 0.022968, -0.0153821, -0.0261199])

    names.append("LWristYaw")
    times.append([0.08, 0.48, 1, 1.12, 1.24, 1.36])
    keys.append([0.88661, 1.3238, 1.30846, 1.30386, 1.62293, 1.49868])

    names.append("RAnklePitch")
    times.append([0.08, 0.48, 1, 1.12, 1.24, 1.36])
    keys.append([-1.10904, 0.374338, 0.699545, 0.638187, 0.570689, 0.570689])

    names.append("RAnkleRoll")
    times.append([0.08, 0.48, 1, 1.12, 1.24, 1.36])
    keys.append([0.0747926, 0.165714, 0.154976, 0.159578, 0.159578, 0.159578])

    names.append("RElbowRoll")
    times.append([0.08, 0.48, 1, 1.12, 1.24, 1.36])
    keys.append([0.262356, 0.0506639, 0.127364, 0.14884, 0.168782, 0.154976])

    names.append("RElbowYaw")
    times.append([0.08, 0.48, 1, 1.12, 1.24, 1.36])
    keys.append([1.61526, 1.66895, 1.6981, 1.69043, 1.59839, 1.60299])

    names.append("RHand")
    times.append([0.08, 0.48, 1, 1.12, 1.24, 1.36])
    keys.append([0.6392, 0.0188, 0.3452, 0.2932, 0.654, 0.654])

    names.append("RHipPitch")
    times.append([0.08, 0.48, 1, 1.12, 1.24, 1.36])
    keys.append([0.139552, -1.2748, -1.20577, -0.898967, -0.360533, -0.365133])

    names.append("RHipRoll")
    times.append([0.08, 0.48, 1, 1.12, 1.24, 1.36])
    keys.append([-0.116542, -0.0168321, -0.202446, -0.156426, -0.128814, -0.12728])

    names.append("RHipYawPitch")
    times.append([0.08, 0.48, 1, 1.12, 1.24, 1.36])
    keys.append([-0.0260359, -0.0413762, -0.0444441, -0.052114, 0.0614019, 0.0614019])

    names.append("RKneePitch")
    times.append([0.08, 0.48, 1, 1.12, 1.24, 1.36])
    keys.append([0.150374, -0.0475121, 0.0951499, 0.067538, 0.0598679, 0.0598679])

    names.append("RShoulderPitch")
    times.append([0.08, 0.48, 1, 1.12, 1.24, 1.36])
    keys.append([-1.41891, 1.26713, 1.9513, 1.8301, 1.92061, 2.08567])

    names.append("RShoulderRoll")
    times.append([0.08, 0.48, 1, 1.12, 1.24, 1.36])
    keys.append([-0.0107799, -0.066004, 0.049046, -0.0874801, 0.0383082, 0.0413762])

    names.append("RWristYaw")
    times.append([0.08, 0.48, 1, 1.12, 1.24, 1.36])
    keys.append([-1.37144, -1.39445, -1.79483, -1.72733, -1.61228, -1.8209])

    return names, times, keys
