from heuristics import nextfit, first_fit, best_fit
import time
import generic_algorithm as ga
import generic_algorithm2 as ga2



weight1 = [4, 8, 1, 4, 2, 1, 10, 3, 5, 6, 2, 7, 5, 4, 3, 6, 4, 2, 6, 7, 2]
c1 = 10

ga_params = {
    'generations': 5000,
    'population': 100,
    'selected': 10,
    'mutation_rate': 0.1,
    'cross_rate': 0.9
}

datasets = {
    'Dataset_1': (weight1, c1)
}
methods = {
    'Next_fit': nextfit,
    'First_fit': first_fit,
    'Best_fit': best_fit,
    'Genetic_algorithm2': ga2.genetic_algorithm2(weight1, c1, ga_params)
}




for dataset_name, dataset in datasets.items():
    weights = dataset[0]
    bin_with_capacity = dataset[1]
    for method_name, method in methods.items():
        start_time = time.perf_counter()
        method_output = method(weights, bin_with_capacity)
        # elapsed time ms
        elapsed_time = (time.perf_counter() - start_time) * 1000
        output = f"{dataset_name};{method_name};{method_output};{elapsed_time}\n"
        with open('output.csv', 'a') as file:
            file.write(output)
        print(output)

