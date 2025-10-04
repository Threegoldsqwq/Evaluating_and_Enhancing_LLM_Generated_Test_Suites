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

    def test_empty_extensions_list_raises_error(self):
            """
            Test that calling Strongest_Extension with an empty list of extensions
            raises a ValueError, covering the 'if not extensions:' branch.
            """
            class_name = "MyClass"
            extensions = []
            with self.assertRaisesRegex(ValueError, "Extensions list cannot be empty"):
                Strongest_Extension(class_name, extensions)

    def test_single_extension_list(self):
            """
            Test with only one extension in the list. This checks the initial
            strength calculation and ensures the loop is correctly skipped.
            """
            self.assertEqual(Strongest_Extension("App", ["BaseExt"]), "App.BaseExt")
            self.assertEqual(Strongest_Extension("Doc", ["API"]), "Doc.API")
            self.assertEqual(Strongest_Extension("Util", ["helper"]), "Util.helper")

    def test_tie_breaking_first_one_wins(self):
            """
            Test cases where multiple extensions have the same maximum strength.
            The function should return the first one encountered in the list.
            """
            # Both "AbC" and "XyZ" have strength (2-1)=1
            self.assertEqual(Strongest_Extension("TieBreaker", ["AbC", "XyZ", "pqr"]), "TieBreaker.AbC")
            # Both "A" and "B" have strength (1-0)=1
            self.assertEqual(Strongest_Extension("Alpha", ["A", "B", "c"]), "Alpha.A")
            # Both "a" and "b" have strength (0-1)=-1
            self.assertEqual(Strongest_Extension("Beta", ["a", "b", "C"]), "Beta.a")
            # Three extensions with strength 1
            self.assertEqual(Strongest_Extension("Gamma", ["Xyz", "AbC", "Pqr"]), "Gamma.Xyz")

    def test_extensions_with_non_alphabetic_chars(self):
            """
            Test that non-alphabetic characters are ignored in strength calculation.
            Strength should only consider uppercase and lowercase letters.
            """
            # "EXT-A": 4 uppercase (E,X,T,A), 0 lowercase. Strength = 4.
            # "Ext123": 1 uppercase (E), 2 lowercase (x,t). Strength = -1.
            # "e_x_t": 0 uppercase, 3 lowercase (e,x,t). Strength = -3.
            # "Strong!": 1 uppercase (S), 5 lowercase (t,r,o,n,g). Strength = -4.
            self.assertEqual(Strongest_Extension("Chars", ["Ext123", "e_x_t", "EXT-A", "Strong!"]), "Chars.EXT-A")

            # Another scenario
            # "P_Y_T_H_O_N": 6 uppercase, 0 lowercase. Strength = 6.
            # "j_a_v_a": 0 uppercase, 4 lowercase. Strength = -4.
            # "C++": 1 uppercase, 0 lowercase. Strength = 1.
            self.assertEqual(Strongest_Extension("Lang", ["C++", "j_a_v_a", "P_Y_T_H_O_N"]), "Lang.P_Y_T_H_O_N")

    def test_varied_strength_extensions(self):
            """
            Test a mix of extensions with positive, negative, and zero strengths.
            """
            # "UPPER": 5 uppercase, 0 lowercase. Strength = 5.
            # "lower": 0 uppercase, 5 lowercase. Strength = -5.
            # "MiXeD": 3 uppercase, 2 lowercase. Strength = 1.
            # "zero": 0 uppercase, 4 lowercase. Strength = -4.
            # "ZERo": 3 uppercase, 1 lowercase. Strength = 2.
            self.assertEqual(Strongest_Extension("Mix", ["lower", "MiXeD", "zero", "ZERo", "UPPER"]), "Mix.UPPER")

            # Test order dependency with mixed strengths
            self.assertEqual(Strongest_Extension("Mix2", ["ZERo", "MiXeD", "UPPER", "lower"]), "Mix2.UPPER")
            self.assertEqual(Strongest_Extension("Mix3", ["MiXeD", "ZERo", "UPPER", "lower"]), "Mix3.UPPER")

    def test_all_uppercase_extensions_multiple_max(self):
            """
            Test with multiple extensions all having maximum positive strength.
            Ensures the first one is chosen.
            """
            self.assertEqual(Strongest_Extension("UpperTest", ["AAA", "BBB", "CCC"]), "UpperTest.AAA")
            self.assertEqual(Strongest_Extension("UpperTest2", ["ZZZZ", "AAAA", "BBBB"]), "UpperTest2.ZZZZ")

    def test_all_lowercase_extensions_multiple_max(self):
            """
            Test with multiple extensions all having maximum negative strength (i.e., least negative).
            Ensures the first one is chosen.
            """
            self.assertEqual(Strongest_Extension("LowerTest", ["aaa", "bbb", "ccc"]), "LowerTest.aaa")
            self.assertEqual(Strongest_Extension("LowerTest2", ["zzz", "aaa", "bbb"]), "LowerTest2.zzz")
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)