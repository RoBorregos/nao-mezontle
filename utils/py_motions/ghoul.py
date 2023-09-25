
def ghoul2():
    names = list()
    times = list()
    keys = list()

    times_v = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    # Legs
    names.append("RKneePitch")
    times.append(times_v)
    keys.append([2.11, 2.11, -0.09, -0.09, 2.11, 2.11, -0.09, -0.09, 2.11, 2.11, -0.09])
    # keys.append([-0.09, 2.11, -0.09, 2.11, -0.09, 2.11, -0.09, 2.11, -0.09, 2.11, -0.09])
    
    names.append("LKneePitch")
    times.append(times_v)
    keys.append([2.11, 2.11, -0.09, -0.09, 2.11, 2.11, -0.09, -0.09, 2.11, 2.11, -0.09])
    # keys.append([-0.09, 1.5, -0.09, 1.5, -0.09, 1.5, -0.09, 1.5, -0.09, 1.5, -0.09])
    # keys.append([-0.09, 2.11, -0.09, 2.11, -0.09, 2.11, -0.09, 2.11, -0.09, 2.11, -0.09])

    names.append("LAnklePitch")
    times.append(times_v)
    keys.append([-1.18267, -1.18267, 0.92, 0.92, -1.18267, -1.18267, 0.92, 0.92, -1.18267, -1.18267, 0.92])
    # keys.append([-0.099668, -1.18267, 0.92, -1.18267, 0.92, -1.18267, 0.92, -1.18267, 0.92, -1.18267, 0.92])

    names.append("RAnklePitch")
    times.append(times_v)
    keys.append([-1.18267, -1.18267, 0.92, 0.92, -1.18267, -1.18267, 0.92, 0.92, -1.18267, -1.18267, 0.92])

    names.append("RHipPitch")
    times.append(times_v)
    keys.append([-1.77, -1.77, 0.48, 0.48, -1.77, -1.77, 0.48, 0.48, -1.77, -1.77, 0.48])

    # keys.append([0.136484, -0.636652, -0.681138, -0.636652, -0.681137, -0.636652, -0.681137, -0.636652, -0.681137, -0.636652, -0.681137])

    names.append("LHipPitch")
    times.append(times_v)
    keys.append([-1.77, -1.77, 0.48, 0.48, -1.77, -1.77, 0.48, 0.48, -1.77, -1.77, 0.48])
    # keys.append([0.090548, -0.7102, -0.765424, -0.710201, -0.765425, -0.710201, -0.765425, -0.710201, -0.765425, -0.710201, -0.765425])

    names.append("RHipRoll")
    times.append(times_v)
    keys.append([-0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2])

    names.append("LHipRoll")
    times.append(times_v)
    keys.append([0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2])

    names.append("LHipYawPitch")
    times.append(times_v)
    keys.append([-0.205514, -0.700996, -0.716336, -0.700996, -0.716335, -0.700996, -0.716335, -0.700996, -0.716335, -0.700996, -0.716335])
    
    names.append("RHipYawPitch")
    times.append(times_v)
    keys.append([-0.205514, -0.700996, -0.716336, -0.700996, -0.716335, -0.700996, -0.716335, -0.700996, -0.716335, -0.700996, -0.716335])


    # Arms
    names.append("LShoulderRoll")
    times.append(times_v)
    keys.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    # keys.append([0.0168321, -0.00157595, -0.016916, -0.00157595, -0.016916, -0.00157595, -0.016916, -0.00157595, -0.016916, -0.00157595, -0.016916])

    names.append("RShoulderRoll")
    times.append(times_v)
    keys.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    # keys.append([0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2])

    # Que tan abierto está el codo. 0 = extendido completamente
    names.append("LElbowRoll")
    times.append(times_v)
    keys.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    # keys.append([-0.529188, -1.04615, -1.017, -1.04615, -1.017, -1.04615, -1.017, -1.04615, -1.017, -1.04615, -1.017])

    names.append("RElbowRoll")
    times.append(times_v)
    keys.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    # keys.append([0.30991, 1.02322, 1.00021, 1.02322, 1.00021, 1.02322, 1.00021, 1.02322, 1.00021, 1.02322, 1.00021])
    
    # Giro de codo
    names.append("LElbowYaw")
    times.append(times_v)
    keys.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    # keys.append([-1.16588, -1.43587, -1.43587, -1.43587, -1.43587, -1.43587, -1.43587, -1.43587, -1.43587, -1.43587, -1.43587])

    names.append("RElbowYaw")
    times.append(times_v)
    keys.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

    # keys.append([1.27011, 1.57384, 1.57384, 1.57384, 1.57384, 1.57384, 1.57384, 1.57384, 1.57384, 1.57384, 1.57384])

    names.append("HeadPitch")
    times.append(times_v)
    keys.append([-0.411154, 0.502679, 0.502679, 0.502679, 0.502679, 0.502679, 0.502679, 0.502679, 0.502679, 0.502679, 0.502679])

    names.append("HeadYaw")
    times.append(times_v)
    keys.append([0.176368, 0.0674541, 0.0674541, 0.0674542, 0.0674542, 0.0674542, 0.0674542, 0.0674542, 0.0674542, 0.0674542, 0.0674542])
    
    names.append("LAnkleRoll")
    times.append(times_v)
    keys.append([-0.0352399, -0.0500216, -0.0475121, -0.0500217, -0.0475121, -0.0500217, -0.0475121, -0.0500217, -0.0475121, -0.0500217, -0.0475121])

    names.append("LShoulderPitch")
    times.append(times_v)
    # keys.append([0.0, 0.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0])
    keys.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    # keys.append([0.253068, 0.644238, 0.654976, 0.644238, 0.654977, 0.644238, 0.654977, 0.644238, 0.654977, 0.644238, 0.654977])

    names.append("RShoulderPitch")
    times.append(times_v)
    keys.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    # keys.append([0.158044, 0.636652, 0.67807, 0.636652, 0.678071, 0.636652, 0.678071, 0.636652, 0.678071, 0.636652, 0.678071])


    names.append("LWristYaw")
    times.append(times_v)
    keys.append([-0.352862, 0.314428, 0.314428, 0.314428, 0.314428, 0.314428, 0.314428, 0.314428, 0.314428, 0.314428, 0.314428])

    names.append("RAnkleRoll")
    times.append(times_v)
    keys.append([0.181054, 0.0511902, 0.0519691, 0.0511902, 0.0519691, 0.0511902, 0.0519691, 0.0511902, 0.0519691, 0.0511902, 0.0519691])

    names.append("RWristYaw")
    times.append(times_v)
    keys.append([0.291418, -0.0644701, -0.04146, -0.06447, -0.0414601, -0.06447, -0.0414601, -0.06447, -0.0414601, -0.06447, -0.0414601])

    # Fingers

    # LPhalanx1 - 8 RPhalanx1 - 8

    names.append("LPhalanx1")
    times.append(times_v)
    keys.append([0.0, 0.0, 1, 1, 0.0, 0.0, 0.0, 0.0, 1, 1, 0.0])

    names.append("RPhalanx1")
    times.append(times_v)
    keys.append([0.0, 0.0, 1, 1, 0.0, 0.0, 0.0, 0.0, 1, 1, 0.0])

    names.append("LPhalanx2")
    times.append(times_v)
    keys.append([0.0, 0.0, 1, 1, 0.0, 0.0, 0.0, 0.0, 1, 1, 0.0])

    names.append("RPhalanx2")
    times.append(times_v)
    keys.append([0.0, 0.0, 1, 1, 0.0, 0.0, 0.0, 0.0, 1, 1, 0.0])

    names.append("LPhalanx3")
    times.append(times_v)
    keys.append([0.0, 0.0, 1, 1, 0.0, 0.0, 0.0, 0.0, 1, 1, 0.0])

    names.append("RPhalanx3")
    times.append(times_v)
    keys.append([0.0, 0.0, 1, 1, 0.0, 0.0, 0.0, 0.0, 1, 1, 0.0])
    
    names.append("LPhalanx4")
    times.append(times_v)
    keys.append([0.0, 0.0, 1, 1, 0.0, 0.0, 0.0, 0.0, 1, 1, 0.0])

    names.append("RPhalanx4")
    times.append(times_v)
    keys.append([0.0, 0.0, 1, 1, 0.0, 0.0, 0.0, 0.0, 1, 1, 0.0])

    names.append("LPhalanx5")
    times.append(times_v)
    keys.append([0.0, 0.0, 1, 1, 0.0, 0.0, 0.0, 0.0, 1, 1, 0.0])

    names.append("RPhalanx5")
    times.append(times_v)
    keys.append([0.0, 0.0, 1, 1, 0.0, 0.0, 0.0, 0.0, 1, 1, 0.0])

    names.append("LPhalanx6")
    times.append(times_v)
    keys.append([0.0, 0.0, 1, 1, 0.0, 0.0, 0.0, 0.0, 1, 1, 0.0])

    names.append("RPhalanx6")
    times.append(times_v)
    keys.append([0.0, 0.0, 1, 1, 0.0, 0.0, 0.0, 0.0, 1, 1, 0.0])
    
    names.append("LPhalanx7")
    times.append(times_v)
    keys.append([0.0, 0.0, 1, 1, 0.0, 0.0, 0.0, 0.0, 1, 1, 0.0])

    names.append("RPhalanx7")
    times.append(times_v)
    keys.append([0.0, 0.0, 1, 1, 0.0, 0.0, 0.0, 0.0, 1, 1, 0.0])

    names.append("LPhalanx8")
    times.append(times_v)
    keys.append([0.0, 0.0, 1, 1, 0.0, 0.0, 0.0, 0.0, 1, 1, 0.0])

    names.append("RPhalanx8")
    times.append(times_v)
    keys.append([0.0, 0.0, 1, 1, 0.0, 0.0, 0.0, 0.0, 1, 1, 0.0])
    

    return names, times, keys
