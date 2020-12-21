import sys, datetime, time
sys.path.append("..")
from math import inf, sqrt, pow
from utils.file_reader import *


"""
    In this assignment we will revisit an old friend, the traveling salesman problem (TSP).  This week you will implement a heuristic for the TSP, rather than an exact algorithm, and as a result will be able to handle much larger problem sizes.  
    Here is a data file describing a TSP instance (original source: http://www.math.uwaterloo.ca/tsp/world/bm33708.tsp).
    
    The first line indicates the number of cities. Each city is a point in the plane, and each subsequent line indicates the x- and y-coordinates of a single city.

    The distance between two cities is defined as the Euclidean distance --- that is, two cities at locations (x,y)(x,y) and (z,w)(z,w) have distance \sqrt{(x-z)^2 + (y-w)^2} 
    (x−z) 2+(y−w) 2 between them.
    
    You should implement the nearest neighbor heuristic:
    
    Start the tour at the first city.
    Repeatedly visit the closest city that the tour hasn't visited yet.  In case of a tie, go to the closest city with the lowest index.  For example, if both the third and fifth cities have the same distance from the first city (and are closer than any other city), 
    then the tour should begin by going from the first city to the third city.
    
    Once every city has been visited exactly once, return to the first city to complete the tour.
    In the box below, enter the cost of the traveling salesman tour computed by the nearest neighbor heuristic for this instance, rounded down to the nearest integer.
    
    [Hint: when constructing the tour, you might find it simpler to work with squared Euclidean distances (i.e., the formula above but without the square root) than Euclidean distances.  But don't forget to report the length of the tour in terms of standard Euclidean distance.]

"""

class City:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

def get_data():
    lines = list(map(lambda s: s.split(), read_input(FilePath.TSP_HEURISTIC)))
    num_nodes = int(lines[0][0])
    cities = []

    for line in lines[1:]:
        cities.append(City(float(line[1]), float(line[2])))

    return cities, num_nodes

def euclidean_distance(a, b):
    return sqrt(pow(a.latitude - b.latitude, 2) + pow(a.longitude - b.longitude, 2))

def tsp(cities, n):
    current_city = 0
    visited_cities = {current_city}
    total_cost = 0

    while len(visited_cities) < n:
        current_cost = inf
        next_city = None

        for i in range(len(cities)):
            if i not in visited_cities:
                candidate_city = cities[i]
                distance = euclidean_distance(cities[current_city], candidate_city)
                if distance < current_cost:
                    current_cost = distance
                    next_city = i

        current_city = next_city
        total_cost+=current_cost
        visited_cities.add(current_city)

    last_distance = euclidean_distance(cities[0], cities[current_city])

    return total_cost + last_distance

start = time.time()

print('TSP Heuristic start time: %s' % datetime.datetime.now())
cities, n = get_data()
min_distance = tsp(cities, n)
print('TSP Heuristic  min distance = %d' % min_distance)

print('TSP Heuristic finish time: %s' % datetime.datetime.now())
print('Total time elapsed: %f' % (time.time() - start))