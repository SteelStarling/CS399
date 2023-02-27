"""
    Program: CS399 Midterm - Chicago
    Author:  Taylor Hancock
    Date:    02/23/2023
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from random import randint


@dataclass
class Player:
    name: str
    score: int = 0

    def __str__(self):
        return self.name + ", Score: " + self.score.__str__()


class Game:

    games_played = 0

    def __init__(self, players: [Player]) -> None:
        self.players = players

    def champions(self) -> [Player]:
        """:return: list of player(s), with the highest score, or an empty list, if nobody scored."""
        # Calculate max score
        max_val = max(self.players, key=lambda x: x.score).score

        # if zero, return empty list
        if max_val == 0:
            return []

        # only return max scoring players
        return list([player for player in self.players if player.score == max_val])

    def play(self) -> None:
        self.games_played += 1
        pass


class Chicago(Game):
    def __init__(self, players: [Player]) -> None:
        super().__init__(players)

    def play(self) -> [Player]:
        self.games_played += 1

        # reset player scores
        for player in self.players:
            player.score = 0

        # play game
        for goal in range(2, 13):
            for player in self.players:
                dice_val = randint(1, 6) + randint(1, 6)
                if dice_val == goal:
                    player.score += goal

        for player in self.players:
            print(player.score)
        # return champions
        return super(self.__class__, self).champions()


class DoubleRoll(Game):

    def __init__(self, players: [Player]) -> None:
        super().__init__(players)

    def play(self) -> [Player]:
        self.games_played += 1

        # reset player scores
        for player in self.players:
            player.score = 0

        # play game
        for goal in range(2, 13):
            for player in self.players:
                die_1 = randint(1, 6)
                die_2 = randint(1, 6)

                # check for win
                dice_val = die_1 + die_2
                if dice_val == goal:
                    player.score += goal
                else:
                    # assume which die is rerolled is random
                    if randint(1, 2) == 1:
                        die_1 = randint(1, 6)
                    else:
                        die_2 = randint(1, 6)

                    # check again
                    dice_val = die_1 + die_2
                    if dice_val == goal:
                        player.score += goal

        # return champions
        return super(self.__class__, self).champions()


contestants = [
    Player("Ricky Bell"),
    Player("Michael Bivins"),
    Player("Bobby Brown"),
    Player("Ronnie DeVoe"),
    Player("Johnny Gill"),
    Player("Ralph Tresvant")
]

for game in (Chicago(contestants), DoubleRoll(contestants)):
    valid_game_found = False
    while not valid_game_found:
        winners = game.play()
        # only count if greater than 2
        if len(winners) >= 2:
            valid_game_found = True

            print(f"After {game.games_played} {game.__class__} games played, a single game had multiple winners:")
            print_str = "Winners: "
            for winner in winners:
                print_str += winner.__str__() + " - "
            print(print_str)
