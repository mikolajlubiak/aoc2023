import re

sum = 0
with open('input.txt', 'r') as input:
    data = input.read().splitlines()
    for i, line in enumerate(data):
        for k, char in enumerate(line):
            if char == '*':
                nums = []
                for e in (-1, 0, 1):
                    matches = re.finditer(r'\d+', data[i + e])
                    for match in matches:
                        num = match.group()
                        start_index = match.start()
                        for j in range(start_index, len(num) + start_index):
                            if k == j - 1 or \
                                    k == j or \
                                    k == j + 1:
                                nums.append(int(num))
                                break
                if len(nums) == 2:
                    sum += nums[0] * nums[1]
print(sum)
