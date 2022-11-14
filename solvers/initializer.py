from enum import Enum
from math import dist
import numpy as np
import random
from typing import List
from solvers.individual import Individual
from cmath import inf
from tqdm import tqdm



class InitializationStrategy(Enum):
    RANDOM = 1
    GREEDY = 2

    @staticmethod
    def convert(text: str):
        if text.upper() == "RANDOM":
            return InitializationStrategy.RANDOM
        elif text.upper() == "GREEDY":
            return InitializationStrategy.GREEDY
        else:
            raise Exception("Unknown initialization strategy passed!")

def initialize_solution(distances: np.ndarray, strategy: InitializationStrategy, start_city=-1) -> Individual:
    order = []
    if strategy == InitializationStrategy.RANDOM:
        order = find_random_order(distances, start_city)
    elif strategy == InitializationStrategy.GREEDY:
        order = find_greedy_order(distances, start_city)

    result = Individual(order)
    result.calculate_cost(distances)
    return result

def find_greedy_order(distances: np.ndarray, start_city=-1) -> List[int]:
    assert (distances.shape[0] == distances.shape[1])
    number_of_cities = distances.shape[0]

    unvisited = np.arange(number_of_cities).tolist()
    del unvisited[0] #TODO start city
    
    route = [0]    
    current_city = 0

    while len(unvisited):
        nearest_city = -1
        min_distance = inf

        #find city with minimum distance, and remove it
        for other_city in unvisited:
            current_distance = distances[current_city, other_city]
            if current_distance < min_distance:
                min_distance = current_distance
                nearest_city = other_city
        unvisited.remove(nearest_city)
        
        route.append(nearest_city)
        current_city = nearest_city
        
    
    return route

def find_random_order(distances: np.ndarray, start_city=-1) -> List[int]:
    assert (distances.shape[0] == distances.shape[1])
    number_of_cities = distances.shape[0]

    result = np.arange(number_of_cities).tolist()
    random.shuffle(result)
    if start_city != -1:
        index = result.index(start_city)
        result[index], result[0] = result[0], result[index]

    return result