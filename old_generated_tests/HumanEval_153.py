import unittest

# Assume Strongest_Extension function is defined elsewhere, for example:
# def Strongest_Extension(class_name, extensions):
#     def calculate_strength(ext_name):
#         cap = sum(1 for char in ext_name if 'A' <= char <= 'Z')
#         sm = sum(1 for char in ext_name if 'a' <= char <= 'z')
#         return cap - sm
    
#     if not extensions:
#         # The problem statement implies extensions list will not be empty,
#         # or this scenario should be handled based on specific requirements
#         # (e.g., raise an error, return a specific string).
#         # For the purpose of generating test cases, we assume non-empty list.
#         raise ValueError("Extensions list cannot be empty.")
    
#     strongest_ext = extensions[0]
#     max_strength = calculate_strength(strongest_ext)
    
#     for i in range(1, len(extensions)):
#         ext = extensions[i]
#         current_strength = calculate_strength(ext)
#         if current_strength > max_strength:
#             max_strength = current_strength
#             strongest_ext = ext
#     return f"{class_name}.{strongest_ext}"

class TestStrongestExtension(unittest.TestCase):

    # Test Case 1: Example from the problem description
    def test_example_one(self):
        # Strengths: SErviNGSliCes (5-8=-3), Cheese (1-5=-4), StuFfed (2-5=-3)
        # 'SErviNGSliCes' and 'StuFfed' both have -3 strength. 'SErviNGSliCes' comes first.
        self.assertEqual(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']), 'Slices.SErviNGSliCes')

    # Test Case 2: Second example from the problem description
    def test_example_two(self):
        # Strengths: AA (2-0=2), Be (1-1=0), CC (2-0=2)
        # 'AA' and 'CC' both have 2 strength. 'AA' comes first.
        self.assertEqual(Strongest_Extension('my_class', ['AA', 'Be', 'CC']), 'my_class.AA')

    # Test Case 3: Extensions with mixed casing, clear strongest
    def test_mixed_cases_clear_winner(self):
        # Strengths: Reader (1-5=-4), WRITER (6-0=6), processor (0-9=-9)
        self.assertEqual(Strongest_Extension('DataProcessor', ['Reader', 'WRITER', 'processor']), 'DataProcessor.WRITER')

    # Test Case 4: Tie-breaking with equal strongest extensions, first in list wins
    def test_tie_breaking_first_occurrence(self):
        # Strengths: First (1-4=-3), Second (1-5=-4), Third (1-4=-3)
        # 'First' and 'Third' both have -3 strength. 'First' comes first.
        self.assertEqual(Strongest_Extension('TieBreaker', ['First', 'Second', 'Third']), 'TieBreaker.First')

    # Test Case 5: List with only one extension
    def test_single_extension(self):
        # Strength: AuthService (2-9=-7)
        self.assertEqual(Strongest_Extension('Authenticator', ['AuthService']), 'Authenticator.AuthService')

    # Test Case 6: Extensions containing non-alphabetic characters (should be ignored for strength calculation)
    def test_non_alphabetic_characters(self):
        # Strengths:
        # File_Handler_V1: (F,H,V=3) - (i,l,e,a,n,d,l,e,r=9) = -6 (Note: V1 doesn't count '1')
        # Cache.Manager: (C,M=2) - (a,c,h,e,a,n,a,g,e,r=10) = -8
        # Net_Worker-2: (N,W=2) - (e,t,o,r,k,e,r=7) = -5
        # 'Net_Worker-2' is strongest.
        self.assertEqual(Strongest_Extension('Filesystem', ['File_Handler_V1', 'Cache.Manager', 'Net_Worker-2']), 'Filesystem.Net_Worker-2')

    # Test Case 7: All extensions result in negative strength (more lowercase than uppercase)
    def test_all_negative_strengths(self):
        # Strengths:
        # dailyreport: (0-11=-11)
        # monthlyReport: (R=1)-(m,o,n,t,h,l,y,e,p,o,r,t=12) = -11
        # yearly_report: (0-11=-11)
        # All three have strength -11. 'dailyreport' comes first.
        self.assertEqual(Strongest_Extension('Report', ['dailyreport', 'monthlyReport', 'yearly_report']), 'Report.dailyreport')

    # Test Case 8: All extensions result in positive strength (more uppercase than lowercase), with a tie
    def test_all_positive_strengths_with_tie(self):
        # Strengths: CPU (3-0=3), GPU (3-0=3), TPU (3-0=3)
        # All equal, 'CPU' comes first.
        self.assertEqual(Strongest_Extension('Processor', ['CPU', 'GPU', 'TPU']), 'Processor.CPU')

    # Test Case 9: Extensions with zero strength, mixed with other strengths, and tie-breaking
    def test_zero_strength_and_tie_breaking(self):
        # Strengths:
        # Ab (1-1=0)
        # aB (1-1=0)
        # CD (2-0=2)
        # eF (1-1=0)
        # 'CD' is strongest.
        self.assertEqual(Strongest_Extension('ZeroBalance', ['Ab', 'aB', 'CD', 'eF']), 'ZeroBalance.CD')

    # Test Case 10: Complex mix of positive, negative, and zero strengths
    def test_complex_mix_of_strengths(self):
        # Strengths:
        # API_Gateway: (A,P,I,G=4) - (a,t,e,w,a,y=6) = -2
        # dataService: (S=1) - (d,a,t,a,s,e,r,v,i,c,e=11) = -10
        # Configurator: (C=1) - (o,n,f,i,g,u,r,a,t,o,r=11) = -10
        # LOG_MANAGER: (L,O,G,M,A,N,A,G,E,R=10) - (0) = 10
        # 'LOG_MANAGER' is clearly the strongest.
        self.assertEqual(Strongest_Extension('ComplexApp', ['API_Gateway', 'dataService', 'Configurator', 'LOG_MANAGER']), 'ComplexApp.LOG_MANAGER')

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)