from enum import Enum
from math import dist
import numpy as np
import random
from typing import List
from solvers.individual import Individual


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
        raise Exception("Greedy initialization strategy not implemented yet!")

    result = Individual(order)
    result.calculate_cost(distances)
    return result


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