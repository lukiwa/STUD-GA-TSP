from math import dist
from loader import load_locations_from_file, calculate_distances_matrix
from solvers import initialize_solution, InitializationStrategy, Individual
from configparser import ConfigParser
from functools import partial
import random
from solvers import initialize_population, evaluate, selection, crossover, mutation
from solvers.genetic_algorithms import CrossoverStrategy, MutationStrategy


def main():
    configur = ConfigParser()
    configur.read("config.ini")
    init_strategy = InitializationStrategy.convert(configur.get("ea", "init_strategy"))
    start_city = configur.getint("ea", "start_city")
    pop_size = configur.getint("ea", "pop_size")
    data_set = configur.get("ea", "data_set")
    max_generations = configur.getint("ea", "max_generations")
    crossover_probability = configur.getfloat("ea", "crossover_probability")
    mutation_probability = configur.getfloat("ea", "mutation_probability")
    crossover_strategy = CrossoverStrategy.convert(configur.get("ea", "crossover_strategy"))
    mutation_strategy = MutationStrategy.convert(configur.get("ea", "mutation_strategy"))

    locations = load_locations_from_file(f"test_data/TSP/{data_set}")
    distances = calculate_distances_matrix(locations)

    populations = initialize_population(pop_size, partial(initialize_solution, distances, init_strategy, start_city))
    current_population = 0
    #best_solution = Individual([], 0)

    P1 = Individual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0)
    P2 = Individual([0, 5, 7, 4, 9, 1, 3, 6, 2, 8], 0)

    #child = crossover(P1, P2, crossover_strategy, crossover_probability)
    child = mutation(P1, mutation_strategy, mutation_probability)
    print(child.order)
    '''
    while current_population_index < max_generations:
        populations.append([])
        while len(populations[current_population_index + 1]) < pop_size:ś
            P1 = selection(populations[current_population_index])
            P2 = selection(populations[current_population_index])
            O1 = crossover(P1, P2, crossover_strategy, crossover_probability)
            O1 = mutation(O1, mutation_strategy, mutation_probability)
            evaluate(O1)
            populations[current_population_index + 1].append(O1)
            #if best_solution > O1:
            #    best_solution = O1
        current_population_index += 1
    '''

if __name__ == "__main__":
    main()
