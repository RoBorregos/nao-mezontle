def arms_up():
	names = list()
	times = list()
	keys = list()

	times_v = [0.0, 0.2, 0.4, 0.6, 0.8]

	names.append("RShoulderRoll")
	times.append(times_v)
	keys.append([-0.4, -0.4, -0.4, 0.31 ,-0.4])

	names.append("LShoulderRoll")
	times.append(times_v)
	keys.append([0.4, 0.4, -0.31, 0.4, 0.4])

	names.append("RShoulderPitch")
	times.append(times_v)
	keys.append([0.7, 0.7, 0.7, -1.5, 0.7])

	names.append("LShoulderPitch")
	times.append(times_v)
	keys.append([0.7, -1.5, -1.5 ,0.7, 0.7])

	names.append("RElbowRoll")
	times.append(times_v)
	keys.append([0.8, 0.8, 0.8, 1.54, 0.8])

	names.append("LElbowRoll")
	times.append(times_v)
	keys.append([-0.8, -0.8, -1.54, -0.8, -0.8])

	names.append("RElbowYaw")
	times.append(times_v)
	keys.append([0.0, 0.0, 0.0, 1.5, 0])

	names.append("LElbowYaw")
	times.append(times_v)
	keys.append([0.0, 0.0, -1.5, 0, 0])
	return names, times, keys
