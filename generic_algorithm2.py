import time
import random
import copy
import operator
import itertools
from collections import namedtuple
from typing import List

import numpy
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl


class run_ga:
    def __init__(self, itemList, binCapacity):
        self.itemList = itemList
        self.binCapacity = binCapacity
        self.population = []

    def set_params(self, populationSize, crossoverP, mutationP, fitnessParam, selectedParents,
                   nbIterations, nbmutationP, cutLength, selectionBestP):
        self.populationSize = populationSize
        self.crossoverP = crossoverP
        self.mutationP = mutationP
        self.fitnessParam = fitnessParam
        self.selectedParents = selectedParents
        self.nbIterations = nbIterations
        self.nbmutationP = nbmutationP
        self.cutLength = cutLength
        self.selectionBestP = selectionBestP
        self.alwaysMutate = False
        self.selection = self.roulette
        self.newGenerationSelection = "bestFitness"

    def generateInitialiPopulation(self):
        for _ in range(self.populationSize):
            self.population.append(self.firstFit())

    def firstFit(self):
        bins = [[]]
        itemListShuffled = self.itemList.copy()
        random.shuffle(itemListShuffled)
        for item in itemListShuffled:
            for b in bins:
                if sum(b) + item <= self.binCapacity:
                    b.append(item)
                    break
            else:
                bins.append([item])
        return bins

    def fitness(self, individual):
        if self.fitnessParam == 0:
            return 1 / len(individual)

        elif self.fitnessParam == 1:
            return sum((sum(b)/self.binCapacity) for b in individual) / len(individual)

        elif self.fitnessParam == 2:
            return sum((sum(b)/self.binCapacity) ** 2 for b in individual) / len(individual)

        elif self.fitnessParam == 99:
            fullness = sum(sum(b)/self.binCapacity for b in individual) / len(individual)
            bin_penalty = len(individual)
            return fullness / bin_penalty

        else:
            return sum((sum(b)/self.binCapacity) ** self.fitnessParam for b in individual) / len(individual)


    def selectParents(self):
        fitnessList = {i: self.fitness(self.population[i]) for i in range(len(self.population))}
        tmp = sorted(fitnessList.items(), key=operator.itemgetter(1), reverse=True)[:self.selectedParents]
        return [self.population[i[0]] for i in tmp]

    def roulette(self):
        fitnessList = [self.fitness(p) for p in self.population]
        fitnessSum = sum(fitnessList)
        probs = [f / fitnessSum for f in fitnessList]
        indices = list(range(len(self.population)))
        chosen_indices = numpy.random.choice(indices, size=self.selectedParents, replace=False, p=probs)
        return [self.population[i] for i in chosen_indices]


    def generateBabies(self, parent, toInsertBins):
        tmp = copy.deepcopy(toInsertBins)
        i = 0
        while i < len(parent):
            if any(item in b for item in parent[i] for b in tmp):
                for item in parent[i]:
                    for b in tmp:
                        if item in b:
                            b.remove(item)
                parent.pop(i)
            else:
                i += 1
        parent += toInsertBins
        notInserted = self.itemList.copy()
        for b in parent:
            for item in b:
                if item in notInserted:
                    notInserted.remove(item)
        return parent, notInserted

    def replacement(self, baby, notInserted):
        for step in [3, 2]:
            for b in baby:
                b.sort()
            i = 0
            while i < len(notInserted):
                replaced = False
                for b in baby:
                    j = 0
                    while j + step <= len(b):
                        if sum(b[j:j + step]) <= notInserted[i] and sum(b) - sum(b[j:j + step]) + notInserted[i] <= self.binCapacity:
                            for _ in range(step):
                                notInserted.append(b.pop(j))
                            b.append(notInserted.pop(i))
                            replaced = True
                            break
                        j += 1
                    if replaced:
                        break
                if not replaced:
                    i += 1
        return baby, notInserted

    def grow(self, baby, notInserted):
        notInserted.sort()
        for item in notInserted:
            for b in baby:
                if sum(b) + item <= self.binCapacity:
                    b.append(item)
                    break
            else:
                baby.append([item])
        return baby

    def crossOver(self, p1, p2):
        if random.random() < self.crossoverP and len(p1) > self.cutLength and len(p2) > self.cutLength:
            cut_indices1 = sorted(random.sample(range(len(p1)), self.cutLength), reverse=True)
            cut_indices2 = sorted(random.sample(range(len(p2)), self.cutLength), reverse=True)

            tmp1 = [p1.pop(i) for i in cut_indices1]
            tmp2 = [p2.pop(i) for i in cut_indices2]

            c1, notInserted1 = self.generateBabies(p1, tmp2)
            c2, notInserted2 = self.generateBabies(p2, tmp1)
            c1, notInserted1 = self.replacement(c1, notInserted1)
            c2, notInserted2 = self.replacement(c2, notInserted2)
            return self.grow(c1, notInserted1), self.grow(c2, notInserted2)
        return p1, p2

    def mutation(self, child):
        if random.random() < self.mutationP and len(child) > 1:
            twin = copy.deepcopy(child)
            nbmutation = random.randint(1, int(len(child) * self.nbmutationP))
            notInserted = []
            for _ in range(nbmutation):
                binDeleted = random.randint(0, len(child) - 1)
                notInserted += child.pop(binDeleted)
            child, notInserted = self.replacement(child, notInserted)
            child = self.grow(child, notInserted)
            return child if self.alwaysMutate or self.fitness(child) > self.fitness(twin) else twin
        return child

    def generateChildren(self, parents):
        children = []
        random.shuffle(parents)

        while len(parents) >= 2:
            p1 = parents.pop()
            p2 = parents.pop()
            c1, c2 = self.crossOver(copy.deepcopy(p1), copy.deepcopy(p2))
            children.append(self.mutation(c1))
            children.append(self.mutation(c2))

        return children


    def solution(self, children):
        return sorted(children, key=lambda v: len(v))[0]

    def populationCream(self, population):
        fitnessList = {i: self.fitness(population[i]) for i in range(len(population))}
        top = sorted(fitnessList.items(), key=operator.itemgetter(1), reverse=True)
        keep = top[:int(self.populationSize * self.selectionBestP)]
        rest = top[-(self.populationSize - len(keep)):]
        return [population[i[0]] for i in keep + rest]

    def run(self):
        self.generateInitialiPopulation()
        best = self.solution(self.population)
        for _ in range(self.nbIterations):
            parents = self.selection()
            children = self.generateChildren(parents)
            self.population = self.populationCream(children + self.population)
            if len(self.solution(self.population)) < len(best):
                best = copy.deepcopy(self.solution(self.population))
        return best

def genetic_algorithm2(items, bin_capacity, ga_params):
    import time
    import pandas as pd
    import itertools
    from collections import namedtuple

    fixed_params = {
        "populationSize": ga_params["population"],
        "selectedParents": ga_params["selected"],
        "nbIterations": ga_params["generations"],
        "mutationP": ga_params["mutation_rate"],
        "crossoverP": ga_params["cross_rate"]
    }

    search_grid = {
        "fitnessParam": [0, 1, 2, 99],
        "nbmutationP": [0.3, 0.7],
        "cutLength": [1, 2],
        "selectionBestP": [0.3, 0.5, 0.9],
    }

    ParamSet = namedtuple("ParamSet", search_grid.keys())
    results = []

    for values in itertools.product(*search_grid.values()):
        params = ParamSet(*values)

        ga = run_ga(items, bin_capacity)
        ga.set_params(
            populationSize=fixed_params["populationSize"],
            crossoverP=fixed_params["crossoverP"],
            mutationP=fixed_params["mutationP"],
            fitnessParam=params.fitnessParam,
            selectedParents=fixed_params["selectedParents"],
            nbIterations=fixed_params["nbIterations"],
            nbmutationP=params.nbmutationP,
            cutLength=params.cutLength,
            selectionBestP=params.selectionBestP
        )

        start = time.time()
        best_solution = ga.run()
        end = time.time()

        results.append({
            "fitnessParam": params.fitnessParam,
            "nbmutationP": params.nbmutationP,
            "cutLength": params.cutLength,
            "selectionBestP": params.selectionBestP,
            "num_bins": len(best_solution),
            "time_sec": round(end - start, 2)
        })

    df = pd.DataFrame(results)
    df_sorted = df.sort_values(by="num_bins").reset_index(drop=True)
    best_row = df_sorted.iloc[0]

    return int(best_row["num_bins"])

