from solution_calc import MathematicalError, parse_input, calculate
import unittest

input_values_1 = "2 +"
input_values_2 = "a + b"
input_values_3 = "2 ' 2"
input_values_4 = "2.2 + 2.2"


class TestCalcSolution(unittest.TestCase):
    def test_calculator_1(self):
        with self.assertRaises(MathematicalError) as context:
            parse_input(input_values_1)
        self.assertEqual(
            str(context.exception),
            'Input does not consist of three elements'
        )

    def test_calculator_2(self):
        with self.assertRaises(MathematicalError) as context:
            parse_input(input_values_2)
        self.assertEqual(
            str(context.exception),
            'The first and third input value must be numbers'
        )

    def test_calculator_3(self):
        with self.assertRaises(MathematicalError) as context:
            parse_input(input_values_3)
        self.assertEqual(
            str(context.exception),
            'Invalid operator. Can only use "+" or "-"'
        )

    def test_assertEqual(self):
        """Fail if the two objects are unequal as determined by the '=='
           operator.
        """
        value = parse_input(input_values_4)
        self.first = calculate(float(value[0]), value[1], float(value[2]))
        self.second = 4.4
        self.assertEqual(self.first, self.second)
        #assertion_func = self._getAssertEqualityFunc(self.first, self.second)
        #assertion_func(self.first, self.second)
