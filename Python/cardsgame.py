from random import shuffle

suite = 'H, D, S, C'.split()
ranks = '2, 3, 4, 5, 6, 7, 8, 9, K, J, Q, A'.split()

# my_cards = [(s, r) for s in suite for r in ranks]
# my_cards = []
# for r in ranks:
#     for s in suite:
#         my_cards.append((s, r))

class desk:
    def __init__(self):
        print(" Creating the new desk ")
        self.all_cards = [(s, r) for s in suite for r in ranks]
    def shuffle(self):
        print(" Shuffle desk ")
        shuffle(self.all_cards)
    def split_in_half(self):
        return (self.all_cards[:26], self.all_cards[26:])

class hand:
    def __init__(self,cards):
        self.cards = cards
    def __str__(self):
        return " Contains {} cards ".format(len(self.cards))
    def add(self, add_cards):
        self.cards.extend(add_cards)
    def remove_card(self):
        self.cards.pop()

class player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} are placed {}".format(self.name, drawn_card))
        print(" \n ")
        return drawn_card
    def remove_warcards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards
    def still_cards(self):
        return len(self.hand.cards) != 0

#Game logic
print(" Welcome to war, Let's Begins..........")
#Split into half
d = desk()
d.shuffle()
half1, half2 = d.split_in_half()

#create both the players
comp = player("computer", hand(half1))
name = input(" Enter your name: ")
user = player("name", hand(half2))
total_rounds = 0
war_count = 0
while user.still_cards() and comp.still_cards():
    total_rounds += 1
    print(" Time for new round: ")
    print(" Here are the current round")
    print(user.name+" have count: " +str(len(user.hand.cards)))
    print(comp.name+" have count: " +str(len(comp.hand.cards)))
    print(" If you want to play game! ")
    print(" \n ")
    table_cards =[]
    comp_card = comp.play_card()
    user_card = user.play_card()
    table_cards.append(comp_card)
    table_cards.append(user_card)

    if comp_card[1] == user_card[1]:
        war_count += 1
        print(" War ")
        table_cards.extend(user.remove_warcards())
        table_cards.extend(comp.remove_warcards())

        if ranks.index(comp_card[1]) < ranks.index(user_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
print(" Game over , Number of rounds: "+str(total_rounds))
print(" War happened here :"+str(war_count)+" times ")
print(" Computer still have cards? ")
print(str(comp.still_cards))
print(" Player still have cards? ")
print(str(user.still_cards))




