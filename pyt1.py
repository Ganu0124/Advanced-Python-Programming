r''' 1.	Single Number: Given a non-empty array of integers nums, every element appears twice except for one. Find that single one. You must implement a solution with a linear runtime complexity and use only constant extra space. 
 
Constraints: 
•	1 <= nums.length <= 3 * 104 
•	-3 * 104 <= nums[i] <= 3 * 104 
•	Each element in the array appears twice except for one element which appears only once. 
  
Example 1: 
Input: nums = [2,2,1] 
Output: 1 
 
Example 2: 
Input: nums = [4,1,2,1,2] 
Output: 4 
 
Example 3: 
Input: nums = [1] 
Output: 1 
'''
# def singleNumber(nums):
#     result = 0
#     for num in nums:
#         result ^= num
#     return result

# nums = [4,4, -1,1, 2, 1, 2]
# print(singleNumber(nums))

r''' 2.	Find Palindromes in a Given Range 
•	You are given two integers m and n representing a range. 
•	Your task is to find and return all numbers within the range [m, n] that are palindromes. 
•	A number is a palindrome if it reads the same forward and backward. 
Constraints: 
•	0 ≤ m ≤ n ≤ 10⁶ 
 
Example 1: 
Input: m = 10, n = 50 
Output: [11, 22, 33, 44] Explanation: 
These numbers remain the same when reversed. 
 
Example 2: 
Input: m = 100, n = 150 Output: [101, 111, 121, 131, 141] Explanation: 
Each number reads the same from both directions. 
 
Example 3: 
Input: m = 1, n = 9 Output: [1,2,3,4,5,6,7,8,9] Explanation: 
All single-digit numbers are palindromes. 
''' 

# def findPalindromes(m, n):
#     result = []

#     for i in range(m, n + 1):
#         num = i
#         rev = 0

#         while num > 0:
#             digit = num % 10
#             rev = rev * 10 + digit
#             num //= 10

#         if i == rev:
#             result.append(i)

#     return result


# m = 10
# n = 50

# print(findPalindromes(m, n))


r''' 3. Regular Expression Matching 
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where: 
•	'.' Matches any single character. 
•	'*' Matches zero or more of the preceding elements. 
Return a boolean indicating whether the matching covers the entire input string (not partial). 
 
Constraints: 
•	1 <= s.length <= 20 
•	1 <= p.length <= 20 
•	s contains only lowercase English letters. 
•	p contains only lowercase English letters, '.', and '*'. 
•	It is guaranteed for each appearance of the character '*', there will be a previous valid character to match. 
  
Example 1: 
Input: s = "abcd" 
p = ".*" Output: true 
Explanation: 
'.' matches any character, '' allows repetition. So "." can match any string, including "abcd". 
 
Example 2: 
Input: 
s = "mississippi" p = "misisp*." Output: false Explanation: 
The pattern fails to fully match the string due to incorrect placement of '*'. 
 
Example 3: 
Input: s = "aa" p = "a" Output: false 
Explanation:  
"a" does not match the entire string "aa". 
'''

# def isMatch(s, p):

#     def check(i, j):

#         if j == len(p):
#             return i == len(s)

#         match = i < len(s) and (s[i] == p[j] or p[j] == '.')

#         if j + 1 < len(p) and p[j + 1] == '*':
#             return check(i, j + 2) or (match and check(i + 1, j))

#         return match and check(i + 1, j + 1)

#     return check(0, 0)


# print(isMatch("abcd", ".*"))
# print(isMatch("mississippi", "misisp*."))
# print(isMatch("aa", "a"))

r''' 4. Decode Ways with Pattern Generation 
You have intercepted a secret message encoded as a string s containing only digits. 
The message is decoded using the mapping: 
	• 	"1" → 'A', "2" → 'B', …, "26" → 'Z'  
A message can be decoded in multiple ways because: 
•	A single digit can map to a letter  
•	Two digits together can also form a valid letter (if between 10 and 26)  Your Task: 
1.	Compute the total number of ways to decode the string  
2.	Also print all possible decoded strings (patterns)  A decoding is valid only if: 
•	No segment starts with '0'  
•	Valid numbers are from 1 to 26 only  
Constraints: 
•	1 ≤ s.length ≤ 100 
•	s contains only digits 
•	Output fits in 32-bit integer 
 
Input: s = "12" Output: 
Total Ways: 2 Decoded Strings: 
 	AB 
 	L 
Explanation: 
Possible groupings: 
•	"1" + "2" → A B → AB  
•	"12" → L → L  
Total = 2 
 
Example 2: Input: s = "226" Output: 
Total Ways: 3 Decoded Strings: 
 	BBF 
 	BZ 
 	VF 
Explanation: 
•	"2" + "2" + "6" → B B F → BBF  
•	"2" + "26" → B Z → BZ  
•	"22" + "6" → V F → VF  
Total = 3 
 
Example 3: Input: s = "11106" Output: 
Total Ways: 2 
Decoded Strings: 
 	AAJF 
 	KJF 
Explanation: 
Valid decodings: 
•	(1,1,10,6) → A A J F → AAJF  
•	(11,10,6) → K J F → KJF  Invalid: 
•	(1,11,06) →   "06" not valid  
 
Example 4 (Invalid Case): 
Input: s = "06" Output: 
Total Ways: 0 Decoded Strings: 
None 
Explanation: 
•	"06" is invalid because leading zero is not allowed 
''' 

# def decode(s):
#     result = []

#     def backtrack(i, current):

#         if i == len(s):
#             result.append(current)
#             return

#         if s[i] == '0':
#             return

#         num = int(s[i])
#         backtrack(i + 1, current + chr(64 + num))

      
#         if i + 1 < len(s):
#             num = int(s[i:i+2])

#             if 10 <= num <= 26:
#                 backtrack(i + 2, current + chr(64 + num))

#     backtrack(0, "")

#     print("Total Ways:", len(result))
#     print("Decoded Strings:")

#     if result:
#         for word in result:
#             print(word)
#     else:
#         print("None")


# decode("226")

r'''5. 5.	Balanced Binary Tree 
Given a binary tree, determine if it is height-balanced. 
 Constraints: 
•	The number of nodes in the tree is in the range [0, 5000]. 
•	-104 <= Node.val <= 104 
 
Example 1: 
  
Input: root = [3, 9, 20, null, null, 15, 7] 
Output: true 
 
Example 2: 
  
Input: root = [1, 2, 2, 3, 3, null, null, 4, 4] 
Output: false 
 
Example 3: 
Input: root = [4] 
Output: true 
#  '''
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


# def isBalanced(root):

#     def height(node):
#         if node is None:
#             return 0

#         left = height(node.left)
#         right = height(node.right)

#         if abs(left - right) > 1:
#             return -1

#         if left == -1 or right == -1:
#             return -1

#         return 1 + max(left, right)

#     return height(root) != -1


# # Example 1
# root = Node(3)
# root.left = Node(9)
# root.right = Node(20)
# root.right.left = Node(15)
# root.right.right = Node(7)

# print(isBalanced(root))