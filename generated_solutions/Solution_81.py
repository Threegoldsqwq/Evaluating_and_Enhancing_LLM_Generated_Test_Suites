def grade_equation(gpas):
    """
    Calculates a list of letter grades from a list of GPAs based on a given grading scale.

    Args:
        gpas (list): A list of floating-point numbers representing student GPAs.

    Returns:
        list: A list of strings representing the corresponding letter grades.
    """
    letter_grades = []

    for gpa in gpas:
        if gpa == 4.0:
            letter_grades.append('A+')
        elif gpa > 3.7:
            letter_grades.append('A')
        elif gpa > 3.3:
            letter_grades.append('A-')
        elif gpa > 3.0:
            letter_grades.append('B+')
        elif gpa > 2.7:
            letter_grades.append('B')
        elif gpa > 2.3:
            letter_grades.append('B-')
        elif gpa > 2.0:
            letter_grades.append('C+')
        elif gpa > 1.7:
            letter_grades.append('C')
        elif gpa > 1.3:
            letter_grades.append('C-')
        elif gpa > 1.0:
            letter_grades.append('D+')
        elif gpa > 0.7:
            letter_grades.append('D')
        elif gpa > 0.0:
            letter_grades.append('D-')
        elif gpa == 0.0: # Explicitly checking for 0.0 as the last defined threshold
            letter_grades.append('E')
        else:
            # Handle cases where GPA might be negative or undefined,
            # though typically GPAs are non-negative. Assigning 'E' for robustness.
            letter_grades.append('E')
            
    return letter_grades