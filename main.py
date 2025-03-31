from heuristics import nextfit, first_fit, best_fit
from genetic_algorithm import run_genetic_algorithm
from dataset_loader import load_datasets

import time
from tqdm import tqdm


methods = {
    'Next_fit': nextfit,
    'First_fit': first_fit,
    'Best_fit': best_fit,
    'Genetic_Algorithm': run_genetic_algorithm
}

params = [
    (10, 5, 0.1, 5)   # (pop_size, generation, mutation_rate, tournament_size)
]

# output files
header = f"DATASET_NAME;METHOD_NAME;BIN_NUMBER;BIN_CAPACITY;N;ELAPSED_TIME_MS;POP_SIZE;GENERATIONS;MUTATION_RATE;TOURNAMENT_SIZE\n"
with open('genetic_algorithm_output.csv', 'w') as file:
    file.write(header)

header = f"DATASET_NAME;METHOD_NAME;BIN_NUMBER;BIN_CAPACITY;N;ELAPSED_TIME_MS\n"
with open('heuristics_output.csv', 'w') as file:
    file.write(header)

print("Loading datasets ...", end=' ')
datasets = load_datasets()
print(f"Loaded {len(datasets)} datasets.")

print('Starting bin packing comparison ...')
pbar = tqdm(datasets.items(), desc="Datasets", unit="file", total=len(datasets))
for dataset_name, dataset in pbar:
    weights, capacity, n = dataset
    for method_name, method in methods.items():
        if method_name == 'Genetic_Algorithm':
            for param in params:
                size, generation, mutation, tournament = param
                pbar.set_description(f"{dataset_name[:30]} | {method_name} {param}")

                start_time = time.perf_counter()
                method_output = method(bin_capacity=capacity, items=weights,
                                       pop_size=size, generations=generation,
                                       mutation_rate=mutation, tourament_size=tournament)
                result_value = method_output["packages count"]
                elapsed_time = (time.perf_counter() - start_time) * 1000
                output = (f"{dataset_name};{method_name};{result_value};{capacity};{n};{elapsed_time:.2f};"
                          f"{size};{generation};{mutation};{tournament}\n")
                with open('genetic_algorithm_output.csv', 'a') as file:
                    file.write(output)
        else:
            pbar.set_description(f"{dataset_name[:30]} | {method_name}")

            start_time = time.perf_counter()
            result_value = method(weights, capacity)
            elapsed_time = (time.perf_counter() - start_time) * 1000
            output = f"{dataset_name};{method_name};{result_value};{capacity};{n};{elapsed_time:.5f}\n"
            with open('heuristics_output.csv', 'a') as file:
                file.write(output)

print('Finished')
