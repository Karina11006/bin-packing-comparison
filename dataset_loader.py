import os
from typing import List, Tuple, Dict

DATA_FOLDER: str = 'datasets'

def get_dataset_names() -> List[str] :
    return os.listdir(DATA_FOLDER)

def get_dataset_file_names(dataset_folder: str) -> List[str]:
    instance_folder: str = os.path.join(DATA_FOLDER, dataset_folder)
    return os.listdir(instance_folder)

def read_file(path: str) -> str:
    with open(path, 'r') as f:
        content: str = f.read()
    return content

def parse_data(raw_data: str) -> Tuple[List[int], int]:
    numbers = [int(x) for x in raw_data.split()]
    weights = numbers[2:]
    capacity = numbers[1]
    return weights, capacity

def load_datasets() -> Dict[str, Tuple[List[int], int]]:
    datasets: Dict[str, Tuple[List[int], int]] = dict() # key: dataset_name, value: (weights, capacity)
    dataset_names: List[str] = get_dataset_names()
    for dataset in dataset_names:
        file_names: List[str] = get_dataset_file_names(dataset)
        for file in file_names:
            path: str = os.path.join(DATA_FOLDER, dataset, file)
            content = read_file(path)
            weights, capacity = parse_data(content)
            datasets[f'{dataset}_{file}'] = (weights, capacity)
    return datasets

