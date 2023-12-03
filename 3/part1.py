import re
sum = 0
with open('input.txt', 'r') as input:
    data = input.read().splitlines()
    for i, line in enumerate(data):
        matches = re.finditer(r'\d+', line)
        for match in matches:
            num = match.group()
            start_index = match.start()
            for j in range(start_index, len(num) + start_index):
                try:
                    if (data[i - 1][j - 1] != '.' and not data[i - 1][j - 1].isdigit()) or \
                            (data[i - 1][j] != '.' and not data[i - 1][j].isdigit()) or \
                            (data[i - 1][j + 1] != '.' and not data[i - 1][j + 1].isdigit()) or \
                            (data[i][j - 1] != '.' and not data[i][j - 1].isdigit()) or \
                            (data[i][j + 1] != '.' and not data[i][j + 1].isdigit()) or \
                            (data[i + 1][j - 1] != '.' and not data[i + 1][j - 1].isdigit()) or \
                            (data[i + 1][j] != '.' and not data[i + 1][j].isdigit()) or \
                            (data[i + 1][j + 1] != '.' and not data[i + 1][j + 1].isdigit()):
                        sum += int(num)
                        break
                except:
                    pass
print(sum)