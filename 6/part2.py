import re
sum = 1
with open('input.txt', 'r') as input:
    data = input.read().splitlines()
    time = int(data[0].replace(' ', '').replace('Time:', ''))
    best_distance = int(data[1].replace(' ', '').replace('Distance:', ''))
    possible_wins = 0
    for j in range(time):
        distance = (time-j)*j
        if distance > best_distance:
            possible_wins += 1
    sum *= possible_wins
print(sum)


