from math import dist
from loader import load_locations_from_file, calculate_distances_matrix
from solvers import initialize_solution, InitializationStrategy, Individual
from configparser import ConfigParser

def main():
    configur = ConfigParser()
    configur.read("config.ini")
    init_strategy =  InitializationStrategy.convert(configur.get("ea", "init_strategy"))
    start_city = configur.getint("ea", "start_city")
    pop_size = configur.getint("ea", "pop_size")
    data_set = configur.get("ea", "data_set")

    locations = load_locations_from_file(f"test_data/TSP/{data_set}")
    distances = calculate_distances_matrix(locations)

    population = []
    for _ in range(pop_size):
        order, cost = initialize_solution(distances=distances, strategy=init_strategy, start_city=start_city)
        population.append(Individual(order, cost))

if __name__ == "__main__":
    main()
