import re
sum = 1
with open('input.txt', 'r') as input:
    data = input.read().splitlines()
    times = list(map(int, filter(None, re.sub(r'Time:\s*', '', data[0]).split(' '))))
    distances = list(map(int, filter(None, re.sub(r'Distance:\s*', '', data[1]).split(' '))))
    for i in range(len(times)):
        possible_wins = 0
        for j in range(times[i]):
            distance = (times[i]-j)*j
            if distance > distances[i]:
                possible_wins += 1
        sum *= possible_wins
print(sum)


