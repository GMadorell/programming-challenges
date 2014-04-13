


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


PATH_DATA = "A-small-attempt0.in"
PATH_OUTPUT = "output.txt"


### PARSING

with open(PATH_DATA, "r") as fd:
    data = fd.readlines()

data = data[1:]
data = map(lambda s: s.strip(), data)

class MagicTrickInstance(object):
    def __init__(self):
        self.first_row = None
        self.second_row = None
        self.first_cards = None
        self.second_cards = None

instances = []

for index in range(0, len(data), 10):  # Iter for every different magic trick instance in input data file.
    instance = MagicTrickInstance()
    instance.first_row = int(data[index])
    instance.second_row = int(data[index+5])

    second_cards = []
    for first_hand_index in range(index+1, index+5):
        cards_as_str = data[first_hand_index]
        splitted_cards = cards_as_str.split()
        numeric_cards = map(lambda s: int(s), splitted_cards)
        second_cards.append(numeric_cards)
    instance.first_cards = second_cards

    second_cards = []
    for second_hand_index in range(index+6, index+10):
        cards_as_str = data[second_hand_index]
        splitted_cards = cards_as_str.split()
        numeric_cards = map(lambda s: int(s), splitted_cards)
        second_cards.append(numeric_cards)
    instance.second_cards = second_cards

    instances.append(instance)


### PROBLEM SOLVING
def solve_instance(instance):
    # Strategy: count how many numbers can be in both the rows the player said.

    first_row = instance.first_cards[instance.first_row - 1]
    second_row = instance.second_cards[instance.second_row - 1]

    possible_cards = []
    for card in first_row:
        if card in second_row:
            possible_cards.append(card)

    return craft_solution(possible_cards)


def craft_solution(possible_cards):
    if len(possible_cards) == 1:
        return str(possible_cards[0])
    elif len(possible_cards) > 1:
        return "Bad magician!"
    else:
        return "Volunteer cheated!"

solutions = []
for instance in instances:
    solutions.append(solve_instance(instance))

with open(PATH_OUTPUT, "w") as output_file:
    for i, solution in enumerate(solutions, start=1):
        newline_needed = True if i != len(solutions) else False
        output_file.write("Case #{0}: {1}{2}".format(i, solution, "\n" if newline_needed else ""))



