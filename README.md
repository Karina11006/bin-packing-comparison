# Bin Packing Comparison

This repository focuses on solving the Bin Packing Problem using three heuristic methods and a genetic algorithm. The goal is to implement and compare different strategies to optimize item placement into bins of fixed capacity in order to minimize the number of bins used.

## Implemented Algorithms

###  Heuristic Methods
- **First Fit**: Places each item into the first bin that has enough remaining capacity.
- **Next Fit**: Places an item into the current open bin. If it doesn't fit, a new bin is opened.
- **Best Fit**: Places each item into the bin that will leave the least remaining space after the item is placed.

These heuristics are implemented in the `heuristics.py` file.

###  Genetic Algorithm
A population-based metaheuristic inspired by natural selection. The algorithm evolves solutions over generations by applying selection, crossover, and mutation operators. Its implementation is found in the `genetic_algorithm.py` file.

##   Datasets
The datasets used in this project were downloaded from the [Bin Packing Problem Library (BPPLib)](https://site.unibo.it/operations-research/en/research/bpplib-a-bin-packing-problem-library). The `dataset_loader.py` file contains the implementation for reading and parsing these datasets.

## 📊  Results Overview
Results from algorithm runs and their analysis are stored in the `results/` directory. The following plots present selected results from the analysis.

### Average number of bins used
![obraz](https://github.com/user-attachments/assets/6f40a6fe-b1e6-470a-b83d-1c281205f03c)

![obraz](https://github.com/user-attachments/assets/c09fb793-a277-4194-aa38-77418415f122)

###  Gap to best known solution [%]

![obraz](https://github.com/user-attachments/assets/ffeb55c5-4820-4da8-9be1-9741d9308f34)

![obraz](https://github.com/user-attachments/assets/6e8a88fb-9583-441f-8c82-058c8cb8de6b)

### Average number of bins used by number of items to pack for each capacity (Scholl_1)
![obraz](https://github.com/user-attachments/assets/1a969286-041b-400e-82d7-ccbf3dbd3809)

## 👥 Contributors
- **Dyrla Mariusz** (<dyrla@student.agh.edu.pl>)
- **Folwarski Konrad** (<konfolw@student.agh.edu.pl>)
- **Kita Karol** (<kkita970@gmail.com>)
- **Krotkiewicz Karina** (<karina.krotkiewicz@gmail.com>)

