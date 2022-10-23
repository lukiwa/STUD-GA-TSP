import imp
import numpy as np
import random
from .individual import Individual
from collections import Counter

def initialize_population(pop_size: int, individual_generator):
    population = []
    for _ in range(pop_size):
        population.append(individual_generator())
    return population

#TODO
def evaluate(individual):
    pass

def selection(population):
    pass

def crossover(first_indivudual: Individual, second_individual: Individual) -> Individual:
    size = len(first_indivudual.order)
    start, end = sorted([random.randrange(size) for _ in range(2)])
    child_order = [None] * size

    for i in range(start, end + 1):
        child_order[i] = first_indivudual.order[i]
    
    order_from_second = [x for x in second_individual.order if x not in child_order]

    for i in range(len(order_from_second)):
        free_index = child_order.index(None)
        child_order[free_index] = order_from_second[i]

    #Assert every city excatly once
    assert(np.unique(child_order).size == len(child_order))


    return Individual(child_order, 0)

def mutation(individual, mutation_probability):
    pass
    