import re


class SingleGame:

    def __init__(self, id: int):
        self.rounds = []
        self.id = id

    def add_round(self, round):
        self.rounds.append(round)

    def __str__(self):
        return f'{self.id}: {self.rounds}'

    def __repr__(self):
        return self.__str__()

    def max_red(self):
        return max(x.red for x in self.rounds)

    def max_green(self):
        return max(x.green for x in self.rounds)

    def max_blue(self):
        return max(x.blue for x in self.rounds)


class GameRound:

    def __init__(self):
        self.green = 0
        self.blue = 0
        self.red = 0

    def add_by_str(self, inval):
        _num = int(re.findall(r'\d+', inval)[0])
        if "green" in inval:
            self.green += _num
        if "blue" in inval:
            self.blue += _num
        if "red" in inval:
            self.red += _num

    def __str__(self):
        return f'r:{self.red} b:{self.blue} g:{self.green}'

    def __repr__(self):
        return self.__str__()


with open("day2.txt", "r") as fp:
    gamesraw = fp.readlines()

games = []

for gameraw in gamesraw:
    gparts1 = gameraw.strip().split(":")
    game = SingleGame(int(re.findall(r'\d+', gparts1[0])[0]))
    colorparts = gparts1[1].split(";")
    for colorpart in colorparts:
        gameround = GameRound()
        subcolorparts = colorpart.split(',')
        for subcolorpart in subcolorparts:
            gameround.add_by_str(subcolorpart)
        game.add_round(gameround)
    games.append(game)


print(games)

_sum_ids = 0

for game in games:
    if game.max_red() <= 12 and game.max_green() <= 13 and game.max_blue() <= 14:
        _sum_ids += game.id

print(f'Part One: {_sum_ids}')

_sumpower = sum(x.max_green() * x.max_blue() * x.max_red() for x in games)

print(f'Part Two: {_sumpower}')