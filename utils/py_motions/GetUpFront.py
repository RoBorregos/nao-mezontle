def GetUpFront():
    names = list()
    times = list()
    keys = list()

    times_v = [0.0, 0.2, 0.48, 0.52, 1.0, 1.04, 1.48, 1.52, 2.0, 2.04, 2.68, 2.7199999999999998, 3.2, 3.24, 3.44, 4.24]

    names.append("LHipYawPitch")
    times.append(times_v)
    keys.append([0.0, 0.0, 0.0, 0.0, 0.0, -1.14, -1.14, -1.14, -1.14, -0.6, -0.6, -0.2, -0.2, 0.0, 0.0, 0.0])

    names.append("LHipRoll")
    times.append(times_v)
    keys.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.37, -0.37, -0.37, -0.37, 0.6, 0.6, 0.0, 0.0, 0.0])

    names.append("LHipPitch")
    times.append(times_v)
    keys.append([0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.76, -1.76, -1.76, -1.76, -0.524, -0.524, -0.524])

    names.append("LKneePitch")
    times.append(times_v)
    keys.append([0, 2.11, 2.11, 2.11, 2.11, 2.11, 2.11, 2.11, 2.11, 1.4, 1.4, 1.4, 1.4, 1.047, 1.047, 1.047])

    names.append("LAnklePitch")
    times.append(times_v)
    keys.append([0.8, -1.18, -1.18, -1.18, -1.18, -1.18, -1.18, -1.18, -1.18, 0.1, 0.1, 0.0, 0.0, -0.524, -0.524, -0.524])

    names.append("LAnkleRoll")
    times.append(times_v)
    keys.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.397, -0.397, 0.0, 0.0, 0.0])

    names.append("RHipYawPitch")
    times.append(times_v)
    keys.append([0.0, 0.0, 0.0, 0.0, 0.0, -1.14, -1.14, -1.14, -1.14, -1.14, -1.14, -0.5, -0.5, 0.0, 0.0, 0.0])

    names.append("RHipRoll")
    times.append(times_v)
    keys.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.37, 0.37, 0.37, 0.37, -0.3, -0.3, 0.0, 0.0, 0.0])

    names.append("RHipPitch")
    times.append(times_v)
    keys.append([0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.7, -1.7, -1.7, -1.7, -0.524, -0.524, -0.524])

    names.append("RKneePitch")
    times.append(times_v)
    keys.append([0, 2.11, 2.11, 2.11, 2.11, 2.11, 2.11, 2.11, 2.11, 2.11, 2.11, 2.11, 2.11, 1.047, 1.047, 1.047])

    names.append("RAnklePitch")
    times.append(times_v)
    keys.append([0.8, -1.18, -1.18, -1.18, -1.18, -1.18, -1.18, -1.18, -1.18, -0.5, 0.0, -0.5, -0.5, -0.524, -0.524, -0.524])

    names.append("RAnkleRoll")
    times.append(times_v)
    keys.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.0, 0.397, 0.397, 0.0, 0.0, 0.0])

    names.append("LShoulderRoll")
    times.append(times_v)
    keys.append([1.32, 1.32, 1.32, 0.5, 0.5, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

    names.append("LShoulderPitch")
    times.append(times_v)
    keys.append([-1.57, -1.57, -1.57, -1.57, -1.57, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0])

    names.append("LElbowRoll")
    times.append(times_v)
    keys.append([0.0, 0.0, 0.0, 0.0, 0.0, -1.54, -1.54, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

    names.append("RShoulderRoll")
    times.append(times_v)
    keys.append([-1.32, -1.32, -1.32, -0.5, -0.5, -0.5, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

    names.append("RShoulderPitch")
    times.append(times_v)
    keys.append([-1.57, -1.57, -1.57, -1.57, -1.57, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

    names.append("RElbowRoll")
    times.append(times_v)
    keys.append([0.0, 0.0, 0.0, 0.0, 0.0, 1.54, 1.54, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])


    return names, times, keys