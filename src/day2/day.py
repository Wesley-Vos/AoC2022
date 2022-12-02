from src.util.day import Day
from enum import Enum
from dataclasses import dataclass


class Player:
    _points = 0

    def __init__(self):
        pass

    def win(self):
        self._points += 6

    def draw(self):
        self._points += 3

    def lose(self):
        self._points += 0

    def add_move_points(self, move):
        self._points += move.value

    def get_points(self):
        return self._points


class RPS:
    class Action(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    class Outcome(Enum):
        PLAYER1_WIN = 0
        PLAYER2_WIN = 1
        DRAW = 2

    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2

    def play(self, rounds):
        for round in rounds:
            self._play_round(round)

    def _play_round(self, round):
        pass

    def _finish_round(self, round):
        self.player1.add_move_points(round.player1_move)
        self.player2.add_move_points(round.player2_move)

        match round.outcome:
            case RPS.Outcome.PLAYER1_WIN:
                self.player1.win()
                self.player2.lose()
            case RPS.Outcome.PLAYER2_WIN:
                self.player2.win()
                self.player1.lose()
            case RPS.Outcome.DRAW:
                self.player1.draw()
                self.player2.draw()


class ForwardRPS(RPS):
    def _play_round(self, round):
        match round.player1_move:
            case RPS.Action.ROCK:
                match round.player2_move:
                    case RPS.Action.ROCK:
                        round.outcome = RPS.Outcome.DRAW
                    case RPS.Action.SCISSORS:
                        round.outcome = RPS.Outcome.PLAYER1_WIN
                    case RPS.Action.PAPER:
                        round.outcome = RPS.Outcome.PLAYER2_WIN
            case RPS.Action.SCISSORS:
                match round.player2_move:
                    case RPS.Action.ROCK:
                        round.outcome = RPS.Outcome.PLAYER2_WIN
                    case RPS.Action.SCISSORS:
                        round.outcome = RPS.Outcome.DRAW
                    case RPS.Action.PAPER:
                        round.outcome = RPS.Outcome.PLAYER1_WIN
            case RPS.Action.PAPER:
                match round.player2_move:
                    case RPS.Action.ROCK:
                        round.outcome = RPS.Outcome.PLAYER1_WIN
                    case RPS.Action.SCISSORS:
                        round.outcome = RPS.Outcome.PLAYER2_WIN
                    case RPS.Action.PAPER:
                        round.outcome = RPS.Outcome.DRAW

        super()._finish_round(round)


class InverseRPS(RPS):
    def _play_round(self, round):
        match round.player1_move:
            case RPS.Action.ROCK:
                match round.outcome:
                    case RPS.Outcome.PLAYER1_WIN:
                        round.player2_move = RPS.Action.SCISSORS
                    case RPS.Outcome.PLAYER2_WIN:
                        round.player2_move = RPS.Action.PAPER
                    case RPS.Outcome.DRAW:
                        round.player2_move = RPS.Action.ROCK
            case RPS.Action.PAPER:
                match round.outcome:
                    case RPS.Outcome.PLAYER1_WIN:
                        round.player2_move = RPS.Action.ROCK
                    case RPS.Outcome.PLAYER2_WIN:
                        round.player2_move = RPS.Action.SCISSORS
                    case RPS.Outcome.DRAW:
                        round.player2_move = RPS.Action.PAPER
            case RPS.Action.SCISSORS:
                match round.outcome:
                    case RPS.Outcome.PLAYER1_WIN:
                        round.player2_move = RPS.Action.PAPER
                    case RPS.Outcome.PLAYER2_WIN:
                        round.player2_move = RPS.Action.ROCK
                    case RPS.Outcome.DRAW:
                        round.player2_move = RPS.Action.SCISSORS

        super()._finish_round(round)


@dataclass
class Round:
    player1_move: RPS.Action
    player2_move: RPS.Action | None
    outcome: RPS.Outcome | None


PLAYER1_MOVE_MAPPING = {
    "A": RPS.Action.ROCK,
    "B": RPS.Action.PAPER,
    "C": RPS.Action.SCISSORS
}

PLAYER2_MOVE_MAPPING = {
    "X": RPS.Action.ROCK,
    "Y": RPS.Action.PAPER,
    "Z": RPS.Action.SCISSORS
}

OUTCOME_MAPPING = {
    "X": RPS.Outcome.PLAYER1_WIN,
    "Y": RPS.Outcome.DRAW,
    "Z": RPS.Outcome.PLAYER2_WIN
}


class Day2(Day):
    first_column = None
    second_column = None

    def __init__(self):
        super().__init__(filename="input.txt")

    def solve_part1(self):
        rounds = []
        for row in self.data:
            player1_move, player2_move = row.split(" ")
            rounds.append(Round(
                player1_move=PLAYER1_MOVE_MAPPING[player1_move],
                player2_move=PLAYER2_MOVE_MAPPING[player2_move],
                outcome=None
            ))

        player1 = Player()
        player2 = Player()

        game = ForwardRPS(
            player1=player1,
            player2=player2
        )
        game.play(rounds)
        return game.player2.get_points()

    def solve_part2(self):
        rounds = []
        for row in self.data:
            player1_move, outcome = row.split(" ")
            rounds.append(Round(
                player1_move=PLAYER1_MOVE_MAPPING[player1_move],
                player2_move=None,
                outcome=OUTCOME_MAPPING[outcome]
            ))

        player1 = Player()
        player2 = Player()

        game = InverseRPS(
            player1=player1,
            player2=player2
        )
        game.play(rounds)
        return game.player2.get_points()


def main():
    day2 = Day2()
    day2.run()


if __name__ == "__main__":
    main()
