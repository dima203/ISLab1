import random

from matplotlib import pyplot


def calculate_distance(path: tuple[int, ...], cities_map: list[list[int]]) -> int:
    return sum(cities_map[path[i]][path[i + 1]] for i in range(len(path) - 1)) + cities_map[path[-1]][path[0]]


def get_paths(current_path: tuple[int, ...], available_cities: list[int]) -> list[tuple[int, ...]]:
    if len(available_cities) == 0:
        return [current_path]
    if len(available_cities) == 1:
        return [current_path + (available_cities[0],)]

    result = []
    for city in available_cities:
        result.extend(get_paths(current_path + (city, ), list(filter(lambda x: x != city, available_cities))))
    return result


def get_shortest_path_brute_force(cities_map: list[list[int]]) -> tuple[tuple[int, ...], int]:
    paths = get_paths((), list(range(len(cities_map))))
    min_path = paths[0]
    min_distance = calculate_distance(min_path, cities_map)
    for path in paths:
        distance = calculate_distance(path, cities_map)
        if distance < min_distance:
            min_path = path
            min_distance = distance

    return min_path, min_distance


def get_shortest_path_far_neighbor(cities_map: list[list[int]]) -> tuple[tuple[int, ...], int]:
    path = (0, )
    distance = 0
    for _ in range(len(cities_map) - 1):
        far_city = 0
        far_distance = float('inf')
        for city, city_distance in enumerate(cities_map[path[-1]]):
            if city not in path and city_distance < far_distance:
                far_city = city
                far_distance = city_distance
        distance += far_distance
        path += (far_city, )
    distance += cities_map[path[-1]][path[0]]
    return path, distance


def get_shortest_path_modeling(cities_map: list[list[int]], iterations: int) -> tuple[tuple[int, ...], int]:
    paths = get_paths((), list(range(len(cities_map))))
    min_path = random.choice(paths)
    min_distance = calculate_distance(min_path, cities_map)
    distances = []
    for i in range(iterations):
        path = random.choice(paths)
        distance = calculate_distance(path, cities_map)
        if distance < min_distance:
            min_path = path
            min_distance = distance
        distances.append(min_distance)
    pyplot.plot(distances)
    pyplot.show()
    return min_path, min_distance
