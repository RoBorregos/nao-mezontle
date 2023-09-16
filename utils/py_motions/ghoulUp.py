def ghoulUp():
    names = list()
    times = list()
    keys = list()

    times_v = [0,0.3, 0.9, 1.2, 1.5]

    # Legs
    names.append("LKneePitch")
    times.append(times_v)
    keys.append([2.11, 2.11, 0.5, 0.5, 0.5])

    names.append("RKneePitch")
    times.append(times_v)
    keys.append([2.11, 2.11, 0.5, 0.5, 0.5])

    names.append("LAnklePitch")
    times.append(times_v)
    keys.append([-1.19, -1.19, 0, 0, 0])

    names.append("RAnklePitch")
    times.append(times_v)
    keys.append([-1.19, -1.19, 0, 0, 0])
    
    names.append("RHipPitch")
    times.append(times_v)
    keys.append([-1.77, -1.77, -1.77, -1.52637, -0.162646])
    
    names.append("LHipPitch")
    times.append(times_v)
    keys.append([-1.77, -1.77, -1.77, -1.52637, -0.162646])

    names.append("RHipRoll")
    times.append(times_v)
    keys.append([-0.5, -0.5, -0.5, -0.5, -0.5])

    names.append("LHipRoll")
    times.append(times_v)
    keys.append([0.5, 0.5, 0.5, 0.5, 0.5])

    names.append("LHipYawPitch")
    times.append(times_v)
    keys.append([0.2, 0.2, 0.2, 0.2, 0.2])

    names.append("RHipYawPitch")
    times.append(times_v)
    keys.append([-0.2, -0.2, -0.2, -0.2, -0.2])

    # Arms

    names.append("LShoulderRoll")
    times.append(times_v)
    keys.append([0.1, 0.1, 0.1, 0.1, 0.1])

    names.append("RShoulderRoll")
    times.append(times_v)
    keys.append([-0.1, -0.1, -0.1, -0.1, -0.1])

    names.append("RShoulderPitch")
    times.append(times_v)
    keys.append([0.0, 0.0, 2, 2, 2])

    names.append("LShoulderPitch")
    times.append(times_v)
    keys.append([0.0, 0.0, 2, 2, 2])

    names.append("LElbowRoll")
    times.append(times_v)
    keys.append([0, 0, 0, 0, 0])

    names.append("RElbowRoll")
    times.append(times_v)
    keys.append([0, 0, 0, 0, 0])

    names.append("LElbowYaw")
    times.append(times_v)
    keys.append([-1.19196, -1.19196, -1.19196, -1.19196, -1.18122])

    names.append("RElbowYaw")
    times.append(times_v)
    keys.append([1.30693, 0.688724, 0.688724, 0.688724, 0.868202])

    # Fingers
    # LPhalanx1 - 8 RPhalanx1 - 8

    names.append("LPhalanx1")
    times.append(times_v)
    keys.append([0, 1.0, 1.0, 1.0, 1.0])

    names.append("RPhalanx1")
    times.append(times_v)
    keys.append([0, 1.0, 1.0, 1.0, 1.0])

    names.append("LPhalanx2")
    times.append(times_v)
    keys.append([0, 1.0, 1.0, 1.0, 1.0])

    names.append("RPhalanx2")
    times.append(times_v)
    keys.append([0, 1.0, 1.0, 1.0, 1.0])

    names.append("LPhalanx3")
    times.append(times_v)
    keys.append([0, 1.0, 1.0, 1.0, 1.0])

    names.append("RPhalanx3")
    times.append(times_v)
    keys.append([0, 1.0, 1.0, 1.0, 1.0])
    
    names.append("LPhalanx4")
    times.append(times_v)
    keys.append([0, 1.0, 1.0, 1.0, 1.0])

    names.append("RPhalanx4")
    times.append(times_v)
    keys.append([0, 1.0, 1.0, 1.0, 1.0])

    names.append("LPhalanx5")
    times.append(times_v)
    keys.append([0, 1.0, 1.0, 1.0, 1.0])

    names.append("RPhalanx5")
    times.append(times_v)
    keys.append([0, 1.0, 1.0, 1.0, 1.0])

    names.append("LPhalanx6")
    times.append(times_v)
    keys.append([0, 1.0, 1.0, 1.0, 1.0])

    names.append("RPhalanx6")
    times.append(times_v)
    keys.append([0, 1.0, 1.0, 1.0, 1.0])
    
    names.append("LPhalanx7")
    times.append(times_v)
    keys.append([0, 1.0, 1.0, 1.0, 1.0])


    names.append("RPhalanx7")
    times.append(times_v)
    keys.append([0, 1.0, 1.0, 1.0, 1.0])

    names.append("LPhalanx8")
    times.append(times_v)
    keys.append([0, 1, 1.0, 1.0, 1.0])

    names.append("RPhalanx8")
    times.append(times_v)
    keys.append([0, 1, 1.0, 1.0, 1.0])


    # Other joints

    names.append("HeadPitch")
    times.append(times_v)
    keys.append([0.51, 0.51, -0.67, -0.67, -0.67])

    names.append("HeadYaw")
    times.append(times_v)
    keys.append([-0.024586, -0.024586, -0.024586, 0.569072, 0.550664])
    
    names.append("LAnkleRoll")
    times.append(times_v)
    keys.append([-0.130348, -0.107338, 0.04146, 0.282298, -0.164096])

    names.append("LWristYaw")
    times.append(times_v)
    keys.append([-0.675002, -0.676536, -0.687274, -0.687274, -0.297638])

    names.append("RAnkleRoll")
    times.append(times_v)
    keys.append([0.130432, 0.14117, 0.0598679, -0.575208, -0.0935321])

    names.append("RWristYaw")
    times.append(times_v)
    keys.append([0.306758, 0.217786, 0.217786, 0.20398, 0.54913])


    return names, times, keys

n, t, k = ghoulUp()
print(n)
print(t)
print(k)