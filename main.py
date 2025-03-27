from heuristics import nextfit, first_fit, best_fit
from genetic_algorithm import run_genetic_algorithm
import time
from typing import List
from dataset_loader import load_datasets

# Parametry algorytmu genetycznego
POP_SIZE: List[int] = [100]
GENERATIONS: List[int] = [500]
MUTATION_RATE: List[float] = [0.1]
TOURNAMENT_SIZE: List[int] = [5]

params = [
    (100, 500, 0.1, 5)   # (pop_size, generation, mutation_rate, tournament_size)
]

datasets = load_datasets()

methods = {
    'Next_fit': nextfit,
    'First_fit': first_fit,
    'Best_fit': best_fit,
    # 'Genetic_Algorithm': run_genetic_algorithm
}

header = f"DATASET_NAME;METHOD_NAME;BIN_NUMBER;BIN_CAPACITY;N;ELAPSED_TIME_MS;POP_SIZE;GENERATIONS;MUTATION_RATE;TOURNAMENT_SIZE\n"
with open('genetic_algorithm_output.csv', 'w') as file:
    file.write(header)

header = f"DATASET_NAME;METHOD_NAME;BIN_NUMBER;BIN_CAPACITY;N;ELAPSED_TIME_MS\n"
with open('heuristics_output.csv', 'w') as file:
    file.write(header)

for dataset_name, dataset in datasets.items():
    print(f'{dataset_name = }')
    weights, capacity, n = dataset
    for method_name, method in methods.items():
        print(f'{method_name = }')

        if method_name == 'Genetic_Algorithm':
            for param in params:
                size, generation, mutation, tournament = param
                start_time = time.perf_counter()
                method_output = method(bin_capacity=capacity, items=weights, pop_size=size, generations=generation,
                                       mutation_rate=mutation, tourament_size=tournament)

                result_value = method_output["packages count"]  #liczba paczek
                elapsed_time = (time.perf_counter() - start_time) * 1000  # ms
                output = (f"{dataset_name};{method_name};{result_value};{capacity};{n};{elapsed_time:.2f};"
                          f"{size};{generation};{mutation};{tournament}\n")
                print(f'{param = }')
                with open('genetic_algorithm_output.csv', 'a') as file:
                    file.write(output)
        else:
            start_time = time.perf_counter()
            result_value = method(weights, capacity)
            elapsed_time = (time.perf_counter() - start_time) * 1000  # ms
            output = f"{dataset_name};{method_name};{result_value};{capacity};{n};{elapsed_time:.5f}\n"
            with open('heuristics_output.csv', 'a') as file:
                file.write(output)
print('Finished')

