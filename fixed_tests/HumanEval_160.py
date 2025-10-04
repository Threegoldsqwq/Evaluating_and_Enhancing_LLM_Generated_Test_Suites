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