from heuristics import nextfit, first_fit, best_fit
from generic_algorithm import run_generic_algorithm
import time


weight1 = [4, 8, 1, 4, 2, 1, 10, 3, 5, 6, 2, 7, 5, 4, 3, 6, 4, 2, 6, 7, 2]
c1 = 10

# Parametry algorytmu genetycznego
POP_SIZE: int = 100
GENERATIONS: int = 500
MUTATION_RATE: float = 0.1
TOURNAMENT_SIZE: int = 5

datasets = {
    'Dataset_1': (weight1, c1, POP_SIZE, GENERATIONS, MUTATION_RATE, TOURNAMENT_SIZE)
}
methods = {
    'Next_fit': nextfit,
    'First_fit': first_fit,
    'Best_fit': best_fit,
    'Genetic_Algorithm': run_generic_algorithm
}

for dataset_name, dataset in datasets.items():
    for method_name, method in methods.items():
        start_time = time.perf_counter()

        if method_name == 'Genetic_Algorithm':
            method_output = method(
                bin_capacity=dataset[1],
                items=dataset[0],
                pop_size=dataset[2],
                generations=dataset[3],
                mutation_rate=dataset[4],
                tourament_size=dataset[5]
            )
            result_value = method_output["packages count"]  # ekstrakt liczby paczek
        else:
            # Dla heurystyk (nextfit, first_fit, best_fit)
            result_value = method(dataset[0], dataset[1])

        elapsed_time = (time.perf_counter() - start_time) * 1000  # ms

        if method_name == 'Genetic_Algorithm':
            output = (f"{dataset_name};{method_name};{result_value};{elapsed_time:.2f}ms;"
                      f"{dataset[2]};{dataset[3]};{dataset[4]};{dataset[5]}\n")
        else:
            output = f"{dataset_name};{method_name};{result_value};{elapsed_time:.5f}ms\n"

        with open('output.csv', 'a') as file:
            file.write(output)

        print(output)
