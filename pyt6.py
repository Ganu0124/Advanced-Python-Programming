''' 
26. Sum of unique elements 
Given an array of integers, find the sum of unique elements in the array. An element is considered unique if it appears only once in the array. In addition to the sum, also print the elements that contributed to the sum. 
 
Example 1: 
Input: array = [1, 3, 2, 3, 2, 4] Output:  
Unique Elements: 1 4 Sum: 5 Explanation: 
	 	Elements appearing once: 1 and 4  
	 	Elements appearing more than once: 2 and 3  
Sum = 1 + 4 = 5 
 
Example 2: 
Input: array = [10, 20, 10, 30, 40, 30] Output: 
Unique Elements: 20 40 Sum: 60 Explanation: 
	 	Unique elements: 20 and 40  
	 	Repeated elements: 10 and 30  
Sum = 20 + 40 = 60 
 
Example 3: 
Input: array = [5, 5, 5, 5] Output: 
Unique Elements: None Sum: 0 Explanation: 
	 	No element appears exactly once  
	 	All elements are repeated  
Sum = 0 
'''

# from collections import Counter

# def sumOfUnique(nums):
#     freq = Counter(nums)
#     unique = [num for num in nums if freq[num] == 1]

#     print("Unique Elements:", *unique if unique else ["None"])
#     print("Sum:", sum(unique))

# sumOfUnique([1, 3, 2, 3, 2, 4])



'''
27.	Invert Binary Tree: Given the root of a binary tree, invert the tree, and return 	. 
 Constraints: 
	 	The number of nodes in the tree is in the range [0, 100]. 
	 	-100 <= Node.val <= 100 
 
Example 1: 
  
Input: root = [4,2,7,1,3,6,9] 
Output: [4,7,2,9,6,3,1] 
 
Example 2: 
  
Input: root = [2,1,3] 
Output: [2,3,1] 
 
28.	Valid Anagram 
You are given two strings: s and t  
Your task is to determine whether t is an anagram of s. 
 
An anagram is a word or phrase formed by: 
	 	Rearranging the letters of another word 
	 	Using all original characters exactly once 
Without adding or removing any characters 
 
Examples of Anagrams: 
	 	"listen" 	 "silent"  
	 	"triangle" 	 "integral"  
	 	"anagram" 	 "nagaram"  
 
Not Anagrams: 
	 	"rat" 	 "car" (different letters)  
	 	"hello" 	 "helloo" (extra character)  
 
Constraints: 
•	1 ≤ s.length, t.length ≤ 5 × 10⁴ 
•	Strings contain only lowercase English letters 
 
Example 1: 
Input: 
s = "anagram" t = "nagaram" Output: true 
Explanation: 
Count characters in both strings: 
Character 	s Count 	t Count
a 	3 	3 
n 	1 	1 
g 	1 	1 
r 	1 	1 
m 	1 	1 
All characters match exactly 
Therefore, "nagaram" is an anagram of "anagram" 
 
Example 2: Input: s = "rat" t = "car" Output: false Explanation: 
Compare characters:  	s → r, a, t   	t → c, a, r  
 Character 't' is missing 
 Character 'c' is extra 
 Not the same set of characters 
 Hence, not an anagram 
'''



# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

# def invertTree(root):
#     if root is None:
#         return None

#     root.left, root.right = root.right, root.left

#     invertTree(root.left)
#     invertTree(root.right)

#     return root

# def levelOrder(root):
#     if root is None:
#         return []

#     queue = [root]
#     result = []

#     while queue:
#         node = queue.pop(0)
#         result.append(node.val)

#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)

#     return result

# root = Node(4)
# root.left = Node(2)
# root.right = Node(7)
# root.left.left = Node(1)
# root.left.right = Node(3)
# root.right.left = Node(6)
# root.right.right = Node(9)

# invertTree(root)
# print(levelOrder(root))



'''
29. Happy Number:  
Write a program to determine if a number n is happy. 
A happy number is a number defined by the following process: 
 	Starting with any positive integer, replace the number by the sum of the squares of its digits. 
 	Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
	 	Those numbers for which this process ends in 1 are happy. 
Return true  n 	 false 	. 
Constraints: 
	 	1 <= n <= 231 - 1 
 
Example 1: 
Input: n = 19 
Output: true Explanation: 
12 + 92 = 82 
82 + 22 = 68 
62 + 82 = 100 
12 + 02 + 02 = 1 
 
Example 2: 
Input: n = 2 
Output: false 
'''



# from collections import Counter

# def isAnagram(s, t):
#     return Counter(s) == Counter(t)

# print(isAnagram("anagram", "nagaram"))
# print(isAnagram("rat", "car"))


# def isHappy(n):
#     seen = set()

#     while n != 1:
#         if n in seen:
#             return False

#         seen.add(n)
#         total = 0

#         while n > 0:
#             digit = n % 10
#             total += digit * digit
#             n //= 10

#         n = total

#     return True

# print(isHappy(19))
# print(isHappy(2))




'''
30.	Set Matrix Zeroes: Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's. You must do it in place. 
 Constraints: 
 	m == matrix.length  	n == matrix[0].length 
	 	1 <= m, n <= 200 
	 	-231 <= matrix[i][j] <= 231 - 1 
 
Example 1: 
  
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]] 
Output: [[1,0,1],[0,0,0],[1,0,1]] 
 
Example 2: 
  
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]] 
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]] 
'''

# def setZeroes(matrix):
#     rows = len(matrix)
#     cols = len(matrix[0])

#     firstRow = any(matrix[0][j] == 0 for j in range(cols))
#     firstCol = any(matrix[i][0] == 0 for i in range(rows))

#     for i in range(1, rows):
#         for j in range(1, cols):
#             if matrix[i][j] == 0:
#                 matrix[i][0] = 0
#                 matrix[0][j] = 0

#     for i in range(1, rows):
#         for j in range(1, cols):
#             if matrix[i][0] == 0 or matrix[0][j] == 0:
#                 matrix[i][j] = 0

#     if firstRow:
#         for j in range(cols):
#             matrix[0][j] = 0

#     if firstCol:
#         for i in range(rows):
#             matrix[i][0] = 0

#     return matrix

# matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# print(setZeroes(matrix))
