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

def grab(): 
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0, 0.48, 0.96, 1.44, 1.92])
    keys.append([-0.0107799, -0.230142, -0.230142, -0.230142, -0.230142])

    names.append("HeadYaw")
    times.append([0, 0.48, 0.96, 1.44, 1.92])
    keys.append([0.00149202, 0.00149202, 0.00149202, 0.00149202, 0.00149202])

    names.append("LAnklePitch")
    times.append([0, 0.48, 0.96, 1.44, 1.92])
    keys.append([-0.00464392, -0.00464392, -0.00464392, -0.00464392, -0.00464392])

    names.append("LAnkleRoll")
    times.append([0, 0.48, 0.96, 1.44, 1.92])
    keys.append([-0.00609398, -0.00609398, -0.00609398, -0.00609398, -0.00609398])

    names.append("LElbowRoll")
    times.append([0, 0.48, 0.96, 1.44, 1.92])
    keys.append([-0.0398421, -0.08126, -0.168698, -0.504644, -0.489304])

    names.append("LElbowYaw")
    times.append([0, 0.48, 0.96, 1.44, 1.92])
    keys.append([-0.023052, -0.964928, -0.964928, -0.964928, -0.964928])

    names.append("LHand")
    times.append([0, 0.48, 0.96, 1.44, 1.92])
    keys.append([0.0248001, 0.0248001, 0.718, 0.718, 0.00119996])

    names.append("LHipPitch")
    times.append([0, 0.48, 0.96, 1.44, 1.92])
    keys.append([-0.00455999, -0.00455999, -0.00455999, -0.00455999, -0.00455999])

    names.append("LHipRoll")
    times.append([0, 0.48, 0.96, 1.44, 1.92])
    keys.append([0.0061779, 0.0061779, 0.0061779, 0.0061779, 0.0061779])

    names.append("LHipYawPitch")
    times.append([0, 0.48, 0.96, 1.44, 1.92])
    keys.append([0.00157595, 0.00157595, 0.00157595, 0.00157595, 0.00157595])

    names.append("LKneePitch")
    times.append([0, 0.48, 0.96, 1.44, 1.92])
    keys.append([0.00302601, 0.00302601, 0.00302601, 0.00302601, 0.00302601])

    names.append("LShoulderPitch")
    times.append([0, 0.48, 0.96, 1.44, 1.92])
    keys.append([0.11194, 0.636568, 0.559868, 0.722472, 0.760822])

    names.append("LShoulderRoll")
    times.append([0, 0.48, 0.96, 1.44, 1.92])
    keys.append([-0.0061779, -0.144238, -0.104354, -0.308376, -0.26389])

    names.append("LWristYaw")
    times.append([0, 0.48, 0.96, 1.44, 1.92])
    keys.append([0.0214341, -0.303774, -0.326784, -0.0583339, -0.0383921])

    names.append("RAnklePitch")
    times.append([0, 0.48, 0.96, 1.44, 1.92])
    keys.append([-0.00149202, -0.00149202, -0.00149202, -0.00149202, -0.00149202])

    names.append("RAnkleRoll")
    times.append([0, 0.48, 0.96, 1.44, 1.92])
    keys.append([-0.00149202, -0.00149202, -0.00149202, -0.00149202, -0.00149202])

    names.append("RElbowRoll")
    times.append([0, 0.48, 0.96, 1.44, 1.92])
    keys.append([0.066004, 0.0552659, 0.070606, 0.168782, 0.168782])

    names.append("RElbowYaw")
    times.append([0, 0.48, 0.96, 1.44, 1.92])
    keys.append([0.0383081, 0.05058, 0.05058, 0.05058, 0.05058])

    names.append("RHand")
    times.append([0, 0.48, 0.96, 1.44, 1.92])
    keys.append([0.0252, 0.0252, 0.8364, 0.8364, 0.2384])

    names.append("RHipPitch")
    times.append([0, 0.48, 0.96, 1.44, 1.92])
    keys.append([-0.00464392, -0.00464392, -0.00464392, -0.00464392, -0.00464392])

    names.append("RHipRoll")
    times.append([0, 0.48, 0.96, 1.44, 1.92])
    keys.append([-0.00455999, -0.00455999, -0.00455999, -0.00455999, -0.00455999])

    names.append("RHipYawPitch")
    times.append([0, 0.48, 0.96, 1.44, 1.92])
    keys.append([0.00157595, 0.00157595, 0.00157595, 0.00157595, 0.00157595])

    names.append("RKneePitch")
    times.append([0, 0.48, 0.96, 1.44, 1.92])
    keys.append([-0.00762796, 0.00310993, 0.00310993, 0.00310993, 0.00310993])

    names.append("RShoulderPitch")
    times.append([0, 0.48, 0.96, 1.44, 1.92])
    keys.append([0.105888, -0.0429101, -0.138018, -0.0720561, -0.0429101])

    names.append("RShoulderRoll")
    times.append([0, 0.48, 0.96, 1.44, 1.92])
    keys.append([-0.021518, -0.158044, 0.053648, 0.245398, 0.25767])

    names.append("RWristYaw")
    times.append([0, 0.48, 0.96, 1.44, 1.92])
    keys.append([0.0229681, 1.65975, 1.78093, 1.76713, 1.79014])
    return names, times, keys

def getUp():
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0, 0.26, 0.52, 0.78, 1.04, 1.3, 1.56, 1.82])
    keys.append([0.28835, -0.242414, -0.262356, 0.269942, -0.517, -0.546146, -0.5937, -0.576826])

    names.append("HeadYaw")
    times.append([0, 0.26, 0.52, 0.78, 1.04, 1.3, 1.56, 1.82])
    keys.append([0.098134, -0.2102, -0.188724, 0.31903, 0.34971, 0.34971, 0.34971, -0.119694])

    names.append("LAnklePitch")
    times.append([0, 0.26, 0.52, 0.78, 1.04, 1.3, 1.56, 1.82])
    keys.append([0.0858622, -0.0552659, -0.0552659, -0.0552659, 0.38806, 0.266874, 0.164096, 0.148756])

    names.append("LAnkleRoll")
    times.append([0, 0.26, 0.52, 0.78, 1.04, 1.3, 1.56, 1.82])
    keys.append([-0.121144, -0.110406, -0.124212, -0.124212, -0.338972, -0.200912, -0.0413761, -0.0413761])

    names.append("LElbowRoll")
    times.append([0, 0.26, 0.52, 0.78, 1.04, 1.3, 1.56, 1.82])
    keys.append([-0.1733, -0.0398421, -0.0398421, -0.0349066, -0.0349066, -0.11961, -0.95564, -0.837522])

    names.append("LElbowYaw")
    times.append([0, 0.26, 0.52, 0.78, 1.04, 1.3, 1.56, 1.82])
    keys.append([-1.19043, -1.20423, -1.20423, -1.20423, -1.20423, -1.20423, -0.69341, -0.704148])

    names.append("LHand")
    times.append([0, 0.26, 0.52, 0.78, 1.04, 1.3, 1.56, 1.82])
    keys.append([0.2824, 0.2824, 0.2824, 0.2824, 0.2824, 0.2824, 0.4508, 0.4508])

    names.append("LHipPitch")
    times.append([0, 0.26, 0.52, 0.78, 1.04, 1.3, 1.56, 1.82])
    keys.append([0.24855, -0.716336, -1.333, -1.34528, -0.783832, -0.306758, -0.0383081, -0.0352399])

    names.append("LHipRoll")
    times.append([0, 0.26, 0.52, 0.78, 1.04, 1.3, 1.56, 1.82])
    keys.append([-0.055182, -0.256136, -0.37272, -0.37272, -0.251534, -0.125746, -0.136484, -0.130348])

    names.append("LHipYawPitch")
    times.append([0, 0.26, 0.52, 0.78, 1.04, 1.3, 1.56, 1.82])
    keys.append([-0.167164, -0.05058, 0.115092, 0.11049, -0.552198, -0.0843279, -0.154892, -0.16563])

    names.append("LKneePitch")
    times.append([0, 0.26, 0.52, 0.78, 1.04, 1.3, 1.56, 1.82])
    keys.append([-0.0890141, 0.0935321, 0.0935321, 0.0935321, 0.0597839, -0.0923279, -0.0923279, -0.0844119])

    names.append("LShoulderPitch")
    times.append([0, 0.26, 0.52, 0.78, 1.04, 1.3, 1.56, 1.82])
    keys.append([0.23466, 0.423342, 0.423342, 0.423342, 0.423342, 0.966378, 1.08603, 1.31306])

    names.append("LShoulderRoll")
    times.append([0, 0.26, 0.52, 0.78, 1.04, 1.3, 1.56, 1.82])
    keys.append([0.0199001, 1.30693, 1.27164, 1.26091, 1.26091, 0.141086, 0.15029, 0.10427])

    names.append("LWristYaw")
    times.append([0, 0.26, 0.52, 0.78, 1.04, 1.3, 1.56, 1.82])
    keys.append([-0.421892, -0.658128, -0.658128, -0.658128, -0.658128, -0.374338, -0.34826, -0.335988])

    names.append("RAnklePitch")
    times.append([0, 0.26, 0.52, 0.78, 1.04, 1.3, 1.56, 1.82])
    keys.append([0.0844119, -0.079726, -1.1863, -1.1863, -1.01393, -0.216252, -0.33437, -0.309826])

    names.append("RAnkleRoll")
    times.append([0, 0.26, 0.52, 0.78, 1.04, 1.3, 1.56, 1.82])
    keys.append([0.12583, 0.0153821, 0.0511902, -0.0597839, 0.114734, 0.388144, -0.0122299, 0.00771189])

    names.append("RElbowRoll")
    times.append([0, 0.26, 0.52, 0.78, 1.04, 1.3, 1.56, 1.82])
    keys.append([0.046062, 0.0644701, 0.0537319, 1.05083, 0.0644701, 0.208666, 0.717954, 0.497058])

    names.append("RElbowYaw")
    times.append([0, 0.26, 0.52, 0.78, 1.04, 1.3, 1.56, 1.82])
    keys.append([1.20568, 1.24863, 1.2379, 1.49101, 0.312894, 0.292952, 0.312894, 0.26534])

    names.append("RHand")
    times.append([0, 0.26, 0.52, 0.78, 1.04, 1.3, 1.56, 1.82])
    keys.append([0.288, 0.288, 0.288, 0.288, 0.288, 0.288, 0.288, 0.288])

    names.append("RHipPitch")
    times.append([0, 0.26, 0.52, 0.78, 1.04, 1.3, 1.56, 1.82])
    keys.append([0.259204, 0.0444441, -0.0828779, -0.09515, -0.974132, -0.966462, -0.451038, -0.34059])

    names.append("RHipRoll")
    times.append([0, 0.26, 0.52, 0.78, 1.04, 1.3, 1.56, 1.82])
    keys.append([-0.0935321, 0.265424, 0.266958, 0.3636, -0.532256, -0.782298, -0.076658, -0.0659201])

    names.append("RHipYawPitch")
    times.append([0, 0.26, 0.52, 0.78, 1.04, 1.3, 1.56, 1.82])
    keys.append([-0.167164, -0.05058, 0.115092, 0.11049, -0.552198, -0.0843279, -0.154892, -0.16563])

    names.append("RKneePitch")
    times.append([0, 0.26, 0.52, 0.78, 1.04, 1.3, 1.56, 1.82])
    keys.append([-0.0919981, 0.14884, 1.84238, 1.32388, 1.38985, 0.934248, 0.774712, 0.60137])

    names.append("RShoulderPitch")
    times.append([0, 0.26, 0.52, 0.78, 1.04, 1.3, 1.56, 1.82])
    keys.append([0.112024, -1.71037, -1.66895, -0.15796, 0.556884, 0.391212, 0.550748, 0.88516])

    names.append("RShoulderRoll")
    times.append([0, 0.26, 0.52, 0.78, 1.04, 1.3, 1.56, 1.82])
    keys.append([0.118076, 0.125746, 0.102736, -1.16588, -1.21497, 0.18864, 0.20398, 0.0597839])

    names.append("RWristYaw")
    times.append([0, 0.26, 0.52, 0.78, 1.04, 1.3, 1.56, 1.82])
    keys.append([0.45709, 1.41584, 1.39897, -0.40195, 1.63827, 0.466294, -0.181054, -0.181054])
    return names, times, keys

# Medio feitas pero la última posición está buena
def goblin():
    # Choregraphe simplified export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0, 0.36, 0.76])
    keys.append([-0.0153821, -0.00310993, 0.0459781])

    names.append("HeadYaw")
    times.append([0, 0.36, 0.76])
    keys.append([-0.019984, -0.019984, -0.019984])

    names.append("LAnklePitch")
    times.append([0, 0.36, 0.76])
    keys.append([-0.526204, -0.898966, -0.576826])

    names.append("LAnkleRoll")
    times.append([0, 0.36, 0.76])
    keys.append([0.046062, 0.0123138, 0.0383921])

    names.append("LElbowRoll")
    times.append([0, 0.36, 0.76])
    keys.append([-0.05058, -0.05058, -0.05058])

    names.append("LElbowYaw")
    times.append([0, 0.36, 0.76])
    keys.append([-0.024586, -0.024586, -0.024586])

    names.append("LHand")
    times.append([0, 0.36, 0.76])
    keys.append([0.0212001, 0.0212001, 0.0212001])

    names.append("LHipPitch")
    times.append([0, 0.36, 0.76])
    keys.append([0.0123138, 0.0123138, 0.0123138])

    names.append("LHipRoll")
    times.append([0, 0.36, 0.76])
    keys.append([-0.00455999, -0.00455999, 0.0337899])

    names.append("LHipYawPitch")
    times.append([0, 0.36, 0.76])
    keys.append([-0.0367742, -0.052114, -0.800706])

    names.append("LKneePitch")
    times.append([0, 0.36, 0.76])
    keys.append([0.343574, 0.808376, 0.819114])

    names.append("LShoulderPitch")
    times.append([0, 0.36, 0.76])
    keys.append([0.101202, 0.101202, 0.101202])

    names.append("LShoulderRoll")
    times.append([0, 0.36, 0.76])
    keys.append([0.0229681, 0.0229681, -0.00157595])

    names.append("LWristYaw")
    times.append([0, 0.36, 0.76])
    keys.append([0.0122299, 0.0122299, 0.0122299])

    names.append("RAnklePitch")
    times.append([0, 0.36, 0.76])
    keys.append([-0.42641, -0.85593, -0.42641])

    names.append("RAnkleRoll")
    times.append([0, 0.36, 0.76])
    keys.append([0.0061779, -0.056716, -0.056716])

    names.append("RElbowRoll")
    times.append([0, 0.36, 0.76])
    keys.append([0.0644701, 0.0644701, 0.0644701])

    names.append("RElbowYaw")
    times.append([0, 0.36, 0.76])
    keys.append([0.024502, 0.024502, 0.024502])

    names.append("RHand")
    times.append([0, 0.36, 0.76])
    keys.append([0.0164, 0.0164, 0.0164])

    names.append("RHipPitch")
    times.append([0, 0.36, 0.76])
    keys.append([0.0904641, -0.0598679, -0.214802])

    names.append("RHipRoll")
    times.append([0, 0.36, 0.76])
    keys.append([0.0337899, 0.105888, -0.1733])

    names.append("RHipYawPitch")
    times.append([0, 0.36, 0.76])
    keys.append([-0.0367742, -0.052114, -0.800706])

    names.append("RKneePitch")
    times.append([0, 0.36, 0.76])
    keys.append([0.20253, 0.845276, 0.845276])

    names.append("RShoulderPitch")
    times.append([0, 0.36, 0.76])
    keys.append([0.092082, 0.092082, 0.092082])

    names.append("RShoulderRoll")
    times.append([0, 0.36, 0.76])
    keys.append([-0.00464392, -0.00464392, -0.00157595])

    names.append("RWristYaw")
    times.append([0, 0.36, 0.76])
    keys.append([0.0152981, 0.0152981, 0.0152981])
    return names, times, keys
