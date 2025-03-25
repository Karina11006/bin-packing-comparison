from heuristics import nextfit, first_fit, best_fit

weight = [2, 5, 4, 7, 1, 3, 8]
c = 10

print(f'Number of bins required in Next Fit : {nextfit(weight, c)}')
print(f'Number of bins required in First Fit : {first_fit(weight, c)}')
print(f'Number of bins required in Best Fit : {best_fit(weight, c)}')