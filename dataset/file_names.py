import os
from itertools import combinations

base_dir = "/dataset/threedmatch/FCGF_data/housecat_6d"

item_types = ["shoe", "teapot", "cutlery"]
path = "C:/master/robot-vision-modul/obj_models/obj_models_small_size_final/"
names = {}
pairs = []
for item in item_types:
    names[item] = {}
    directory_path = path + item + "/"
    for filename in os.listdir(directory_path):
        if filename.endswith(".obj"):
            obj_name = filename.split(".")[0]
            names[item][obj_name] = []
            names[item][obj_name].append(obj_name)
            for i in range(0, 9):
                names[item][obj_name].append(obj_name + "00" + str(i))
                pairs.append([obj_name, obj_name + "00" + str(i)])

# Example usage:
print(pairs)


def write_pairs_to_file(pairs, filename):
    with open(filename, 'w') as f:
        for pair in pairs:
            line = ' '.join(pair) + '\n'
            f.write(line)


write_pairs_to_file(pairs, "pairs.txt")
