from heuristics import nextfit, first_fit, best_fit
import time



weight1 = [4, 8, 1, 4, 2, 1, 10, 3, 5, 6, 2, 7, 5, 4, 3, 6, 4, 2, 6, 7, 2]
c1 = 10

datasets = {
    'Dataset_1': (weight1, c1)
}
methods = {
    'Next_fit': nextfit,
    'First_fit': first_fit,
    'Best_fit': best_fit
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

