from path_finder import get_shortest_path_brute_force, get_shortest_path_far_neighbor, get_shortest_path_modeling


cities = [
    [0, 7, 4, 2, 8, 5, 1, 17, 14, 21],
    [7, 0, 5, 9, 8, 3, 15, 11, 7, 24],
    [4, 5, 0, 6, 3, 1, 11, 8, 12, 19],
    [2, 9, 6, 0, 4, 13, 9, 26, 17, 5],
    [8, 8, 3, 4, 0, 16, 19, 6, 7, 6],
    [5, 3, 1, 13, 16, 0, 7, 4, 5, 2],
    [1, 15, 11, 9, 19, 7, 0, 1, 3, 9],
    [17, 11, 8, 26, 6, 4, 1, 0, 9, 4],
    [14, 7, 12, 17, 7, 5, 3, 9, 0, 8],
    [21, 24, 19, 5, 6, 2, 9, 4, 8, 0],
]

print(*get_shortest_path_brute_force(cities))
print(*get_shortest_path_far_neighbor(cities))
print(*get_shortest_path_modeling(cities, 100))
print(*get_shortest_path_modeling(cities, 1000))
print(*get_shortest_path_modeling(cities, 10000))

