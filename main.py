from cmath import inf
from dis import dis
from math import dist
from loader import load_locations_from_file, calculate_distances_matrix
from solvers import initialize_solution, InitializationStrategy, Individual
from configparser import ConfigParser
from functools import partial
import random
from solvers import initialize_population, evaluate, selection, crossover, mutation
from solvers.genetic_algorithms import CrossoverStrategy, MutationStrategy
from tqdm import tqdm

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
    tour_size = configur.getfloat("ea", "tour_size")

    locations = load_locations_from_file(f"test_data/TSP/{data_set}.tsp")
    distances = calculate_distances_matrix(locations)

    populations = [initialize_population(pop_size, partial(initialize_solution, distances, init_strategy, start_city))]
    best_solution = Individual([], inf)

    for current_population_index in tqdm(range(max_generations), desc="Performing genetic algorithm..."):
        populations.append([])
        while len(populations[current_population_index + 1]) < pop_size:
            P1 = selection(populations[current_population_index], tour_size)
            P2 = selection(populations[current_population_index], tour_size)
            O1 = crossover(P1, P2, crossover_strategy, crossover_probability, distances)
            O1 = mutation(O1, mutation_strategy, mutation_probability, distances)
            #evaluate(O1) #TODO
            populations[current_population_index + 1].append(O1)
            if best_solution.cost > O1.cost:
                best_solution = O1

    print(f"Best solution: {best_solution.cost}")


if __name__ == "__main__":
    main()
