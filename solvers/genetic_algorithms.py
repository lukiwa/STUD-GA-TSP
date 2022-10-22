import numpy as np

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

def crossover(first_indivudual, second_individual):
    pass

def mutation(individual, mutation_probability):
    pass
    