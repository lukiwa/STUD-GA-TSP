from enum import Enum
import numpy as np
import random
from typing import List


class InitializationStrategy(Enum):
    RANDOM = 1
    GREEDY = 2


def initialize_solution(distances: np.ndarray, strategy: InitializationStrategy, start_city: int):
    order = []
    cost = 0
    if strategy == InitializationStrategy.RANDOM:
        order = find_random_order(distances, start_city)
        cost = calculate_total_cost(order, distances)
    elif strategy == InitializationStrategy.GREEDY:
        raise Exception("Greedy initialization strategy not implemented yet!")

    return order, cost


def find_random_order(distances: np.ndarray, start_city: int) -> List[int]:
    assert (distances.shape[0] == distances.shape[1])
    number_of_cities = distances.shape[0]
    result = [start_city]

    # one city already in list
    for _ in range(number_of_cities - 1):
        result.append(random.choice(
            [x for x in range(number_of_cities) if x not in result]))

    return result


def calculate_total_cost(order: List[int], distances: np.ndarray):
    cost = 0
    for city_index in range(1, len(order)):
        previous = order[city_index - 1]
        current = order[city_index]
        cost += distances[previous, current]
    return cost
