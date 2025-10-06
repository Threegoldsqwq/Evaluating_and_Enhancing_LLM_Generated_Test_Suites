# Evaluating_and_Enhancing_LLM_Generated_Test_Suites
Hello \o/, welcome to the experiment on using LLM to generate and improve test suites.

Here are the explanations of files inside this repository:

**test_generation.ipynb:** the file for part 1 (generating test cases and evaluating it). You can run the experiment, but don't forget to change the path when you run the code. \\
**iterative_enhancement.ipynb:** the file for generating solutions, fixing the tests and enhancing them. You can run the experiment, but don't forget to change the path when you run the code.

**canonical_solutions:** store canonical solutions (ground truth) got from HumanEval dataset.
**old_generated_solutions:** store the initial generated tests from LLM in part 1.
**generated_solutions:** store LLM generated solutions in part 2.
**fixed_tests:** store the tests that fixed by LLM in part 2.
**generated_tests:** store final enhanced tests (last step) in part 2.
**results:** store data in dataset during the experiment (e.g. validity rate, coverage, mutation score), details are in Explanation.txt.
**_test_runner.py:** the test runner used to run the tests, important in using tools (coverage and mutmut).
**.coverage and coverage.json:** cache file