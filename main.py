from math import dist
from loader import load_locations_from_file, calculate_distances_matrix
from solvers import initialize_solution, InitializationStrategy, Individual


def main():
    locations = load_locations_from_file("test_data/TSP/berlin11_modified.tsp")
    distances = calculate_distances_matrix(locations)

    population = []
    for i in range(100):
        order, cost = initialize_solution(distances=distances, strategy=InitializationStrategy.RANDOM, start_city=0)
        population.append(Individual(order, cost))


if __name__ == "__main__":
    main()
