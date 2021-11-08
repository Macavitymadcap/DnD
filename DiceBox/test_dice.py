import unittest

from dice import d4
from dice import d6
from dice import d8
from dice import d10
from dice import d12
from dice import d20
from dice import d100
from dice import roll
from dice import roll_ability_scores
from dice import roll_advantage
from dice import roll_array
from dice import roll_crit
from dice import roll_d
from dice import roll_disadvantage
from dice import roll_string

class die_test(unittest.TestCase):
    """Class for testing the dx and roll functions."""
    def setUp(self) -> None:
        """Set up the variables used in tests"""
        self.standard_string = '1d20+2'
        self.crit_string = '2d6'
        self.crit_mod = '+2'
        self.array_string = '2d8+1'
        self.one_to_three = range(1, 4)
        self.one_to_four = range(1, 5)
        self.one_to_six = range(1, 7)
        self.one_to_eight = range(1, 9)
        self.one_to_ten = range(1, 11)
        self.one_to_twelve = range(1, 13)
        self.one_to_twenty = range(1, 21)
        self.one_to_one_hundred = range(1, 101)
        self.two_to_eight = range(2, 9)
        self.two_to_nine = range(2, 10)
        self.three_to_eighteen = range(3, 19)
        self.three_to_twenty_three = range(3, 24)
        self.six_to_twenty_six = range(6, 27)

    def test_range(self):
        """Test that the output of each roll function is in expected range."""
        d3_roll = roll_d(3)
        d4_roll = d4()
        d6_roll = d6()
        d8_roll = d8()
        d10_roll = d10()
        d12_roll = d12()
        d20_roll = d20()
        d100_roll = d100()
        mult_dice_roll = roll(2, d4)
        string_roll = roll_string(self.standard_string)
        crit_roll = roll_crit(self.crit_string, self.crit_mod)
        advantage_roll = roll_advantage(self.standard_string)
        disadvantage_roll = roll_disadvantage(self.standard_string)
        array_roll = roll_array(self.array_string)
        scores_roll = roll_ability_scores()

        self.assertIn(d3_roll, self.one_to_three)
        self.assertIn(d4_roll, self.one_to_four)
        self.assertIn(d6_roll, self.one_to_six)
        self.assertIn(d8_roll, self.one_to_eight)
        self.assertIn(d10_roll, self.one_to_ten)
        self.assertIn(d12_roll, self.one_to_twelve)
        self.assertIn(d20_roll, self.one_to_twenty)
        self.assertIn(d100_roll, self.one_to_one_hundred)
        self.assertIn(mult_dice_roll, self.two_to_eight)
        self.assertIn(string_roll, self.three_to_twenty_three)
        self.assertIn(crit_roll, self.six_to_twenty_six)
        self.assertIn(advantage_roll[0], self.three_to_twenty_three)
        self.assertIn(advantage_roll[1], self.three_to_twenty_three)
        self.assertIn(disadvantage_roll[0], self.three_to_twenty_three)
        self.assertIn(disadvantage_roll[1], self.three_to_twenty_three)
        self.assertIn(array_roll[0], self.two_to_nine)
        self.assertIn(array_roll[1], self.two_to_nine)
        self.assertIn(scores_roll[0], self.three_to_eighteen)
        self.assertIn(scores_roll[1], self.three_to_eighteen)
        self.assertIn(scores_roll[2], self.three_to_eighteen)
        self.assertIn(scores_roll[3], self.three_to_eighteen)
        self.assertIn(scores_roll[4], self.three_to_eighteen)
        self.assertIn(scores_roll[5], self.three_to_eighteen)

    def test_lists(self):
        """Test that array-based roll functions return lists."""
        advantage_roll = roll_advantage(self.standard_string)
        disadvantage_roll = roll_disadvantage(self.standard_string)
        array_roll = roll_array(self.array_string)
        scores_roll = roll_ability_scores()

        self.assertIsInstance(advantage_roll, list)
        self.assertIsInstance(disadvantage_roll, list)
        self.assertIsInstance(array_roll, list)
        self.assertIsInstance(scores_roll, list)
        

if __name__ == "__main__":
    unittest.main()