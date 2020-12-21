import sys, datetime, time
sys.path.append("..")
from math import inf, sqrt, pow
from utils.file_reader import *
from itertools import chain, combinations

"""
    In this assignment you will implement one or more algorithms for the traveling salesman problem, such as the dynamic programming algorithm covered in the video lectures.  
    Here is a data file describing a TSP instance.

    The first line indicates the number of cities.  Each city is a point in the plane, and each subsequent line indicates the x- and y-coordinates of a single city.  

    The distance between two cities is defined as the Euclidean distance --- that is, two cities at locations (x,y)(x,y) and (z,w)(z,w) have distance \sqrt{(x-z)^2 + (y-w)^2} 
    (x−z) 2 +(y−w) 2 between them.  

    In the box below, type in the minimum cost of a traveling salesman tour for this instance, rounded down to the nearest integer.

    OPTIONAL: If you want bigger data sets to play with, check out the TSP instances from around the world here.  
    The smallest data set (Western Sahara) has 29 cities, and most of the data sets are much bigger than that.  
    What's the largest of these data sets that you're able to solve --- using dynamic programming or, if you like, a completely different method?

    HINT: You might experiment with ways to reduce the data set size.  For example, trying plotting the points.  
    Can you infer any structure of the optimal solution?  Can you use that structure to speed up your algorithm?

"""


class City:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude


def get_data():
    lines = list(map(lambda s: s.split(), read_input(FilePath.TSP)))
    num_nodes = int(lines[0][0])
    cities = []

    for line in lines[1:]:
        cities.append(City(float(line[0]), float(line[1])))

    return cities, num_nodes

def euclidean_distance(a, b):
    return sqrt(pow(a.latitude - b.latitude, 2) + pow(a.longitude - b.longitude, 2))

def generate_permutations(size):
    subsets_by_size = {}
    s = list(range(1, size+1))
    sets = chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))

    for subsets in sets:
        problem_size = len(subsets)
        subsets_by_size[problem_size] = subsets_by_size.get(problem_size, []) + [subsets]

    return subsets_by_size


def tsp(cities, n):
    subsets = generate_permutations(n)
    cache = {((1,), 1): 0}

    # missing base case

    for m in range(2, n+1):
        subsets_s = [x for x in subsets[m] if 1 in x]
        for subset_s in subsets_s:
            cache[subset_s, 1] = 0
            for j in subset_s:
                subset_s_minus_j = tuple([x for x in list(subset_s) if x != j])
                possibilities = []
                if j != 1:
                    for k in subset_s:
                        if k != j:
                            ckj = euclidean_distance(cities[k-1], cities[j-1])
                            iteration_result = cache.get((subset_s_minus_j, k), inf) + ckj
                            possibilities.append(iteration_result)
                            print("distance between city %d and %d: %f" % (j, k, ckj))

                    cache[subset_s, j] = min(possibilities)

    subset_all_cities = tuple(list(range(1, n+1)))
    last_iteration = []
    for j in range(2, n+1):
        current_cost = cache[subset_all_cities, j] +euclidean_distance(cities[0], cities[j-1])
        last_iteration.append(current_cost)

    return min(last_iteration)

start = time.time()

print('tsp start time %s' % datetime.datetime.now())
cities, n = get_data()
min_distance = tsp(cities, n)
print('TSP min distance = %d' % min_distance)

print('tsp finish time %s' % datetime.datetime.now())
print('total time elapsed %f' % (time.time() - start))

