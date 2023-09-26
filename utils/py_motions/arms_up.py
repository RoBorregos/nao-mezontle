def arms_up():
	names = list()
	times = list()
	keys = list()

	times_v = [0.0, 0.05, 0.1, 0.15, 0.2]

	names.append("RShoulderRoll")
	times.append(times_v)
	keys.append([-0.4, -0.4, 0.0, 0.0, -0.4])

	names.append("LShoulderRoll")
	times.append(times_v)
	keys.append([0.4, 0.4, 0.0, 0.0, 0.4])

	names.append("RShoulderPitch")
	times.append(times_v)
	keys.append([0.7, 0.7, 0.0, 0.0, 0.7])

	names.append("LShoulderPitch")
	times.append(times_v)
	keys.append([0.7, 0.7, 0.0, 0.0, 0.7])

	names.append("RElbowRoll")
	times.append(times_v)
	keys.append([0.8, 0.8, 0.0, 0.0, 0.8])

	names.append("LElbowRoll")
	times.append(times_v)
	keys.append([-0.8, -0.8, 0.0, 0.0, -0.8])

	names.append("RElbowYaw")
	times.append(times_v)
	keys.append([0.0, 0.0, 0.0, 0.0, 0.0])

	names.append("LElbowYaw")
	times.append(times_v)
	keys.append([0.0, 0.0, 0.0, 0.0, 0.0])

	names.append("RWristYaw")
	times.append(times_v)
	keys.append([0.0, 0.0, 1.8, 1.8, 0.0])

	names.append("LWristYaw")
	times.append(times_v)
	keys.append([0.0, 0.0, 1.8, 1.8, 0.0])

	names.append("LPhalanx1")
	times.append(times_v)
	keys.append([0.0, 1, 1, 1, 0.0])
	
	names.append("RPhalanx1")
	times.append(times_v)
	keys.append([0.0, 1, 1, 1, 0.0])

	names.append("LPhalanx2")
	times.append(times_v)
	keys.append([0.0, 1, 1, 1, 0.0])

	names.append("RPhalanx2")
	times.append(times_v)
	keys.append([0.0, 1, 1, 1, 0.0])

	names.append("LPhalanx3")
	times.append(times_v)
	keys.append([0.0, 1, 1, 1, 0.0])

	names.append("RPhalanx3")
	times.append(times_v)
	keys.append([0.0, 1, 1, 1, 0.0])
    
	names.append("LPhalanx4")
	times.append(times_v)
	keys.append([0.0, 1, 1, 1, 0.0])

	names.append("RPhalanx4")
	times.append(times_v)
	keys.append([0.0, 1, 1, 1, 0.0])

	names.append("LPhalanx5")
	times.append(times_v)
	keys.append([0.0, 1, 1, 1, 0.0])

	names.append("RPhalanx5")
	times.append(times_v)
	keys.append([0.0, 1, 1, 1, 0.0])

	names.append("LPhalanx6")
	times.append(times_v)
	keys.append([0.0, 1, 1, 1, 0.0])

	names.append("RPhalanx6")
	times.append(times_v)
	keys.append([0.0, 1, 1, 1, 0.0])
    
	names.append("LPhalanx7")
	times.append(times_v)
	keys.append([0.0, 1, 1, 1, 0.0])

	names.append("RPhalanx7")
	times.append(times_v)
	keys.append([0.0, 1, 1, 1, 0.0])

	names.append("LPhalanx8")
	times.append(times_v)
	keys.append([0.0, 1, 1, 1, 0.0])

	names.append("RPhalanx8")
	times.append(times_v)
	keys.append([0.0, 1, 1, 1, 0.0])

	return names, times, keys