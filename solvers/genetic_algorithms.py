from cmath import inf
import imp
import numpy as np
import random
from .individual import Individual
from collections import Counter
from enum import Enum

class CrossoverStrategy(Enum):
    OX = 1
    ERX = 2

    @staticmethod
    def convert(text: str):
        if text.upper() == "OX":
            return CrossoverStrategy.OX
        elif text.upper() == "ERX":
            return CrossoverStrategy.ERX
        else:
            raise Exception("Unknown crossover strategy passed!")

def initialize_population(pop_size: int, individual_generator):
    population = []
    for _ in range(pop_size):
        population.append(individual_generator())
    return population

def random_selector(first, second):
    if random.uniform(0, 1) > 0.5:
        return first
    else:
        return second

def remove_from_neightbour_list(element, neightbour_list):
    # neightbour_list.pop(element)
    for _, values in neightbour_list.items():
        try:
            values.remove(element)
        except KeyError:
            pass

def evaluate(individual):
    pass

def selection(population):
    pass

def ordered_crossover(first_indivudual: Individual, second_individual: Individual) -> Individual:
    size = len(first_indivudual.order)
    start, end = sorted([random.randrange(size) for _ in range(2)])
    child_order = [None] * size

    for i in range(start, end + 1):
        child_order[i] = first_indivudual.order[i]

    order_from_second = [x for x in second_individual.order if x not in child_order]

    for i in range(len(order_from_second)):
        free_index = child_order.index(None)
        child_order[free_index] = order_from_second[i]

    return Individual(child_order, 0)


def edge_recombination_crossover(first_indivudual: Individual, second_individual: Individual) -> Individual:
    child_order = []
    size = len(first_indivudual.order)
    neightbour_list = {}
    for i in range(size):
        neightbour_list[i] = set()

    # fill neightbour list
    for node in range(size):
        neightbour_list[node].add(first_indivudual.order[node - 1])
        neightbour_list[node].add(first_indivudual.order[(node + 1) % size])
        neightbour_list[node].add(second_individual.order[node - 1])
        neightbour_list[node].add(second_individual.order[(node + 1) % size])

    X = random_selector(first_indivudual, second_individual).order[0]
    while len(child_order) < size:
        child_order.append(X)
        remove_from_neightbour_list(X, neightbour_list)
        if len(neightbour_list[X]) == 0:
            try:
                X = random.choice([x for x in range(size) if x not in child_order])
            except IndexError:
                #all lists are empty, time to end
                pass
        else:
            fewest_neightbour = inf
            for neightbour in neightbour_list[X]:
                if len(neightbour_list[neightbour]) < fewest_neightbour:
                    fewest_neightbour = neightbour
                elif len(neightbour_list[neightbour]) == fewest_neightbour:
                    fewest_neightbour = random_selector(neightbour, fewest_neightbour)
            X = fewest_neightbour

    return Individual(child_order, 0)


def crossover(first_indivudual: Individual, second_individual: Individual, crossover_strategy: CrossoverStrategy) -> Individual:
    result = Individual([])
    if crossover_strategy == CrossoverStrategy.OX:
        result = ordered_crossover(first_indivudual, second_individual)
    if crossover_strategy == CrossoverStrategy.ERX:
        result = edge_recombination_crossover(first_indivudual, second_individual)
    
    # Assert every city excatly once
    assert (np.unique(result.order).size == len(result.order))
    # Assert every city is present
    assert (all(x in result.order for x in first_indivudual.order) and all(x in result.order for x in second_individual.order))
    return result


def mutation(individual, mutation_probability):
    pass
