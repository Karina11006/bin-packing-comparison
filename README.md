# Bin Packing Comparison

## Project Summary
This repository focuses on solving the Bin Packing Problem using three heuristic methods and a genetic algorithm. The goal is to implement and compare different strategies to optimize item placement into bins of fixed capacity in order to minimize the number of bins used.

## Implemented Algorithms

### Heuristic Methods
- **First Fit**: Places each item into the first bin that has enough remaining capacity.
- **Next Fit**: Places an item into the current open bin. If it doesn't fit, a new bin is opened.
- **Best Fit**: Places each item into the bin that will leave the least remaining space after the item is placed.

These heuristics are implemented in the `heuristics.py` file.

### Genetic Algorithm
A population-based metaheuristic inspired by natural selection. The algorithm evolves solutions over generations by applying selection, crossover, and mutation operators. Its implementation is found in the `genetic_algorithm.py` file.

## Data
The datasets used in this project were downloaded from the [Bin Packing Problem Library (BPPLib)](https://site.unibo.it/operations-research/en/research/bpplib-a-bin-packing-problem-library). The `dataset_loader.py` file contains the implementation for reading and parsing these datasets.

## Results
Results from algorithm runs and their analysis are stored in the `results/` directory. 

## Main Script
The `main.py` file is the entry point for executing and comparing the different algorithms on selected datasets.

## Contributors
- **Mariusz Dyrla** (<dyrla@student.agh.edu.pl>)
- **Folwarski Konrad** (<konfolw@student.agh.edu.pl>)
- **Kita Karol** (<kkita970@gmail.com>)
- **Krotkiewicz Karina** (<karina.krotkiewicz@gmail.com>)

