import random
from typing import List, Dict, Any


# Creation of a random individual (chromosome)
def create_individual(items: List[int]) -> List[int]:
    return [random.randint(0, len(items) - 1) for _ in range(len(items))]


# Calculating the number of bins needed to pack according to the chromosome
def fitness(ind: List[int], items: List[int], bin_capacity: int) -> int:
    bins: Dict[int, List[int]] = {}
    for item_index, bin_index in enumerate(ind):
        bins.setdefault(bin_index, []).append(items[item_index])
    valid_bins: List[List[int]] = [b for b in bins.values() if sum(b) <= bin_capacity]
    penalty: int = sum(1 for b in bins.values() if sum(b) > bin_capacity)
    return len(valid_bins) + penalty * 10  # kara za przekroczenie pojemności


# Tournament selection
def tournament_selection(pop: List[List[int]], tourament_size: int, items: List[int], bin_capacity: int) -> List[int]:
    selected: List[List[int]] = random.sample(pop, tourament_size)
    return min(selected, key=lambda ind: fitness(ind, items, bin_capacity))


# Single-point crossing
def crossover(parent1: List[int], parent2: List[int]) -> List[int]:
    point: int = random.randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:]


# Mutation - changing bin index for one element
def mutate(ind: List[int], mutation_rate: float, items: List[int]) -> List[int]:
    if random.random() < mutation_rate:
        idx: int = random.randint(0, len(ind) - 1)
        ind[idx] = random.randint(0, len(items) - 1)
    return ind


def run_genetic_algorithm(
    bin_capacity: int,
    items: List[int],
    pop_size: int,
    generations: int,
    mutation_rate: float,
    tourament_size: int
) -> Dict[str, Any]:

    # Population initialization
    population: List[List[int]] = [create_individual(items) for _ in range(pop_size)]

    # Main loop
    for gen in range(generations):
        new_population: List[List[int]] = []
        for _ in range(pop_size):
            parent1: List[int] = tournament_selection(population, tourament_size, items, bin_capacity)
            parent2: List[int] = tournament_selection(population, tourament_size, items, bin_capacity)
            child: List[int] = crossover(parent1, parent2)
            child = mutate(child, mutation_rate, items)
            new_population.append(child)
        population = new_population

    # best solutions
    best: List[int] = min(population, key=lambda ind: fitness(ind, items, bin_capacity))

    return {
        "items": items,
        "bin capacity": bin_capacity,
        "pop size": pop_size,
        "generations": generations,
        "mutation rate": mutation_rate,
        "tourament size": tourament_size,
        "packages count": fitness(best, items, bin_capacity),
    }
