import unittest

# Assume the function 'grade_equation' is defined elsewhere.
# For demonstration purposes in a test file, one might include a placeholder:
# def grade_equation(gpas):
#     # This is a placeholder/mock implementation for testing setup.
#     # The actual implementation is what needs to be tested.
#     grades = []
#     for gpa in gpas:
#         if gpa == 4.0:
#             grades.append('A+')
#         elif gpa > 3.7:
#             grades.append('A')
#         elif gpa > 3.3:
#             grades.append('A-')
#         elif gpa > 3.0:
#             grades.append('B+')
#         elif gpa > 2.7:
#             grades.append('B')
#         elif gpa > 2.3:
#             grades.append('B-')
#         elif gpa > 2.0:
#             grades.append('C+')
#         elif gpa > 1.7:
#             grades.append('C')
#         elif gpa > 1.3:
#             grades.append('C-')
#         elif gpa > 1.0:
#             grades.append('D+')
#         elif gpa > 0.7:
#             grades.append('D')
#         elif gpa > 0.0:
#             grades.append('D-')
#         elif gpa == 0.0:
#             grades.append('E')
#         else: # Handle potentially negative or invalid GPAs gracefully, though problem implies non-negative.
#             grades.append('INVALID') # Or raise an error
#     return grades


class TestGradeEquation(unittest.TestCase):

    def test_example_case(self):
        # Test case provided in the problem description
        input_gpas = [4.0, 3.0, 1.7, 2.0, 3.5]
        expected_grades = ['A+', 'B', 'C-', 'C', 'A-']
        self.assertEqual(grade_equation(input_gpas), expected_grades)

    def test_all_a_grades_and_boundary(self):
        # Test A+, A, A- grades including boundary values
        input_gpas = [4.0, 3.9, 3.71, 3.7, 3.5, 3.31, 3.3]
        expected_grades = ['A+', 'A', 'A', 'A-', 'A-', 'A-', 'B+']
        self.assertEqual(grade_equation(input_gpas), expected_grades)

    def test_all_b_grades_and_boundary(self):
        # Test B+, B, B- grades including boundary values
        input_gpas = [3.1, 3.0, 2.8, 2.7, 2.4, 2.3]
        expected_grades = ['B+', 'B', 'B', 'B-', 'B-', 'C+']
        self.assertEqual(grade_equation(input_gpas), expected_grades)

    def test_all_c_grades_and_boundary(self):
        # Test C+, C, C- grades including boundary values
        input_gpas = [2.1, 2.0, 1.8, 1.7, 1.4, 1.3]
        expected_grades = ['C+', 'C', 'C', 'C-', 'C-', 'D+']
        self.assertEqual(grade_equation(input_gpas), expected_grades)

    def test_all_d_and_e_grades_and_boundary(self):
        # Test D+, D, D- and E grades including boundary values
        input_gpas = [1.1, 1.0, 0.8, 0.7, 0.1, 0.0]
        expected_grades = ['D+', 'D', 'D', 'D-', 'D-', 'E']
        self.assertEqual(grade_equation(input_gpas), expected_grades)

    def test_empty_list(self):
        # Test an empty list of GPAs
        input_gpas = []
        expected_grades = []
        self.assertEqual(grade_equation(input_gpas), expected_grades)

    def test_single_gpa_max_min(self):
        # Test a list with a single GPA at maximum and minimum valid points
        input_gpas = [4.0, 0.0]
        expected_grades = ['A+', 'E']
        self.assertEqual(grade_equation(input_gpas), expected_grades)

    def test_gpas_just_above_thresholds(self):
        # Test values infinitesimally greater than each threshold to ensure '>' logic
        input_gpas = [3.7000001, 3.3000001, 3.0000001, 2.7000001, 2.3000001,
                      2.0000001, 1.7000001, 1.3000001, 1.0000001, 0.7000001, 0.0000001]
        expected_grades = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-']
        self.assertEqual(grade_equation(input_gpas), expected_grades)

    def test_all_integer_gpas(self):
        # Test a list where all GPAs are integers (common input)
        input_gpas = [4.0, 3.0, 2.0, 1.0, 0.0]
        expected_grades = ['A+', 'B', 'C', 'D', 'E']
        self.assertEqual(grade_equation(input_gpas), expected_grades)

    def test_mixed_random_gpas(self):
        # Test a comprehensive mix of GPAs, including some in between explicit thresholds
        input_gpas = [2.5, 0.5, 3.2, 1.5, 3.95, 0.9, 1.9, 2.9, 0.0, 4.0]
        expected_grades = ['B-', 'D-', 'B+', 'C-', 'A', 'D', 'C', 'B', 'E', 'A+']
        self.assertEqual(grade_equation(input_gpas), expected_grades)