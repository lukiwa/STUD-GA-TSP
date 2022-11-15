from cmath import inf
from dis import dis
from math import dist
from timeit import timeit
from tkinter.tix import Select
from loader import load_locations_from_file, calculate_distances_matrix
from solvers import initialize_solution, InitializationStrategy, Individual
from configparser import ConfigParser
from functools import partial
import random
import time
from solvers import initialize_population, evaluate, selection, crossover, mutation
from solvers.genetic_algorithms import CrossoverStrategy, MutationStrategy, SelectionStrategy
from tqdm import tqdm
import pandas as pd

import csv
import locale

start_time = time.time()

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
    selection_strategy = SelectionStrategy.convert(configur.get("ea", "selection_strategy"))

    locations = load_locations_from_file(f"test_data/TSP/{data_set}.tsp")
    distances = calculate_distances_matrix(locations)

    populations = [initialize_population(pop_size, partial(initialize_solution, distances, init_strategy, start_city))]
    best_solution = Individual([], inf)

    for current_population_index in tqdm(range(max_generations), desc="Performing genetic algorithm..."):
        populations.append([])
        while len(populations[current_population_index + 1]) < pop_size:
            P1 = selection(populations[current_population_index], selection_strategy, tour_size)
            P2 = selection(populations[current_population_index], selection_strategy, tour_size)
            O1 = crossover(P1, P2, crossover_strategy, crossover_probability, distances)
            O1 = mutation(O1, mutation_strategy, mutation_probability, distances)
            # evaluate(O1) #TODO
            populations[current_population_index + 1].append(O1)
            if O1.cost < best_solution.cost:
                best_solution = O1

    end_time = time.time()
    finish_time= end_time-start_time
    print(f"Best solution: {best_solution.cost}")
    print(f"Strategy: {crossover_strategy}")

    print(f"data_set:  {data_set}")
    print(f"max generations:  {max_generations}")
    print(f"start_city:  {start_city}")
    print(f"time:  {finish_time}")

    # csvPath = "plik.csv"
    # with open(csvPath) as csv_file:
    #     csv_reader = csv.reader(csv_file, delimiter=',')
    #     # totalRecord =len(list(csv_reader1))
    #     line_count = 0
    #     for row in csv_reader:
    #         if line_count == 0:
    #             print(f'Column names: {", ".join(row)}')
    #             line_count += 1
    #
    #         else:
    #             if row:
    #                 print(f'\t{row[0]}, {row[1]},  {row[2]}, {row[3]}.')
    #                 line_count += 1
    #     print(f'Processed {line_count} lines.')


    with open("berkin52_cross.csv", 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([f"{data_set}" , f"{best_solution.cost}", f"{max_generations}", f"{crossover_strategy}", f"{finish_time}"])


    filecsv = pd.read_csv('berkin52_cross.csv')
    print("Number of lines present:",len(filecsv))

    sorted_filecsv = filecsv.sort_values(by=["Best solution"], ascending=False)
    sorted_filecsv.to_csv('berkin52_cross.csv', index=False)




if __name__ == "__main__":
    main()
