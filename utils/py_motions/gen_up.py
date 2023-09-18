def gen_up():
	names = list()
	times = list()
	keys = list()

	times_v = [0, 0.2, 0.5]

	names.append('RKneePitch')
	times.append(times_v)
	keys.append([2.11, 1.56, 0.35])

	names.append('LKneePitch')
	times.append(times_v)
	keys.append([2.11, 1.56, 0.35])

	names.append('RAnklePitch')
	times.append(times_v)
	keys.append([-1.19, -0.66, 0.92])

	names.append('LAnklePitch')
	times.append(times_v)
	keys.append([-1.19, -0.66, 0.92])

	names.append('RAnkleRoll')
	times.append(times_v)
	keys.append([-0.77, -0.77, -0.77])

	names.append('LAnkleRoll')
	times.append(times_v)
	keys.append([0.77, 0.77, 0.77])

	names.append('RHipPitch')
	times.append(times_v)
	keys.append([-1.77, -0.65, -1.77])

	names.append('LHipPitch')
	times.append(times_v)
	keys.append([-1.77, -0.65, -1.77])

	names.append('RHipRoll')
	times.append(times_v)
	keys.append([-0.15, -0.15, -0.15])

	names.append('LHipRoll')
	times.append(times_v)
	keys.append([0.21, 0.21, 0.21])

	names.append('RHipYawPitch')
	times.append(times_v)
	keys.append([-0.2, -0.2, -0.2])

	names.append('LHipYawPitch')
	times.append(times_v)
	keys.append([-0.2, -0.2, -0.2])

	names.append('RShoulderRoll')
	times.append(times_v)
	keys.append([-0.1, -0.1, -0.1])

	names.append('LShoulderRoll')
	times.append(times_v)
	keys.append([0.1, 0.1, 0.1])

	names.append('RShoulderPitch')
	times.append(times_v)
	keys.append([2.09, 2.09, 2.09])

	names.append('LShoulderPitch')
	times.append(times_v)
	keys.append([2.09, 2.09, 2.09])

	names.append('RElbowRoll')
	times.append(times_v)
	keys.append([0.0, 0.0, 1.54])

	names.append('LElbowRoll')
	times.append(times_v)
	keys.append([0.0, 0.0, -1.54])

	names.append('RElbowYaw')
	times.append(times_v)
	keys.append([-2.09, -2.09, 2.09])

	names.append('LElbowYaw')
	times.append(times_v)
	keys.append([2.09, 2.09, -2.09])

	names.append('RWristYaw')
	times.append(times_v)
	keys.append([1.82, 1.82, 1.82])

	names.append('LWristYaw')
	times.append(times_v)
	keys.append([-1.82, -1.82, -1.82])

	names.append('LPhalanx1')
	times.append(times_v)
	keys.append([1, 0.5, 0])

	names.append('RPhalanx1')
	times.append(times_v)
	keys.append([1, 0.5, 0])

	names.append('LPhalanx2')
	times.append(times_v)
	keys.append([1, 0.5, 0])

	names.append('RPhalanx2')
	times.append(times_v)
	keys.append([1, 0.5, 0])

	names.append('LPhalanx3')
	times.append(times_v)
	keys.append([1, 0.5, 0])

	names.append('RPhalanx3')
	times.append(times_v)
	keys.append([1, 0.5, 0])

	names.append('LPhalanx4')
	times.append(times_v)
	keys.append([1, 0.5, 0])

	names.append('RPhalanx4')
	times.append(times_v)
	keys.append([1, 0.5, 0])

	names.append('LPhalanx5')
	times.append(times_v)
	keys.append([1, 0.5, 0])

	names.append('RPhalanx5')
	times.append(times_v)
	keys.append([1, 0.5, 0])

	names.append('LPhalanx6')
	times.append(times_v)
	keys.append([1, 0.5, 0])

	names.append('RPhalanx6')
	times.append(times_v)
	keys.append([1, 0.5, 0])

	names.append('LPhalanx7')
	times.append(times_v)
	keys.append([1, 0.5, 0])

	names.append('RPhalanx7')
	times.append(times_v)
	keys.append([1, 0.5, 0])

	names.append('LPhalanx8')
	times.append(times_v)
	keys.append([1, 0.5, 0])

	names.append('RPhalanx8')
	times.append(times_v)
	keys.append([1, 0.5, 0])

	names.append('HeadPitch')
	times.append(times_v)
	keys.append([-0.67, -0.67, 0.51])

	names.append('HeadYaw')
	times.append(times_v)
	keys.append([0.0, 0.0, 0.0])

	return names, times, keys