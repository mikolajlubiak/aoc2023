import re
import math
max_cubes_sum = 0
with open('input.txt', 'r') as input:
    data = input.read().splitlines()
    for game in data:
        game_num = int(re.search(r'Game (\d+):', game).group(1))
        game_data = re.sub(r'Game \d+: ', '', game)
        sets = game_data.split('; ')
        max_cubes = {'red': 0, 'green': 0, 'blue': 0}
        for set in sets:
            random_cubes = set.split(', ')
            for cube in random_cubes:
                cube = cube.split(' ')
                if int(cube[0]) > max_cubes[cube[1]]:
                    max_cubes[cube[1]] = int(cube[0])
        max_cubes_sum += math.prod(max_cubes.values())

print(max_cubes_sum)