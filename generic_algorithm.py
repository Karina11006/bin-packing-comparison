import random
from typing import List, Dict

# Parametry problemu
bin_capacity: int = 10
items: List[int] = [4, 8, 1, 4, 2, 1, 10, 3, 5, 6, 2, 7, 5, 4, 3, 6, 4, 2, 6, 7, 2]

# Parametry algorytmu genetycznego
POP_SIZE: int = 100
GENERATIONS: int = 5000
MUTATION_RATE: float = 0.1
TOURNAMENT_SIZE: int = 5


# Tworzenie losowego osobnika (chromosomu)
def create_individual() -> List[int]:
    return [random.randint(0, len(items) - 1) for _ in range(len(items))]


# Obliczanie liczby pudełek potrzebnych do spakowania zgodnie z chromosomem
def fitness(ind: List[int]) -> int:
    bins: Dict[int, List[int]] = {}
    for item_index, bin_index in enumerate(ind):
        bins.setdefault(bin_index, []).append(items[item_index])
    valid_bins: List[List[int]] = [b for b in bins.values() if sum(b) <= bin_capacity]
    penalty: int = sum(1 for b in bins.values() if sum(b) > bin_capacity)
    return len(valid_bins) + penalty * 10  # kara za przekroczenie pojemności


# Selekcja turniejowa
def tournament_selection(pop: List[List[int]]) -> List[int]:
    selected: List[List[int]] = random.sample(pop, TOURNAMENT_SIZE)
    return min(selected, key=fitness)


# Krzyżowanie jednopunktowe
def crossover(parent1: List[int], parent2: List[int]) -> List[int]:
    point: int = random.randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:]


# Mutacja - zmiana indeksu pudełka dla jednego elementu
def mutate(ind: List[int]) -> List[int]:
    if random.random() < MUTATION_RATE:
        idx: int = random.randint(0, len(ind) - 1)
        ind[idx] = random.randint(0, len(items) - 1)
    return ind


# Inicjalizacja populacji
population: List[List[int]] = [create_individual() for _ in range(POP_SIZE)]

# Główna pętla algorytmu genetycznego
for gen in range(GENERATIONS):
    new_population: List[List[int]] = []
    for _ in range(POP_SIZE):
        parent1: List[int] = tournament_selection(population)
        parent2: List[int] = tournament_selection(population)
        child: List[int] = crossover(parent1, parent2)
        child = mutate(child)
        new_population.append(child)
    population = new_population
    best: List[int] = min(population, key=fitness)
    print(f"Generacja {gen}: najlepszy wynik = {fitness(best)}")

# Wynik
best_solution: List[int] = min(population, key=fitness)
print("\nNajlepsze rozmieszczenie:")
final_bins: Dict[int, List[int]] = {}
for item_index, bin_index in enumerate(best_solution):
    final_bins.setdefault(bin_index, []).append(items[item_index])
for i, b in enumerate(final_bins.values()):
    print(f"Pudełko {i+1}: {b}, suma = {sum(b)}")
