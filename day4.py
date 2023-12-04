import math
import re
from typing import List, Dict


class ScratchCard:

    def __init__(self, card_number: int, number_i_have: List[int], winning_numbers: List[int]):
        self.card_number = card_number
        self.winning_numbers = winning_numbers
        self.number_i_have = number_i_have

    def winning_points(self):
        winning_numbers_i_have = self.number_of_numbers_i_won()
        if winning_numbers_i_have == 0:
            return 0
        return math.pow(2, winning_numbers_i_have-1)

    def number_of_numbers_i_won(self) -> int:
        return len([x for x in self.number_i_have if x in self.winning_numbers])

    def __str__(self):
        return f'{self.card_number}: {self.winning_points()}'

    def __repr__(self):
        return self.__str__()


with open("day4.txt", "r") as fp:
    gamesraw = fp.readlines()

cards: List[ScratchCard] = []
cards_to_process: List[ScratchCard] = []
cards_to_count: Dict[ScratchCard, int] = {}
id_to_card: Dict[int, ScratchCard] = {}

for game in gamesraw:
    gameparts1 = game.split(":")
    numberparts = gameparts1[1].split("|")
    gamenumber = int(re.findall(r'\d+', gameparts1[0])[0])
    numbers_i_have = re.findall(r'\d+', numberparts[0])
    winning_numbers = re.findall(r'\d+', numberparts[1])
    sc = ScratchCard(gamenumber, numbers_i_have, winning_numbers)
    cards.append(sc)
    cards_to_count[sc] = 1
    id_to_card[gamenumber] = sc
    cards_to_process.append(sc)

winning_points_total = int(sum(x.winning_points() for x in cards))

print(f"Part One: {winning_points_total}")

while len(cards_to_process) > 0:
    card = cards_to_process.pop(0)
    faktor = cards_to_count[card]
    print(f"[{len(cards_to_process)}] Card {card.card_number} won {card.number_of_numbers_i_won()}")
    for i in range(card.card_number + 1, card.card_number + card.number_of_numbers_i_won() + 1):
        if i in id_to_card:
            cards_to_count[id_to_card[i]] += 1 * faktor
            #print(f"Adding card {id_to_card[i].card_number} to stack")


total_num_of_scratch_cards = sum([cards_to_count[k] for k in cards_to_count])

print(f"Total number of scratch-cards: {total_num_of_scratch_cards}")

