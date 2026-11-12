r'''51. File and Directory Management Using Python's os and time Modules

You are developing a Python Assignment Management System to organize student assignments. Write a Python program using the built-in os and time modules to create directories, manage files, and retrieve file and directory information. Your program should perform the following operations:

1. Create Directories: Create a nested directory structure named My_Project/assignments/task1 using os.makedirs(). Ensure that the program does not generate an error if the directories already exist.

2. Display Directory Information: Display the current working directory using os.getcwd() and its byte-string representation using os.getcwdb().

3. Create and Write a File: Create a Python file named sample.py inside the task1 directory and write the statement print('Python Assignment') into it.

4. Check Directory: Verify whether the specified directory exists using os.path.isdir().

5. Calculate Total File Size: Use os.walk() to traverse the directory structure and calculate the total size of all files using os.path.getsize().

6. Retrieve File Timestamps: Retrieve the file's access time and last modification time using os.path.getatime() and os.path.getmtime(). Convert these timestamps into a readable format using time.ctime().

7. List Directory Contents: Display all files and directories present in the specified directory using os.listdir().

Note:
• Use appropriate functions from the os, os.path, and time modules.
• The file size and timestamps may vary depending on the system.
• The program should create the directory and file before retrieving their information.

Output:

Current Working Directory: C:\Users\Student
Byte String Format: b'C:\\Users\\Student'
True
total_size: 25 bytes
access time: ...
Last modified time: ...
list of files in the directory: ['sample.py']
'''

# import os
# import time

# path = "PYTHON code 3rd sem/assignments"

# os.makedirs(path, exist_ok=True)

# print("Current Working Directory:", os.getcwd())
# print("Byte String Format:", os.getcwdb())

# file_path = os.path.join(path, "sample.py")

# with open(file_path, "w") as f:
#     f.write("print('Python Assignment')")

# print(os.path.isdir(path))

# total_size = 0

# for root, dirs, files in os.walk("My_Project"):
#     for file in files:
#         total_size += os.path.getsize(os.path.join(root, file))

# print("total_size:", total_size, "bytes")

# print("access time:", time.ctime(os.path.getatime(file_path)))
# print("Last modified time:", time.ctime(os.path.getmtime(file_path)))

# print("list of files in the directory:", os.listdir(path))

r'''
52. CSV Data Cleaning and JSON File Conversion Using Python

You are given a CSV dataset containing employee information, including their names, ages, salaries, and joining dates. However, the dataset contains missing values, extra whitespace, and invalid entries.

Write a Python program using the built-in csv and json modules to clean the dataset, validate the records, and convert the cleaned data into a structured JSON file.

Given: A raw CSV dataset containing employee details.

Your program should perform the following operations:

1. Read CSV Data: Store the given CSV data as a multiline string and use split() to separate it into lines.

2. Read Records: Use csv.DictReader() to read the CSV data as dictionary records.

3. Remove Whitespace: Remove leading and trailing whitespace from all string fields using strip().

4. Handle Missing and Invalid Values: Skip records containing missing age or salary values, or salary values marked as "Unknown".

5. Type Conversion: Convert the age field into an integer using int() and the salary field into a floating-point number using float().

6. Handle Exceptions: Use try-except to handle ValueError exceptions that may occur during type conversion. Skip invalid records.

7. Reconstruct the Schema: Create a dictionary for each valid employee record with the keys name, age, salary, and join_date.

8. Store Cleaned Records: Append all valid employee records into a list named cleaned_records.

9. Generate JSON File: Use json.dump() to write the cleaned records into a file named cleaned_data.json with an indentation of 2 spaces.

Constraints:
• The input must be in CSV format.
• Age must be a valid integer.
• Salary must be a valid numeric value.
• Records with missing or invalid age/salary values must be skipped.
• The cleaned output must be stored in JSON format.

Input:

raw_data = """Name,Age,Salary,Join Date
Alice, 30, 95000, 2015-03-01
Bob, , 60000, 2018-07-15
Charlie, 35, Unknown, 2024-02-01
Diana, 40, 110000, 2021-11-03"""

Output:

The cleaned records should contain only valid employee entries.

Contents of cleaned_data.json:

[
  {
    "name": "Alice",
    "age": 30,
    "salary": 95000.0,
    "join_date": "2015-03-01"
  },
  {
    "name": "Diana",
    "age": 40,
    "salary": 110000.0,
    "join_date": "2021-11-03"
  }
]

Explanation:
• Alice: Valid record; retained.
• Bob: Age is missing; skipped.
• Charlie: Salary is "Unknown"; skipped.
• Diana: Valid record; retained.
'''

# import csv
# import json

# raw_data = """Name,Age,Salary,Join Date
# Alice, 30, 95000, 2015-03-01
# Bob, , 60000, 2018-07-15
# Charlie, 35, Unknown, 2024-02-01
# Diana, 40, 110000, 2021-11-03"""

# lines = raw_data.splitlines()

# reader = csv.DictReader(lines)

# cleaned_records = []

# for row in reader:
#     row = {k.strip(): v.strip() for k, v in row.items()}

#     if not row["Age"] or not row["Salary"] or row["Salary"] == "Unknown":
#         continue

#     try:
#         employee = {
#             "name": row["Name"],
#             "age": int(row["Age"]),
#             "salary": float(row["Salary"]),
#             "join_date": row["Join Date"]
#         }

#         cleaned_records.append(employee)

#     except ValueError:
#         continue

# with open("cleaned_data.json", "w") as f:
#     json.dump(cleaned_records, f, indent=2)

# print("Cleaned Records:")
# print(json.dumps(cleaned_records, indent=2))

# print("\nContents of cleaned_data.json:")

# with open("cleaned_data.json", "r") as f:
#     print(f.read())

r'''
53. Longest Substring Without Repeating Characters Using Sliding Window Technique

Problem Statement:

You are given a string s. Your task is to find the length of the longest substring that contains no repeating characters.

Write a Python program using the Sliding Window Technique and a Boolean visited array to identify the longest substring without duplicate characters.

Your program should perform the following operations:

1. Input: Read a string from the user.

2. Initialize Variables: Initialize two pointers, left and right, to represent the boundaries of the sliding window.

3. Visited Array: Create a Boolean array of size 26 to keep track of the characters present in the current window.

4. Expand the Window: Move the right pointer to include the next character in the substring.

5. Handle Repeated Characters: If a character is already present in the current window, move the left pointer forward and mark the removed characters as unvisited until the duplicate character is removed.

6. Calculate Maximum Length: Update the maximum substring length whenever a valid window is obtained.

7. Return Result: Display the length of the longest substring without repeating characters.

Input: A string s containing lowercase English alphabet characters.

Output: An integer representing the length of the longest substring without repeating characters.

Constraints:
• 0 ≤ s.length ≤ 105
• The string contains only lowercase English letters (a-z).
• The solution should use the sliding window technique.

Example 1:

Input:
s = "abcabcbb"

Output:
Length of the longest unique substring: 3

Explanation:
The longest substrings without repeating characters include "abc", "bca", and "cab". Their maximum length is 3.

Example 2:

Input:
s = "bbbbb"

Output:
Length of the longest unique substring: 1

Explanation:
Each character is repeated. Therefore, the longest substring without repeating characters is "b", with length 1.

Example 3:

Input:
s = "pwwkew"

Output:
Length of the longest unique substring: 3

Explanation:
The longest substring without repeating characters is "wke", with length 3.

Note: The program should return the length of the substring, not the substring itself.
'''

# s = input("Enter string: ")

# visited = [False] * 26

# left = 0
# max_length = 0

# for right in range(len(s)):
#     index = ord(s[right]) - ord('a')

#     while visited[index]:
#         left_index = ord(s[left]) - ord('a')
#         visited[left_index] = False
#         left += 1

#     visited[index] = True

#     max_length = max(max_length, right - left + 1)

# print("Length of the longest unique substring:", max_length)

r'''
54. Generator Function to Extract Vowels from a Given Name

Problem Statement:

Write a Python program to create a generator function that accepts a person's name as input and returns only the vowels present in the name.

Your program should perform the following operations:

1. Define a generator function named getvowels() that accepts a name as an argument.

2. Initialize a string containing all vowels (aeiouAEIOU).

3. Iterate through each character in the given name using a for loop.

4. Check whether each character is a vowel.

5. Use the yield statement to return only the vowel characters one at a time.

6. Call the generator function and display the vowels using a for loop.

Input:

Enter name: Priyanka

Output:

i
a
a

Explanation:

The given name is Priyanka.

P – Consonant (ignored)
r – Consonant (ignored)
i – Vowel (returned)
y – Consonant (ignored)
a – Vowel (returned)
n – Consonant (ignored)
k – Consonant (ignored)
a – Vowel (returned)
'''

# def getvowels(name):
#     vowels = "aeiouAEIOU"

#     for ch in name:
#         if ch in vowels:
#             yield ch


# name = input("Enter name: ")

# for vowel in getvowels(name):
#     print(vowel)

r'''
55. Create a User-Defined Iterator to Generate a Sequence of Decimal Values

Problem Statement:

Write a Python program to create a user-defined iterator that generates a sequence of decimal values starting from 0.0 and ending at 1.0 with an increment of 0.25.

The iterator should accept three parameters: start, stop, and step, and return all values in the specified range.

Your program should perform the following operations:

1. Define a class named NumberIterator.

2. Initialize the iterator with start = 0.0, stop = 1.0, and step = 0.25.

3. Implement the __iter__() method to return the iterator object.

4. Implement the __next__() method to generate the next decimal value.

5. Use StopIteration to terminate the iteration when the stopping condition is reached.

6. Display all generated values using a for loop.

Input:

start = 0.0
stop = 1.0
step = 0.25

Output:

0.0
0.25
0.5
0.75
1.0

Explanation:

• The sequence starts at 0.0.
• Each iteration increases the value by 0.25.
• The iterator generates values up to and including 1.0.
• Once the stopping condition is reached, StopIteration terminates the iterator.

Note: The solution must implement a user-defined iterator using __iter__() and __next__() methods.
'''

# class NumberIterator:

#     def __init__(self, start, stop, step):
#         self.start = start
#         self.stop = stop
#         self.step = step
#         self.current = start

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current > self.stop:
#             raise StopIteration

#         value = self.current
#         self.current = round(self.current + self.step, 10)

#         return value


# obj = NumberIterator(0.0, 1.0, 0.25)

# for num in obj:
#     print(num)

