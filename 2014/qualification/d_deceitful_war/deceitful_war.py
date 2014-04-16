# coding=utf-8

"""
Deceitful War - https://code.google.com/codejam/contest/2974486/dashboard#s=p3
------------------------

Game between Naomi and Ken.
Each of them get N identical-looking blocks.
All blocks have different weights between 0.0kg and 1.0kg inclusive.

War game:
1.- Each player knows the weights of his/her own blocks.
2.- Repeat N times:
    - Naomi chooses block.
    - Naomi tells Ken mass of the block.
    - Ken chooses a block.
    - Whoever block weights more wins one point.
    - Both blocks are burned. Therefore, no repetitions allowed.


Another game: Deceitful War
Very similar but Naomi has more chances to win.
1.- Naomi knows all weights, Ken only his.
2.- Repeat N times:
    - Naomi chooses block.
    - Naomi tells Ken mass of the block. BUT IT CAN BE A LIE!!!
    - Ken chooses a block.
    - Whoever block weights more wins one point.
    - Both blocks are burned. Therefore, no repetitions allowed.
3.- Naomi knows that Ken will ALWAYS play optimal War strategy.

The key in this game is that Naomi can lie when telling the weight.
Basically, the key here is to lie so that Ken doesn't know it.

Goal: Predict Naomi score when both games are played perfectly by both parts.

Examples

If each player has a single block left, where Naomi has 0.5kg and Ken has 0.6kg,
then Ken is guaranteed to score the point. Naomi can't say her number is ≥ 0.6kg,
or Ken will know she isn't playing War when the balance scale shows his block was heavier.

If each player has two blocks left, where Naomi has [0.7kg, 0.2kg] and Ken has [0.8kg, 0.3kg],
then Naomi could choose her 0.2kg block, and deceive Ken by telling him that she chose a block
that was 0.6kg. Ken assumes Naomi is telling the truth (as in how the War game works) and
will play his 0.8kg block to score a point. Ken was just deceived, but he will never realize
it because the balance scale shows that his 0.8kg block is, like he expected, heavier than
the block Naomi played. Now Naomi can play her 0.7kg block, tell Ken it is 0.7kg, and score
a point. If Naomi had played War instead of Deceitful War, then Ken would have scored two
points and Naomi would have scored zero.

Input

The first line of the input gives the number of test cases, T. T test cases follow. Each test
case starts with a line containing a single integer N, the number of blocks each player has.
Next follows a line containing N space-separated real numbers: the masses of Naomi's blocks,
in kg. Finally there will be a line containing N space-separated real numbers: the masses of
Ken's blocks, in kg.

Each of the masses given to Ken and Naomi will be represented as a 0, followed by a decimal
point, followed by 1-5 digits. Even though all the numbers in the input have 1-5 digits after
the decimal point, Ken and Naomi don't know that; so Naomi can still tell Ken that she played
a block with mass 0.5000001kg, and Ken has no reason not to believe her.

Output

For each test case, output one line containing "Case #x: y z", where x is the test case number
(starting from 1), y is the number of points Naomi will score if she plays Deceitful War
optimally, and z is the number of points Naomi will score if she plays War optimally.


Sample Input
--------------------
4
1
0.5
0.6
2
0.7 0.2
0.8 0.3
3
0.5 0.1 0.9
0.6 0.4 0.3
9
0.186 0.389 0.907 0.832 0.959 0.557 0.300 0.992 0.899
0.916 0.728 0.271 0.520 0.700 0.521 0.215 0.341 0.458

Sample Output
-------------------
Case #1: 0 0
Case #2: 1 0
Case #3: 2 1
Case #4: 8 4

"""

from __future__ import division
import copy
from jam_utils.jam_parser import JamParser
from jam_utils.jam_solver import JamSolver

PATH_DATA = "data.txt"
PATH_OUTPUT = PATH_DATA.split(".")[0] + ".out"  # Same name as path data, except for the file format.


class DeceitfulWarInstance(object):
    def __init__(self):
        self.amount_blocks = None
        self.naomi = None
        self.ken = None


class DeceitfulWarParser(JamParser):
    def parse(self):
        """
        This method needs to fill the instances list.
        """
        # self.data is a list of rows. every row is a row of the input file
        # already split as str.
        # use self.get_data_as_type() to parse it to a different type if needed.
        data = self.get_data_as_type(float)
        for i in range(0, len(self.data), 3):
            instance = DeceitfulWarInstance()
            instance.amount_blocks = int(data[i][0])
            instance.naomi = data[i + 1]
            instance.ken = data[i + 2]
            self.instances.append(instance)


class DeceitfulWarSolver(JamSolver):

    def solve_instance(self, instance):
        war_result = self.calculate_war_result(instance)
        return "{0}".format(war_result)

    def calculate_war_result(self, instance):
        # Strategy:
        #   Choose heaviest naomi block and then:
        #       - Choose max ken block if he can beat that score.
        #       - Choose min ken block if he cannot beat the score.
        
        points = 0
        naomi = copy.copy(instance.naomi)
        ken = copy.copy(instance.ken)
        for i in range(instance.amount_blocks):
            chosen_naomi = max(naomi)

            can_ken_beat_that = chosen_naomi < max(ken)
            if can_ken_beat_that:
                naomi.remove(chosen_naomi)
                ken.remove(max(ken))
            else:
                naomi.remove(chosen_naomi)
                ken.remove(min(ken))
                points += 1

        return points


if __name__ == "__main__":
    parser = DeceitfulWarParser(PATH_DATA)
    solver = DeceitfulWarSolver(PATH_OUTPUT)
    solver.solve(parser.instances)