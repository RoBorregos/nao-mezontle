"""
File to transform .motion files to "nao format" (format given by choregraphe), which can be also used to
create motions in webots using nao_to_webots.
"""

import os

def convert_motion_file(input_file):
    names = []
    times = []
    keys = []

    with open(input_file, 'r') as file:
        lines = file.readlines()
        header = lines[0].strip().split(',')
        joint_names = header[2:]
        times_v = []
        current_time = 0.0

        for line in lines[1:]:
            data = line.strip().split(',')
            time_str = data[0]
            pose_name = data[1]
            joint_values = [float(val) for val in data[2:]]

            # Calculate time in seconds
            time_parts = time_str.split(':')
            seconds = float(time_parts[0]) * 60 + float(time_parts[1]) + int(time_parts[2]) / 1000.0
            times_v.append(current_time)
            current_time = seconds

            for i, joint_name in enumerate(joint_names):
                if len(names) <= i:
                    names.append(joint_name)
                    keys.append([joint_values[i]])
                    times.append([current_time])
                else:
                    keys[i].append(joint_values[i])
                    times[i].append(current_time)

    return names, times, keys


if __name__ == '__main__':
    # Run the script to generate the motion file
    # print(os.getcwd())
    # input_file = "./controllers/motions/ArmsUp.motion"
    input_file = "./controllers/motions/FastForward.motion"
    name = "ArmsUp"
    names, times, keys = convert_motion_file(input_file)

    
    all_text = f"def {name}():\n"
    all_text += "\tnames = list()\n"
    all_text += "\ttimes = list()\n"
    all_text += "\tkeys = list()\n\n"

    text_str = ""
    for time in times[0]:
        text_str += f"{time}, "

    all_text += f"\ttimes_v = [{text_str[:-2]}]\n\n"

    # Print the generated lists
    for i in range(len(names)):
        all_text += f"\tnames.append(\"{names[i]}\")\n"
        all_text += f"\times.append(times_v)\n"
        all_text += f"\tkeys.append(\"{keys[i]}\")\n\n"

    print(all_text)
