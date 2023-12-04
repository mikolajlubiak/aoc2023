import re
sum = 0
with open('input.txt', 'r') as input:
    data = input.read().splitlines()
    for card in data:
        card_sum = 0
        card_data = re.sub(r'Card \d+: ', '', card)
        sections = card_data.split(' | ')
        for your_num in filter(None, sections[1].split(' ')):
            if your_num in filter(None, sections[0].split(' ')):
                if card_sum == 0:
                    card_sum = 1
                else:
                    card_sum *= 2
        sum += card_sum
print(sum)