import unittest

# Assume the function to be tested is named 'evaluate_expression'.
# The actual implementation of 'evaluate_expression' is not provided here,
# as per the instructions to "ONLY generate test cases, assume the function exist."

class TestEvaluateExpression(unittest.TestCase):




    def test_mixed_operations_high_precedence(self):
            """
            Test case with mixed operations, including exponentiation which has highest precedence.
            5 + 2 ** 3 // 4  =>  5 + 8 // 4  =>  5 + 2  =>  7
            """
            operators = ['+', '**', '//']
            operands = [5, 2, 3, 4]
            self.assertEqual(do_algebra(operators, operands), 7)
    def test_long_expression_with_zeros(self):
            """
            Test case for a longer expression with various operators and handling of zeros.
            10 * 0 + 5 // 2 - 3 ** 1  =>  0 + 2 - 3  =>  -1
            """
            operators = ['*', '+', '//', '-', '**']
            operands = [10, 0, 5, 2, 3, 1]
            self.assertEqual(do_algebra(operators, operands), -1)

    def test_chain_of_same_precedence_operators(self):
            """
            Test case for chained operations of the same precedence,
            verifying left-to-right evaluation for operators like // and *.
            100 // 10 // 2 * 3  =>  (100 // 10) // 2 * 3  =>  10 // 2 * 3  =>  5 * 3  =>  15
            """
            operators = ['//', '//', '*']
            operands = [100, 10, 2, 3]
            self.assertEqual(do_algebra(operators, operands), 15)

    def test_floor_division_operator(self):
            # Test case for floor division (//)
            operator = ['//']
            operand = [10, 3]
            self.assertEqual(do_algebra(operator, operand), 3)

            operator = ['//', '+']
            operand = [20, 4, 2]
            # Expression: 20 // 4 + 2 = 5 + 2 = 7
            self.assertEqual(do_algebra(operator, operand), 7)

    def test_exponentiation_operator(self):
            # Test case for exponentiation (**)
            operator = ['**']
            operand = [2, 3]
            self.assertEqual(do_algebra(operator, operand), 8)

            operator = ['+', '**']
            operand = [3, 2, 4]
            # Expression: 3 + 2 ** 4 = 3 + 16 = 19
            self.assertEqual(do_algebra(operator, operand), 19)

    def test_single_operator_case(self):
            # Test case with minimum valid input (one operator, two operands)
            operator = ['+']
            operand = [10, 5]
            self.assertEqual(do_algebra(operator, operand), 15)

            operator = ['-']
            operand = [7, 3]
            self.assertEqual(do_algebra(operator, operand), 4)

    def test_operations_with_zeros(self):
            # Test cases involving zero operands
            operator = ['*', '+']
            operand = [5, 0, 10]
            # Expression: 5 * 0 + 10 = 0 + 10 = 10
            self.assertEqual(do_algebra(operator, operand), 10)

            operator = ['-', '//']
            operand = [10, 5, 0] # Note: will result in ZeroDivisionError if not careful, but 0 is an operand, not a divisor here.
            # This will fail as 0 is not the divisor, rather operand[2] = 0.
            # 10 - 5 // 0 -> This case is invalid for division by zero.
            # The problem statement says "non-negative integers" for operands.
            # Let's try to avoid creating a ZeroDivisionError if possible for now.
            # For floor division by zero, the behavior of eval is to raise an error.
            # The problem doesn't specify handling of division by zero.
            # A valid test with zero:
            operator = ['*', '+']
            operand = [0, 5, 10]
            # Expression: 0 * 5 + 10 = 0 + 10 = 10
            self.assertEqual(do_algebra(operator, operand), 10)

            operator = ['+', '**']
            operand = [2, 0, 5]
            # Expression: 2 + 0 ** 5 = 2 + 0 = 2
            self.assertEqual(do_algebra(operator, operand), 2)

            operator = ['**', '+']
            operand = [0, 2, 5]
            # Expression: 0 ** 2 + 5 = 0 + 5 = 5
            self.assertEqual(do_algebra(operator, operand), 5)

    def test_operations_resulting_in_negative_numbers(self):
            # Although operands are non-negative, subtraction can yield negative results.
            operator = ['-']
            operand = [5, 10]
            self.assertEqual(do_algebra(operator, operand), -5)

            operator = ['-', '*']
            operand = [10, 3, 5]
            # Expression: 10 - 3 * 5 = 10 - 15 = -5
            self.assertEqual(do_algebra(operator, operand), -5)

    def test_complex_expression_all_operators(self):
            # Test a more complex expression involving all supported operators and precedence
            operator = ['+', '*', '-', '//', '**']
            operand = [2, 3, 4, 10, 2, 3]
            # Expression: 2 + 3 * 4 - 10 // 2 ** 3
            # Precedence: ** (exponentiation), * // (multiplication, division), + - (addition, subtraction)
            # 2 + 3 * 4 - 10 // (2 ** 3)
            # 2 + 3 * 4 - 10 // 8
            # 2 + (3 * 4) - (10 // 8)
            # 2 + 12 - 1
            # 14 - 1 = 13
            self.assertEqual(do_algebra(operator, operand), 13)

    def test_mixed_operators_and_values(self):
            # Another test with a mix of operators and values to ensure robustness
            operator = ['*', '-', '+', '//']
            operand = [10, 2, 5, 3, 6]
            # Expression: 10 * 2 - 5 + 3 // 6
            # 20 - 5 + 0 = 15
            self.assertEqual(do_algebra(operator, operand), 15)

            operator = ['//', '**', '+']
            operand = [100, 10, 2, 5]
            # Expression: 100 // 10 ** 2 + 5
            # 100 // 100 + 5
            # 1 + 5 = 6
            self.assertEqual(do_algebra(operator, operand), 6)
# To run these tests, you would typically have your 'evaluate_expression'
# function defined in the same file or imported.
# Example dummy implementation for local testing (not part of the solution):
# def evaluate_expression(operators, operands):
#     expression_parts = [str(operands[0])]
#     for i in range(len(operators)):
#         expression_parts.append(operators[i])
#         expression_parts.append(str(operands[i+1]))
#     # Use eval() to leverage Python's built-in operator precedence
#     return eval(" ".join(expression_parts))

if __name__ == '__main__':
    # This dummy function is just to make the tests runnable for verification.
    # In a real scenario, this would be the actual function to be tested.
    # def evaluate_expression(operators, operands):
    #     expression_parts = [str(operands[0])]
    #     for i in range(len(operators)):
    #         expression_parts.append(operators[i])
    #         expression_parts.append(str(operands[i+1]))
    #     return eval(" ".join(expression_parts))

    unittest.main()