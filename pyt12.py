r'''
56. Move All Zeros to the End of a List While Maintaining the Order of Non-Zero Elements

Problem Statement:

You are given a list of integers containing both zeros and non-zero elements. Your task is to move all zeros to the end of the list while maintaining the original relative order of the nonzero elements.

Write a Python program to rearrange the elements using list comprehension.

Your program should perform the following operations:

1. Initialize a list of integers containing zero and non-zero elements.
2. Use list comprehension to extract all non-zero elements from the original list.
3. Use another list comprehension to extract all zero elements.
4. Concatenate both lists to move all zeros to the end.
5. Display the resulting list.

Constraints:
• 1 ≤ len(l) ≤ 100
• List elements are integers.
• Maintain the original relative order of all non-zero elements.
• Use list comprehension to perform the rearrangement.

Input:
l = [0, 1, 0, 2, 0, 3]

Output:
[1, 2, 3, 0, 0, 0]

Explanation:
• Non-zero elements: [1, 2, 3]
• Zero elements: [0, 0, 0]
• Concatenate both lists to obtain [1, 2, 3, 0, 0, 0].

Example 2:

Input:
l = [4, 0, 5, 0, 2, 0, 8]

Output:
[4, 5, 2, 8, 0, 0, 0]
'''

# l = [0, 1, 0, 2, 0, 3]

# non_zero = [i for i in l if i != 0]

# zeros = [i for i in l if i == 0]

# result = non_zero + zeros

# print(result)

r'''
57. Student Performance Analyzer

Use multiple standard-library modules to build a small student performance analyzer.

Requirements:

Given student marks:

students = {
    "Tarun": [82, 91, 78],
    "Karthik": [65, 72, 68],
    "Chadrika": [91, 95, 89],
    "Trisha": [76, 81, 79],
    "Atul": [88, 84, 92]
}

The program should:

1. Calculate each student's average.
2. Find the highest average.
3. Randomly select one student.
4. Display the current date.
5. Use Counter to classify grades.
6. Use reduce() to calculate total marks.
'''

# import random
# from datetime import date
# from collections import Counter
# from functools import reduce

# students = {
#     "Mohan": [82, 91, 78],
#     "Arya": [65, 72, 68],
#     "A": [91, 95, 89],
#     "B": [76, 81, 79],
#     "C": [88, 84, 92]
# }

# averages = {}

# for name, marks in students.items():
#     total = reduce(lambda a, b: a + b, marks)
#     averages[name] = total / len(marks)

#     print(name, "Average:", averages[name])

# topper = max(averages, key=averages.get)

# print("Highest Average:", topper, averages[topper])

# selected = random.choice(list(students.keys()))

# print("Random Student:", selected)

# print("Current Date:", date.today())

# grades = []

# for avg in averages.values():
#     if avg >= 90:
#         grades.append("A")
#     elif avg >= 75:
#         grades.append("B")
#     elif avg >= 60:
#         grades.append("C")
#     else:
#         grades.append("D")

# print("Grade Classification:", Counter(grades))

# total_marks = reduce(
#     lambda a, b: a + b,
#     [mark for marks in students.values() for mark in marks]
# )

# print("Total Marks:", total_marks)

r'''
58. Automated Course Project Team Allocation

Imagine that your MCA department is organizing a semester-end industry-oriented project. There are 12 students from different departments:

• CSE students
• Data Science students
• AI students
• Cyber Security students

The department wants to automatically create project teams instead of manually assigning students.

Real-world situation:

The coordinator enters the required team size from the command line:

python allocation.py 3

Here, 3 means each project team should contain 3 students.

The program then performs the following operations:

1. Group students by department

• CSE students are grouped together.
• AI students are grouped together.
• Data Science students are grouped together.
• This can be handled using defaultdict.

2. Generate possible teams

The program generates different combinations of students.

For example, from 4 students:

(Anita, Rahul, Priya)
(Anita, Rahul, Kiran)
(Anita, Priya, Kiran)
(Rahul, Priya, Kiran)

itertools.combinations() is useful here.

3. Randomly select a team

• Instead of always selecting the first combination, the system randomly chooses a team.
• random.sample() can be used.

4. Calculate the team's total marks

Suppose the selected students have marks:

Anita → 85
Rahul → 78
Priya → 92

Total: 85 + 78 + 92 = 255

functools.reduce() performs this calculation.

5. Calculate average marks

Using the total and number of students:

Average = 255 / 3 = 85

math can be used for mathematical processing.

6. Record the allocation date

The system records when the team was created:

Allocation Date: 25-09-2026

datetime is used.

7. Accept team size from the command line

Instead of modifying the program every time, the coordinator enters:

python allocation.py 3

sys.argv retrieves 3.

Output:

===== PROJECT TEAM ALLOCATION =====

Team Size: 3

Allocation Date: 25-09-2026

Department: CSE

Selected Team:
1. Anita - 85
2. Rahul - 78
3. Priya - 92

Total Marks: 255
Average Marks: 85.00
'''

# import sys
# import random
# import math
# from datetime import datetime
# from collections import defaultdict
# from itertools import combinations
# from functools import reduce

# students = [
#     ("Mohan V", "CSE", 85),
#     ("Arya", "CSE", 78),
#     ("A", "CSE", 92),
#     ("B", "CSE", 80),
#     ("C", "AI", 88),
#     ("KarDthik", "AI", 75),
#     ("E", "AI", 90),
#     ("F", "AI", 82),
#     ("G", "Data Science", 95),
#     ("H", "Data Science", 84),
#     ("U", "Data Science", 89),
#     ("I", "Cyber Security", 79)
# ]

# team_size = int(sys.argv[1]) if len(sys.argv) > 1 else 3

# groups = defaultdict(list)

# for student in students:
#     groups[student[1]].append(student)

# print("===== PROJECT TEAM ALLOCATION =====")
# print("Team Size:", team_size)
# print("Allocation Date:", datetime.now().strftime("%d-%m-%Y"))

# for department, members in groups.items():

#     possible_teams = list(combinations(members, team_size))

#     if not possible_teams:
#         continue

#     selected_team = random.choice(possible_teams)

#     marks = [student[2] for student in selected_team]

#     total = reduce(lambda a, b: a + b, marks)

#     average = total / len(marks)

#     print("\nDepartment:", department)
#     print("Selected Team:")

#     for i, student in enumerate(selected_team, 1):
#         print(i, student[0], "-", student[2])

#     print("Total Marks:", total)
#     print("Average Marks:", round(average, 2))

r'''
59. Student Marks Management System

A university examination department wants to develop a Student Marks Management System to store student marks electronically.

The examination staff should be able to enter the student's name and marks. Since the data is entered manually, the system must handle possible errors and invalid inputs.

Requirements:

1. The student's name cannot be empty. Use an assert statement to validate the name.

2. The marks must be numeric. If the user enters a character or string such as ABC, the program should handle the ValueError.

3. Marks must be between 0 and 100.

4. Create a user-defined exception called InvalidMarksError.

5. If the marks are less than 0 or greater than 100, raise InvalidMarksError.

6. Valid student records should be stored in a file named student_records.txt.

7. The program should use try, except, and finally blocks to handle exceptions and ensure that the record-processing operation is completed.

8. The user should be allowed to enter details for multiple students using a loop.

9. After processing each student, ask whether the user wants to enter another record.

Develop a Python-based Student Marks Management System for a university examination department. The system should accept a student's name and marks, validate the input using assertions and exception handling, raise a user-defined exception for marks outside the range 0–100, store valid records in a text file, and allow multiple student records to be processed until the user chooses to exit.
'''

# class InvalidMarksError(Exception):
#     pass


# while True:

#     try:
#         name = input("Enter student name: ")

#         assert name.strip() != "", "Name cannot be empty"

#         marks = float(input("Enter marks: "))

#         if marks < 0 or marks > 100:
#             raise InvalidMarksError("Marks must be between 0 and 100")

#         with open("student_records.txt", "a") as f:
#             f.write(f"Name: {name}, Marks: {marks}\n")

#         print("Record saved successfully")

#     except AssertionError as e:
#         print("Error:", e)

#     except ValueError:
#         print("Error: Enter valid numeric marks")

#     except InvalidMarksError as e:
#         print("Error:", e)

#     finally:
#         print("Record processing completed")

#     choice = input("Do you want to add another record? (yes/no): ")

#     if choice.lower() != "yes":
#         break

# print("Student Marks Management System Closed")

r'''
60. Insert a Valid Integer into a NumPy Array Using Exception Handling

A smart industrial monitoring system stores numerical sensor readings, such as temperature values, in a NumPy array:

[10, 20, 30, 40, 50]

An operator needs to insert a new sensor reading at a specific position in the array. Since the system is designed to store only numerical integer values, the operator must not enter characters or text such as:

A
Hello
25.5

The system should validate the entered element using the isdigit() method.

Develop a Python program that:

1. Creates a NumPy array containing numerical sensor readings.

2. Displays the original array.

3. Accepts the insertion position from the user.

4. Accepts a new element as input.

5. Uses isdigit() to check whether the entered element contains only digits.

6. Raises a ValueError if the user enters a character, string, decimal value, or any non-digit input.

7. Checks whether the insertion position is valid.

8. Raises an IndexError for an invalid position.

9. Inserts the valid numerical element into the NumPy array.

10. Uses try, except, and finally blocks for exception handling.

A smart industrial monitoring system stores sensor readings in a NumPy array. Develop a Python program that allows an operator to insert a new sensor reading at a specified position. The program should ensure that only integer numerical values are inserted by validating the input using isdigit(). Handle invalid numerical input using ValueError and invalid insertion positions using IndexError. Display a completion message using the finally block.
'''

# import numpy as np

# arr = np.array([10, 20, 30, 40, 50])

# print("Original Array:", arr)

# try:
#     pos = int(input("Enter insertion position: "))

#     element = input("Enter new element: ")

#     if not element.isdigit():
#         raise ValueError("Only integer values are allowed")

#     if pos < 0 or pos > len(arr):
#         raise IndexError("Invalid insertion position")

#     arr = np.insert(arr, pos, int(element))

#     print("Updated Array:", arr)

# except ValueError as e:
#     print("Value Error:", e)

# except IndexError as e:
#     print("Index Error:", e)

# finally:
#     print("Program execution completed")


