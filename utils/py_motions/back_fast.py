def back_fast():
	names = list()
	times = list()
	keys = list()

	times_v = [0.0, 0.3, 0.4, 0.8, 1.199, 1.8, 2.1, 2.2]

	names.append("RKneePitch")
	times.append(times_v)
	keys.append([-0.0, 0.4202, 0.4202, 0.5, 2.11, 2.11, 2.11, 1.9])

	names.append("LKneePitch")
	times.append(times_v)
	keys.append([0.0, 0.4202, 0.4202, 0.5, 2.11, 2.11, 2.11, 1.9])

	names.append("RAnklePitch")
	times.append(times_v)
	keys.append([0.0, 0.0, 0.0, -1.2361, -1.0186, -1.0186, -1.0186, -0.7])

	names.append("LAnklePitch")
	times.append(times_v)
	keys.append([0.0, 0.0, 0.0, -1.2361, -1.0189, -1.0189, -1.0189, -0.7])

	names.append("RAnkleRoll")
	times.append(times_v)
	keys.append([-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0])

	names.append("LAnkleRoll")
	times.append(times_v)
	keys.append([-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0])

	names.append("RHipPitch")
	times.append(times_v)
	keys.append([0.0293, -1.77, -1.77, 0.48, 0.48, -0.2, -0.2, 0.0])

	names.append("LHipPitch")
	times.append(times_v)
	keys.append([0.0156, -1.77, -1.77, 0.48, 0.48, -0.2, -0.2, 0.0])

	names.append("RHipRoll")
	times.append(times_v)
	keys.append([-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0])

	names.append("LHipRoll")
	times.append(times_v)
	keys.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

	names.append("RHipYawPitch")
	times.append(times_v)
	keys.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

	names.append("LHipYawPitch")
	times.append(times_v)
	keys.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

	names.append("RShoulderRoll")
	times.append(times_v)
	keys.append([-0.5, -0.5, -0.1, -0.1, -0.1, -0.1, -0.0, 0.0])

	names.append("LShoulderRoll")
	times.append(times_v)
	keys.append([0.5, 0.5, 0.1, 0.1, 0.1, 0.1, -0.0, 0.0])

	names.append("RShoulderPitch")
	times.append(times_v)
	keys.append([-2.0, 1.5962, 1.5962, 1.9524, 2.0762, 2.0762, 2.0762, 2.0762])

	names.append("LShoulderPitch")
	times.append(times_v)
	keys.append([-2.0, 1.5954, 1.5954, 1.9519, 2.0762, 2.0762, 2.0762, 2.0762])

	names.append("RElbowRoll")
	times.append(times_v)
	keys.append([0.0, 0.9282, 0.9282, 1.3476, 1.3133, 0.5, 0.5, 0.0])

	names.append("LElbowRoll")
	times.append(times_v)
	keys.append([-0.0, -0.9282, -0.9282, -1.3476, -1.3133, -0.5, -0.5, 0.0])

	names.append("RElbowYaw")
	times.append(times_v)
	keys.append([0.0, -1.1657, -1.1657, -1.1657, -1.1432, -1.1432, -1.1432, 2.0])

	names.append("LElbowYaw")
	times.append(times_v)
	keys.append([-0.0, 1.1657, 1.1657, 1.1657, 1.1432, 1.1432, 1.1432, -2.0])

	names.append("RWristYaw")
	times.append(times_v)
	keys.append([-0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0])

	names.append("LWristYaw")
	times.append(times_v)
	keys.append([-0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

	names.append("RPhalanx1")
	times.append(times_v)
	keys.append([-0.0, -0.0, -0.0, 0.0, 0.0, 0.0, 1.0, 1.0])

	names.append("LPhalanx1")
	times.append(times_v)
	keys.append([-0.0, -0.0, -0.0, 0.0, 0.0, 0.0, 1.0, 1.0])

	names.append("RPhalanx2")
	times.append(times_v)
	keys.append([-0.0, -0.0, -0.0, 0.0, 0.0, 0.0, 1.0, 1.0])

	names.append("LPhalanx2")
	times.append(times_v)
	keys.append([-0.0, -0.0, -0.0, 0.0, 0.0, 0.0, 1.0, 1.0])

	names.append("RPhalanx3")
	times.append(times_v)
	keys.append([-0.0, 0.0, 0.0, 0.0, -0.0, -0.0, 1.0, 1.0])

	names.append("LPhalanx3")
	times.append(times_v)
	keys.append([-0.0, -0.0, -0.0, 0.0, 0.0, 0.0, 1.0, 1.0])

	names.append("RPhalanx4")
	times.append(times_v)
	keys.append([-0.0, -0.0, -0.0, 0.0, 0.0, 0.0, 1.0, 0.0])

	names.append("LPhalanx4")
	times.append(times_v)
	keys.append([-0.0, -0.0, -0.0, 0.0, 0.0, 0.0, 1.0, 0.0])

	names.append("RPhalanx5")
	times.append(times_v)
	keys.append([-0.0, -0.0, -0.0, 0.0, 0.0, 0.0, 1.0, 1.0])

	names.append("LPhalanx5")
	times.append(times_v)
	keys.append([-0.0, -0.0, -0.0, 0.0, 0.0, 0.0, 1.0, 1.0])

	names.append("RPhalanx6")
	times.append(times_v)
	keys.append([-0.0, -0.0, -0.0, 0.0, 0.0, 0.0, 1.0, 1.0])

	names.append("LPhalanx6")
	times.append(times_v)
	keys.append([-0.0, -0.0, -0.0, 0.0, 0.0, 0.0, 1.0, 1.0])

	names.append("RPhalanx7")
	times.append(times_v)
	keys.append([-0.0, -0.0, -0.0, 0.0, 0.0, 0.0, 1.0, 1.0])

	names.append("LPhalanx7")
	times.append(times_v)
	keys.append([-0.0, -0.0, -0.0, 0.0, 0.0, 0.0, 1.0, 1.0])

	names.append("RPhalanx8")
	times.append(times_v)
	keys.append([-0.0, -0.0, -0.0, 0.0, 0.0, 0.0, 1.0, 1.0])

	names.append("LPhalanx8")
	times.append(times_v)
	keys.append([-0.0, -0.0, -0.0, 0.0, 0.0, 0.0, 1.0, 1.0])

	names.append("HeadPitch")
	times.append(times_v)
	keys.append([-0.0, -0.54, -0.54, -0.54, -0.54, -0.54, 0.51, 0.51])

	names.append("HeadYaw")
	times.append(times_v)
	keys.append([-0.0, -0.0, -0.0, -0.0, 0.0, 0.0, 0.0, 0.0])


	return names, times, keys

