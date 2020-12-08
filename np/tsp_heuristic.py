import sys, datetime, time
sys.path.append("..")
from math import inf, sqrt, pow
from utils.file_reader import *

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