from heuristics import nextfit

weight = [2, 5, 4, 7, 1, 3, 8]
c = 10

print(f'Number of bins required in Next Fit : {nextfit(weight, c)}')