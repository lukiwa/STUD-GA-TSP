from io import TextIOWrapper
from lib2to3.pgen2 import token
from re import L
import numpy as np
from .location import Location

def calculate_data_beginning(lines):
    data_begin = 1
    for line in lines:
        s = line.split()[0]
        if not s.startswith("NODE_COORD_SECTION"):
            data_begin += 1
        else:
            break
    return data_begin


def load_locations_from_file(filename: str):
    locations = []
    with open(filename) as file:
        lines = file.readlines()
        data_begin = calculate_data_beginning(lines)

        for line_index in range(data_begin, len(lines)):
            if not lines[line_index].startswith("EOF") and len(lines[line_index]) > 1:
                tokens = lines[line_index].split()
                locations.append(Location(float(tokens[1]), float(tokens[2])))
    return locations
