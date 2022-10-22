from enum import Enum
import numpy as np
import random
from typing import List


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


def initialize_solution(distances: np.ndarray, strategy: InitializationStrategy, start_city=-1):
    order = []
    cost = 0
    if strategy == InitializationStrategy.RANDOM:
        order = find_random_order(distances, start_city)
        cost = calculate_total_cost(order, distances)
    elif strategy == InitializationStrategy.GREEDY:
        raise Exception("Greedy initialization strategy not implemented yet!")

    return order, cost


def find_random_order(distances: np.ndarray, start_city=-1) -> List[int]:
    assert (distances.shape[0] == distances.shape[1])
    number_of_cities = distances.shape[0]

    result = []
    if start_city != -1:
        result.append(start_city)

    # one city might already be in the list
    for _ in range(number_of_cities - len(result)):
        result.append(random.choice(
            [x for x in range(number_of_cities) if x not in result]))

    return result


def calculate_total_cost(order: List[int], distances: np.ndarray):
    cost = 0
    for city_index in range(1, len(order)):
        previous = order[city_index - 1]
        current = order[city_index]
        cost += distances[previous, current]
    
    cost += distances[order[0], order[-1]]
    return cost
