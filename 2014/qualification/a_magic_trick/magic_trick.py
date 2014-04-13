"""
Magician arranges 16 cards in a square grid: 4 rows of cards with 4 cards in each row.
Each card has a different number.

Magician asks for someone to choose one card telling the row.

Magician rearranges cars -> asks again for card row -> then determines chosen card.

You're given two arrangement of cards with the row.

Program needs to say: - which card is chosen if there's a single possibility.
                      - "Bad magician!" if >1 card possibility.
                      - "Volunteer cheated!" if 0 card possibilities.
"""
from jam_utils.jam_parser import JamParser
from jam_utils.jam_solver import JamSolver

PATH_DATA = "A-small-attempt0.in"
PATH_OUTPUT = PATH_DATA.split(".")[0] + ".out"  # Same name as path data, except for the file format.


class MagicTrickInstance(object):
    def __init__(self):
        self.first_row = None
        self.second_row = None
        self.first_cards = None
        self.second_cards = None


class MagicTrickParser(JamParser):
    def parse(self):
        for index in range(0, len(self.data), 10):  # Iter for every different magic trick instance in input data file.
            instance = MagicTrickInstance()
            instance.first_row = int(self.data[index][0])
            instance.second_row = int(self.data[index + 5][0])

            first_cards = []
            for first_hand_index in range(index + 1, index + 5):
                first_cards.append(self.parse_cards(first_hand_index))
            instance.first_cards = first_cards

            first_cards = []
            for second_hand_index in range(index + 6, index + 10):
                first_cards.append(self.parse_cards(second_hand_index))
            instance.second_cards = first_cards

            self.instances.append(instance)

    def parse_cards(self, index):
        cards_as_str = self.data[index]
        numeric_cards = map(lambda s: int(s), cards_as_str)
        return numeric_cards


class MagicTrickSolver(JamSolver):
    def solve_instance(self, instance):
        # Strategy: count how many numbers can be in both the rows the player said.

        first_row = instance.first_cards[instance.first_row - 1]
        second_row = instance.second_cards[instance.second_row - 1]

        possible_cards = []
        for card in first_row:
            if card in second_row:
                possible_cards.append(card)

        return self.craft_solution(possible_cards)

    def craft_solution(self, possible_cards):
        if len(possible_cards) == 1:
            return str(possible_cards[0])
        elif len(possible_cards) > 1:
            return "Bad magician!"
        else:
            return "Volunteer cheated!"


if __name__ == "__main__":
    parser = MagicTrickParser(PATH_DATA)
    solver = MagicTrickSolver(PATH_OUTPUT)
    solver.solve(parser.instances)










