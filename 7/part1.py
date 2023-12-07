cards = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
with open('input.txt', 'r') as input:
    data = input.readlines()
    data = (x.strip() for x in data)
    hands = []
    sum = 0
    for line in data:
        hand = line.split(' ')[0]
        bid = int(line.split(' ')[1])
        rank = 0
        card_counter = {}
        for card in hand:
            if card not in card_counter:
                card_counter[card] = 1
            else:
                card_counter[card] += 1

        values = card_counter.values()

        if len(values) == 1:
            rank = 7
        elif len(values) == 2:
            rank = 6
        elif max(values) == 3 and len(values) == 2:
            rank = 5
        elif max(values) == 3 and len(values) == 3:
            rank = 4
        elif max(values) == 2 and len(values) == 3:
            rank = 3
        elif max(values) == 2 and len(values) == 4:
            rank = 2
        else:
            rank = 1

        hands.append([hand, bid, rank])

    hands = sorted(hands, key=lambda x: x[2], reverse=True)

    for i in range(len(hands)):
        for j in range(i+1, len(hands)):
            if hands[i][2] == hands[j][2]:
                for k in range(len(hands[i][0])):
                    if cards[hands[i][0][k]] < cards[hands[j][0][k]]:
                        hands[i], hands[j] = hands[j], hands[i]
                        break
                    elif cards[hands[i][0][k]] > cards[hands[j][0][k]]:
                        break

    hands.reverse()

    for i in range(len(hands)):
        sum += hands[i][1]*(i+1)

print(sum)