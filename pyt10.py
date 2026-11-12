''' 
46. Filter Characters from a String You are given two strings: 
	 	A target string  
	 	A reference string  
Your task is to remove all characters from the target string that are present in the reference string. 
Return the resulting string after removal. 
 
Constraints: 
•	1 ≤ target.length ≤ 10⁵ 
•	1 ≤ reference.length ≤ 10⁵ 
•	Strings contain only lowercase English letters 
 
Example 1: 
Input: target = "programming" reference = "grm" Output: "poain" Explanation: 
Characters to remove: g, r, m 
"programming" → remove all g, r, m → "poain" 
 
Example 2: 
Input: target = "hello world" reference = "lo" Output: 
"he wrd" 
Explanation: 
Characters 'l' and 'o' are removed from the target string. 
 
Example 3: 
Input: 
target = "abcdef" reference = "xyz" Output: 
"abcdef" Explanation: 
No characters from the reference string are present in the target string, so the original string remains unchanged. 
'''


def filterCharacters(target, reference):
    ref = set(reference)
    result = ""

    for ch in target:
        if ch not in ref:
            result += ch

    return result

print(filterCharacters("programming", "grm"))
print(filterCharacters("hello world", "lo"))
print(filterCharacters("abcdef", "xyz"))



'''
47. Sum of Odd Numbers in a List 
You are given a list of integers containing both odd and even numbers. Your task is to calculate the sum of all odd numbers present in the list. 
Write a Python program to find the sum of all odd numbers in the given list using the following approaches: 
1.	Using a regular function parameter. 
2.	Using list comprehension. 
3.	Using a user-defined function. 
Given: An integer list nums containing positive and negative integers. 
Return: The sum of all odd numbers in the list. 
Constraints: 
	 	1 <= nums.length <= 100 
	 	-1000 <= nums[i] <= 1000 
 
Example 1: 
Input: 
nums = [1, 2, 3, 4, 5, 6] 
Output: 9 
Explanation: The odd numbers in the list are 1, 3, and 5. Sum = 1 + 3 + 5 = 9. 
 
Example 2: 
Input: nums = [10, 15, 20, 25, 30, 35] 
Output: 75 
Explanation: The odd numbers in the list are 15, 25, and 35. Sum = 15 + 25 + 35 = 75. 
 
Example 3: 
Input: 
nums = [2, 4, 6, 8] 
Output: 0 
Explanation: The list does not contain any odd numbers. Therefore, the sum is 0. 
'''

def sumOdd(nums):
    total = 0

    for num in nums:
        if num % 2 != 0:
            total += num

    return total

print(sumOdd([1, 2, 3, 4, 5, 6]))




'''
48. Palindrome Number Using a Decorator Function 
A decorator is a function that takes another function as an argument and extends its functionality without modifying its original code. 
Write a Python program to check whether a given integer is a palindrome number using a decorator function. 
A palindrome number is a number that remains the same when its digits are reversed. 
Given: An integer num representing a number. 
Return: Display whether the given number is a palindrome or not using a decorator function. Constraints: 
	 	0 <= num <= 109 
	 	The input must be a non-negative integer. 
 
Example 1: 
Input: num = 121 Output: 
121 is a Palindrome 
Explanation: The reverse of 121 is 121. Since the original number and its reverse are the same, it is a palindrome. 
 
Example 2: 
Input: 
num = 1234 Output: 
1234 is Not a Palindrome 
Explanation: The reverse of 1234 is 4321. Since the original number and its reverse are different, it is not a palindrome. 
'''

def palindromeDecorator(func):
    def wrapper(num):
        reverse = int(str(num)[::-1])

        if num == reverse:
            print(num, "is a Palindrome")
        else:
            print(num, "is Not a Palindrome")

        return func(num)

    return wrapper

@palindromeDecorator
def checkPalindrome(num):
    return num

checkPalindrome(121)
checkPalindrome(1234)

'''
49. Cumulative Average Using a Closure Function in Python 
A closure is a function that remembers and accesses variables from its enclosing function even after the enclosing function has finished execution. 
Write a Python program to calculate the cumulative average of numbers entered by the user one by one using a closure function. 
 
The program should: 
1.	Define an outer function that initializes an empty list. 
2.	Define an inner function that accepts a number as an argument. 
3.	Use the append() function to add each entered number to the list. 
4.	Calculate and display the cumulative average after every insertion. 
5.	Use the closure concept to retain the list and its values between function calls. 
 
Input: A sequence of integers entered by the user one at a time. 
Output: Display the cumulative average after each number is added. 
Constraints: 
	 	1 <= n <=100 
	 	-1000 <=num <=1000 
 
Example 1: Input: n =	4 
Enter number:	10 
Enter number:	20 
Enter number:	30 
Enter number:Output: 	40 

Cumulative Average: 10.0 
Cumulative Average: 15.0 
Cumulative Average: 20.0 
Cumulative Average: 25.0 Explanation: 
	 	After entering 10: Average = 10 / 1 = 10.0 
	 	After entering 20: Average = (10 + 20) / 2 = 15.0 
	 	After entering 30: Average = (10 + 20 + 30) / 3 = 20.0 
	 	After entering 40: Average = (10 + 20 + 30 + 40) / 4 = 25.0 
 
Example 2: 
Input: n = 3 
Enter number: 5 
Enter number: 15 
Enter number: 25 
Output: 
Cumulative Average: 5.0 
Cumulative Average: 10.0 
Cumulative Average: 15.0 
Note: The solution must use a closure function and the list append() method. 
'''

def cumulativeAverage():
    numbers = []

    def calculate(num):
        numbers.append(num)
        return sum(numbers) / len(numbers)

    return calculate

average = cumulativeAverage()

print("Cumulative Average:", average(10))
print("Cumulative Average:", average(20))
print("Cumulative Average:", average(30))
print("Cumulative Average:", average(40))




'''
50.	Remove Elements Greater Than 20 Using Decorator and Filter Problem Statement: 
Given a list of integers [5, 10, 23, 40, 8], write a Python program to remove all elements whose values are greater than 20 and return the filtered list. 
Implement the solution using a decorator function and Python's built-in filter() function. 
Requirements: 
1.	Define a user-defined function to filter the list elements. 
2.	Use a decorator to extend the functionality of the function. 
3.	Use the filter() function to select elements whose values are less than or equal to 20. 
4.	Return the resulting list after removing elements greater than 20. 
Constraint: 
	 	1 ≤ nums.length ≤ 100 
	 	0 ≤ nums[i] ≤ 1000 
	 	The solution must use both a decorator function and filter(). 
 
Input: 
nums = [5, 10, 23, 40, 8] Output: 
[5, 10, 8] 
Explanation: 
	 	5 ≤ 20 → Retained 
	 	10 ≤ 20 → Retained 
	 	23 > 20 → Removed 
	 	40 > 20 → Removed 
	 	8 ≤ 20 → Retained 
The resulting list is [5, 10, 8]. 
'''

def filterDecorator(func):
    def wrapper(nums):
        return list(filter(lambda x: x <= 20, func(nums)))

    return wrapper

@filterDecorator
def removeElements(nums):
    return nums

nums = [5, 10, 23, 40, 8]

print(removeElements(nums))