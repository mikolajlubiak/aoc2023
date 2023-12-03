import re
cubes = {'red': 12, 'green': 13, 'blue': 14}
sum = 0
with open('input.txt', 'r') as input:
    data = input.read().splitlines()
    for game in data:
        game_num = int(re.search(r'Game (\d+):', game).group(1))
        game_data = re.sub(r'Game \d+: ', '', game)
        sets = game_data.split('; ')
        possible = True
        for set in sets:
            random_cubes = set.split(', ')
            for cube in random_cubes:
                cube = cube.split(' ')
                if int(cube[0]) > cubes[cube[1]]:
                    possible = False
        if possible:
            sum += game_num
print(sum)
