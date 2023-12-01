sum = 0
with open('input.txt', 'r') as input:
	data = input.read().splitlines()
	for line in data:
		num = ''
		for char in line:
			if char.isdigit():
				num += char
				break
		for char in reversed(line):
			if char.isdigit():
				num += char
				break
		if num:
			sum += int(num)

print(sum)
