digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
sum = 0
with open('input.txt', 'r') as input:
	data = input.read().splitlines()
	for line in data:
		num = ''
		for i, char in enumerate(line):
			loop = True
			for j, digit in enumerate(digits):
				if line[i:i+len(digit)] == digit:
					num += str(j+1)
					loop = False
					break
			if loop == False:
				break
			if char.isdigit():
				num += char
				break
		for i, char in enumerate(reversed(line)):
			loop = True
			for j, digit in enumerate(digits):
				if i == 0:
					if line[-len(digit):] == digit:
						num += str(j+1)
						loop = False
						break
				else:
					if line[-len(digit)-i:-i] == digit:
						num += str(j+1)
						loop = False
						break
			if loop == False:
				break
			if char.isdigit():
				num += char
				break
		if num:
			sum += int(num)

print(sum)
