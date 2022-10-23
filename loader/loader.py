from io import TextIOWrapper
from lib2to3.pgen2 import token
from re import L
import numpy as np
from .location import Location
from typing import List
from tqdm import tqdm

# Calculate where actual data starts, based on given magic word indicating begining
def calculate_data_beginning(lines: List[str], magic_word: str) -> int:
    data_begin = 1
    for line in lines:
        s = line.split()[0]
        if not s.startswith(magic_word):
            data_begin += 1
        else:
            break
    return data_begin

# Load cities locations from file
def load_locations_from_file(filename: str, data_begining_magic_word="NODE_COORD_SECTION") -> List[Location]:
    locations = []
    with open(filename) as file:
        lines = file.readlines()
        data_begin = calculate_data_beginning(lines, data_begining_magic_word)

        for line_index in tqdm(range(data_begin, len(lines)), desc="Loading cities..."):
            if not lines[line_index].startswith("EOF") and len(lines[line_index]) > 1:
                tokens = lines[line_index].split()
                locations.append(Location(float(tokens[1]), float(tokens[2])))
    return locations

# calculate distance between each location and put in matrix
def calculate_distances_matrix(locations: List[Location]) -> np.ndarray:
    distances = np.zeros((len(locations), len(locations)), float)
    for base_location in tqdm(range(0, len(locations)), desc="Calculating distances...", leave=True):
        for other_location in tqdm(range(0, len(locations)), leave=False):
            distances[base_location, other_location] = locations[base_location].calculate_distance(
                locations[other_location])
    return distances
