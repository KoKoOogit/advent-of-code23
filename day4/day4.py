inp = open("input.txt","r")
cards = []
active_line = 0 
class Card:
    def __init__(self,idx, match):
        self.match = match
        self.copy = 1
        self.idx = idx
    
    def copy_card(self):
       
        self.copy += 1
    
    def __str__(self):
        return f"{self.idx}"

part_1 = 0
part_2 = 0
for line in inp:
    content = line.split("\n")[0]
    numbers = content.split(":")[1]
    splitter = numbers.split("|")
    winning = [int(x) for x in splitter[0][1:-1].split()]
    mines = [int(y) for y in splitter[1][1:].split()]
    matches = len([z for z in winning if z in mines])
    print(matches)
    point = 2**(matches-1) if 2**(matches-1) >= 1 else 0
    part_1 += point
    card = Card(active_line,matches)

    cards.append(card)
    active_line += 1


for i in cards:
    idx = i.idx
    matches = i.match
    copies = i.copy

    part_2 +=  i.copy
   
    for copy in range(0,copies):
        for c in range(idx+1,idx+matches+1):
            if c < len(cards):
                next_card = cards[c]
                next_card.copy_card()
                print(f"{idx+1}: added 1 to {c+1}")

    print() 

print(part_2)