from collections import Counter

import utils
from enum import Enum


class Game(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3


class Outcome(Enum):
    Win = 6
    Tie = 3
    Loss = 0


def determine_winner(p1: Game, p2: Game) -> int:
    # Rock beats Scissors
    # Scissors beat Paper
    # Paper beats Rock
    if p1 == p2:
        # it's a tie
        return p2.value + 3
    elif p1.value > p2.value:
        if p1 == Game.Scissors and p2 == Game.Rock:
            # player 2 wins
            return p2.value + 6
        else:
            # player 1 wins
            return p2.value
    else:
        if p1 == Game.Rock and p2 == Game.Scissors:
            # player 1 wins
            return p2.value
        else:
            # player 2 wins
            return p2.value + 6


def determine_outcome(p1: Game, outcome: Outcome) -> int:
    if outcome == Outcome.Loss:
        if p1 == Game.Rock:
            return Game.Scissors.value + Outcome.Loss.value
        if p1 == Game.Paper:
            return Game.Rock.value + Outcome.Loss.value
        if p1 == Game.Scissors:
            return Game.Paper.value + Outcome.Loss.value
    elif outcome == Outcome.Win:
        if p1 == Game.Rock:
            return Game.Paper.value + Outcome.Win.value
        if p1 == Game.Paper:
            return Game.Scissors.value + Outcome.Win.value
        if p1 == Game.Scissors:
            return Game.Rock.value + Outcome.Win.value
    else:
        return p1.value + Outcome.Tie.value

def day2():
    print("###########")
    print("# Day  2  #")
    print("###########")
    game_map = {
        "A": Game.Rock,
        "B": Game.Paper,
        "C": Game.Scissors,
        "X": Game.Rock,
        "Y": Game.Paper,
        "Z": Game.Scissors
    }
    outcome_map = {
        "X": Outcome.Loss,
        "Y": Outcome.Tie,
        "Z": Outcome.Win
    }
    part1_score = 0
    part2_score = 0
    with open("day2/input2", "rb") as data:
        for line in data:
            line = line.strip().decode("utf8")
            player1 = game_map.get(line[0])
            player2 = game_map.get(line[2])
            part1_score += determine_winner(player1, player2)
            outcome = outcome_map.get(line[2])
            part2_score += determine_outcome(player1, outcome)
        print(f"Part 1: Game score is {part1_score}")
        print(f"Part 2: Game score is {part2_score}")
