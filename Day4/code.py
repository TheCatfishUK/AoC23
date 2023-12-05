data = 1

if data == 0:
    f = open("test.py")
else:
    f = open("input.py")

result = 0

# PART 1
# for line in f:
#     line = line.strip()
#     line = line.split(":")
#     line = line[1].split("|")
#     winning = line[0].split(" ")
#     test = line[1].split(" ")
#     outcome = 0
#     for win in winning:
#         if win == '':
#             pass
#         elif win in test:
#             outcome+= 1
#     if outcome != 0:
#         result += 2**(outcome-1)
# print(result)

cards = []

# PART 2
for line in f:
    line = line.strip()
    line = line.split(":")
    line = line[1].split("|")
    winning = line[0].split(" ")
    test = line[1].split(" ")
    
    cards.append({"id":len(cards)+1, "W":winning, "T":test, "copies":1})
    
for card in cards:
    win_range = 0
    for win in card["W"]:
        if win == '':
            pass
        elif win in card["T"]:
            win_range += 1
    if win_range != 0:
        for i in range(win_range):
            cards[card['id']+i]['copies']+=card['copies']

result = 0
for a in cards:
    result += int(a['copies'])

print(result)
