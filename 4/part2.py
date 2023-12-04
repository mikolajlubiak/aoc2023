import re
with open('input.txt', 'r') as input:
    data = input.read().splitlines()
    copies = [0] * (len(data) + 1)
    for card in data:
        card_sum = 0
        card_data = re.sub(r'Card\s*(\d+):', '', card)
        card_num = int(re.search(r'Card\s*(\d+):', card).group(1))
        sections = card_data.split(' | ')
        copies[card_num] += 1
        for your_num in filter(None, sections[1].split(' ')):
            if your_num in filter(None, sections[0].split(' ')):
                card_sum += 1
        if card_sum > 0:
            for i in range(card_num + 1, card_num + card_sum + 1):
                copies[i] += copies[card_num]
    print(sum(copies))