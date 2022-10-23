from cmath import inf, log
from typing import List
import numpy as np

class Individual:
    def __init__(self, order: List[int], cost=0):
        self.order = order
        self.cost = cost
    
    def calculate_cost(self, distances: np.ndarray):
        self.distances = distances
        self.cost = 0
        for city_index in range(1, len(self.order)):
            previous = self.order[city_index - 1]
            current = self.order[city_index]
            self.cost += distances[previous, current]
        self.cost += distances[self.order[0], self.order[-1]]
        self.calculate_fitness()

    def calculate_fitness(self):
        #TODO Suboptimal
        self.fitness = 1 - (1 / self.cost)
        return self.fitness
    
    def __repr__(self):
        return f"Order:{self.order}_Cost:{self.cost}"
