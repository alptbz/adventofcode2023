from typing import List


class CardSet:
    TYPE_FIVE_OF_A_KIND = 10
    TYPE_FOUR_OF_A_KIND = 9
    TYPE_FULL_HOUSE = 8
    TYPE_THREE_OF_A_KIND = 7
    TYPE_TWO_PAIR = 6
    TYPE_ONE_PAIR = 5
    TYPE_HIGH_CARD = 4
    CARD_VALUES = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    NUM_CARD_TYPES = 13

    def __init__(self, cards: str, bid: int):
        self.bid = bid
        self.cards = cards
        self.no_duplicates = "".join(set(self.cards))
        self.card_values = list(self.cards)
        for i in range(0, len(self.card_values)):
            if self.card_values[i] in CardSet.CARD_VALUES.keys():
                self.card_values[i] = int(CardSet.CARD_VALUES[self.card_values[i]])
            else:
                self.card_values[i] = int(self.card_values[i])
        self.set_type = self._get_type(self.cards)
        assert len(self.cards) == 5


    def counts_for_type(self, cards):
        counts = []
        no_duplicates = "".join(set(cards))
        for c in no_duplicates:
            counts.append(cards.count(c))
        counts.sort()
        return counts

    def _get_type(self, cards):
        no_duplicates = "".join(set(cards))
        _counts_for_type = self.counts_for_type(cards)
        if len(no_duplicates) == 1:
            return CardSet.TYPE_FIVE_OF_A_KIND
        if len(no_duplicates) == 2:
            if _counts_for_type[0] == 1 and _counts_for_type[1] == 4:
                return CardSet.TYPE_FOUR_OF_A_KIND
            if _counts_for_type[0] == 2 and _counts_for_type[1] == 3:
                return CardSet.TYPE_FULL_HOUSE
        if len(no_duplicates) == 3 and _counts_for_type[-1] == 3:
            return CardSet.TYPE_THREE_OF_A_KIND
        if len(no_duplicates) == 3 and _counts_for_type[-1] == 2 and _counts_for_type[-2] == 2:
            return CardSet.TYPE_TWO_PAIR
        if len(no_duplicates) == 4 and _counts_for_type[-1] == 2:
            return CardSet.TYPE_ONE_PAIR
        if len(no_duplicates) == 5:
            return CardSet.TYPE_HIGH_CARD

    def highest_possible_type(self):
        initial_type = self._get_type(self.cards)


    def highest_card(self):
        return max(self.card_values)

    def first_card_value(self):
        return self.card_values[0]

    def __str__(self):
        return self.cards

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        if other.set_type != self.set_type:
            return other.set_type > self.set_type
        else:
            for i in range(0, len(self.card_values)):
                if other.card_values[i] == self.card_values[i]:
                    continue
                else:
                    return other.card_values[i] > self.card_values[i]

    def __eq__(self, other):
        return sorted(other.card_values) == sorted(self.card_values)


assert CardSet("AAAAA", 0).set_type == CardSet.TYPE_FIVE_OF_A_KIND
assert CardSet("AA8AA", 0).set_type == CardSet.TYPE_FOUR_OF_A_KIND
assert CardSet("23332", 0).set_type == CardSet.TYPE_FULL_HOUSE
assert CardSet("TTT98", 0).set_type == CardSet.TYPE_THREE_OF_A_KIND
assert CardSet("23432", 0).set_type == CardSet.TYPE_TWO_PAIR
assert CardSet("A23A4", 0).set_type == CardSet.TYPE_ONE_PAIR
assert CardSet("23456", 0).set_type == CardSet.TYPE_HIGH_CARD

with open("day7-alptbz.txt", "r") as fp:
    lines_raw = fp.readlines()

card_sets: List[CardSet] = []

for line in lines_raw:
    line_parts = line.strip().split(" ")
    card_sets.append(CardSet(line_parts[0], int(line_parts[1])))

sorted_cardset = sorted(card_sets)

c = 1
total_bids = 0

for card_set in sorted_cardset:
    total_bids += card_set.bid * c
    c += 1

print(f"Part One: {total_bids}")

CardSet.CARD_VALUES['J'] = 1

assert card_sets[0].CARD_VALUES['J'] == 1

