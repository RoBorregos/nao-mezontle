def generate_motion(name, times, values):
    """Helper function to generate files that can be used to tune joint positions."""
    # joints = ['LKneePitch', 'RKneePitch', 'LAnklePitch', 'RAnklePitch', 'RHipPitch', 'LHipPitch', 'RHipRoll', 'LHipRoll', 'LHipYawPitch', 'RHipYawPitch', 'LShoulderRoll', 'RShoulderRoll', 'RShoulderPitch', 'LShoulderPitch', 'LElbowRoll', 'RElbowRoll', 'LElbowYaw', 'RElbowYaw', 'LPhalanx1', 'RPhalanx1', 'LPhalanx2', 'RPhalanx2', 'LPhalanx3', 'RPhalanx3', 'LPhalanx4', 'RPhalanx4', 'LPhalanx5', 'RPhalanx5', 'LPhalanx6', 'RPhalanx6', 'LPhalanx7', 'RPhalanx7', 'LPhalanx8', 'RPhalanx8', 'HeadPitch', 'HeadYaw', 'LAnkleRoll', 'LWristYaw', 'RAnkleRoll', 'RWristYaw']

    # Map of each joint to its open and closed values
    # joint_name: [openValue, closedValue]
    joint_values = { 'RKneePitch': [-0.09, 2.11], 'LKneePitch': [-0.09, 2.11], 'RAnklePitch': [0.92, -1.19], 'LAnklePitch': [0.92, -1.19], 'RAnkleRoll': [-0.77, 0.4], 'LAnkleRoll': [0.77, -0.4], 'RHipPitch': [0.48, -1.77], 'LHipPitch': [0.48, -1.77], 'RHipRoll': [-0.74, 0.45], 'LHipRoll': [0.79, -0.38], 'RHipYawPitch': [-1.15, 0.74], 'LHipYawPitch': [-1.15, 0.74], 'RShoulderRoll': [-1.33, 0.31], 'LShoulderRoll': [1.33, -0.31], 'RShoulderPitch': [-2.09, 2.09], 'LShoulderPitch': [-2.09, 2.09], 'RElbowRoll': [0, 1.54], 'LElbowRoll': [0, -1.54], 'RElbowYaw': [-2.09, 2.09], 'LElbowYaw': [2.09, -2.09], 'RWristYaw': [-1.82, 1.82], 'LWristYaw': [1.82, -1.82], 'LPhalanx1': [1, 0], 'RPhalanx1':[1, 0], 'LPhalanx2':[1, 0], 'RPhalanx2':[1, 0], 'LPhalanx3':[1, 0], 'RPhalanx3':[1, 0], 'LPhalanx4':[1, 0], 'RPhalanx4':[1, 0], 'LPhalanx5':[1, 0], 'RPhalanx5':[1, 0], 'LPhalanx6':[1, 0], 'RPhalanx6':[1, 0], 'LPhalanx7':[1, 0], 'RPhalanx7':[1, 0], 'LPhalanx8':[1, 0], 'RPhalanx8':[1, 0], 'HeadPitch': [-0.67, 0.51], 'HeadYaw': [2.09, -2.09], } 

    # Values is a dictionary which maps names to an array of values [0, 1] that indicate how open or close is the joint
    # 0 indicates that the joint is open

    # Print the initial lines
    print("def " + name + "():")

    print("\tnames = list()")
    print("\ttimes = list()")
    print("\tkeys = list()")
    print()
    # Print the times
    times_var = "times_v"
    
    t_string = ""
    for time in times:
        t_string += str(time) + ", "
    print(f"\t{times_var} = [{t_string[:-2]}]")
    print()


    for x in joint_values:
        # Preserve order of joints given in joint_values

        print("\tnames.append('" + x + "')")
        print(f"\ttimes.append({times_var})")

        if x not in values:
            empty_keys = "["
            for _ in len(times):
                empty_keys += "0, "
            
            print(f"\tkeys.append([{empty_keys[:-2]}])")
            continue

        key_temp = ""

        
        if len(times) != len(values[x]):
            diff = len(times) - len(values[x]) 
            if (diff < 0):
                print(f"ERROR: there are more values than times for {x}")
            else:
                for _ in range(diff):
                    values[x].append(values[x][-1]) # Repeat last element until end.

        for y in values[x]:
            if (y > 1 or y < 0):
                print(f"ERROR: INVALID VALUE in values: {values[x]}")
                continue

            open, closed = joint_values[x]
            unit = (closed - open)
            key_temp += str(round(open + unit*y, 2)) + ", "

        print(f"\tkeys.append([{key_temp[:-2]}])")
        print()
    
    print("\treturn names, times, keys")
    

if __name__ == "__main__":
    # 0 indicates that the joint is open
    knees = {
        "RKneePitch": [1, 0.75, 0.2],
        "LKneePitch": [1, 0.75, 0.2],
    }

    ankles = {
        "RAnklePitch": [1, 0.75, 0],
        "LAnklePitch": [1, 0.75, 0],
        "RAnkleRoll": [0, 0, 0],
        "LAnkleRoll": [0, 0, 0],
    }

    hip = {
        "RHipPitch": [1, 0.5, 1],
        "LHipPitch": [1, 0.5, 1],
        "RHipRoll": [0.5],
        "LHipRoll": [0.5],
        "RHipYawPitch": [0.5],
        "LHipYawPitch": [0.5],
    }

    shoulders = {
        "RShoulderRoll": [0.75],
        "LShoulderRoll": [0.75],
        "RShoulderPitch": [1, 1, 1],
        "LShoulderPitch": [1, 1, 1],
    }

    arms = {
        "RElbowRoll": [0, 0, 1],
        "LElbowRoll": [0, 0, 1],
        "RElbowYaw": [0, 0, 1],
        "LElbowYaw": [0, 0, 1],
    }

    hands = {
        "RWristYaw": [1, 1, 1],
        "LWristYaw": [1, 1, 1],
        "RPhalanx1": [0, 0.5, 1],
        "LPhalanx1": [0, 0.5, 1],
        "RPhalanx2": [0, 0.5, 1],
        "LPhalanx2": [0, 0.5, 1],
        "RPhalanx3": [0, 0.5, 1],
        "LPhalanx3": [0, 0.5, 1],
        "RPhalanx4": [0, 0.5, 1],
        "LPhalanx4": [0, 0.5, 1],
        "RPhalanx5": [0, 0.5, 1],
        "LPhalanx5": [0, 0.5, 1],
        "RPhalanx6": [0, 0.5, 1],
        "LPhalanx6": [0, 0.5, 1],
        "RPhalanx7": [0, 0.5, 1],
        "LPhalanx7": [0, 0.5, 1],
        "RPhalanx8": [0, 0.5, 1],
        "LPhalanx8": [0, 0.5, 1],
    }

    head = {
        "HeadPitch": [0, 0, 1],
        "HeadYaw": [0.5],
    }

    values = { **knees, **ankles, **hip, **shoulders, **arms, **hands, **head }

    generate_motion("gen_up", [0, 0.2, 0.5], values)