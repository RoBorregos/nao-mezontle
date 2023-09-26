# https://github.com/dorkamotorka/RoboCup-project/blob/main/scripts/nao_to_webots_motion_converter.py
# Script to convert Naoqi motion files to Webots motion files

import csv
import os
from py_motions import movements
from py_motions import arms_up
from py_motions import ghoulUp
from py_motions import gen_up
from py_motions import back_fast3
# NOTE: You need to import the wanted file e.g. pick_up.py

def convert_time_array(arr):
    out = []
    pose = 1
    for el in arr:
        webots_time = convert_time_to_webots_time(el, pose)
        out.append(webots_time)
        pose += 1

    return out


def convert_time_to_webots_time(time, pose):
    tmp = (time % 1)
    milisec = tmp * 1000
    sec = time - tmp

    return '00:' + ("%02d" % (sec,)) + ':' + ("%03d" % (milisec,)) + ',' + ('Pose%d' % pose)

all_names, all_times, all_keys = arms_up.arms_up() # NOTE: Python function should be called here!

first_row = ['#WEBOTS_MOTION','V1.0'] + all_names

if __name__ == "__main__":
    path = "./nao-mezontle/controllers/motions"
    motion = os.path.join(path, "ArmsUp.motion") # Write file directly to motions directory
    time_set = set()
    with open(motion, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(first_row)

        # Get all times
        for times in all_times:
            for time in times:
                time_set.add(time)

        time_array = sorted(time_set)
        time_array_webots = convert_time_array(time_array)

        for name,times,keys in zip(all_names,all_times,all_keys):
            indexes = []
            for time,key in zip(times,keys):
                index = time_array.index(time)
                indexes.append(index)
                time_array_webots[index] += (',' + str(key))

            time_array_webots = [(x + ',*') if (i not in indexes) else time_array_webots[i] for i,x in enumerate(time_array_webots) ] 
            print(time_array_webots)
                   
        out_csv = []
        for row in time_array_webots:
            out = row.split(',')
            out_csv.append(out)
                
        writer.writerows(out_csv)
                

"""
def replace_string(text, to_replace, replacement):
    # Use the replace method to replace 'to_replace' with 'replacement'
    updated_text = text.replace(to_replace, replacement)
    return updated_text

    t = "keys.append([-0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3])"
    replace_string(t, r, n)

n = "times.append([0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1, 2.4, 2.7, 3.0])"
r = "times.append([0, 0.16, 0.24, 0.32, 0.4, 0.48, 0.56, 0.64, 0.72, 0.8, 0.88])"

"""