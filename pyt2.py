''' 6.Reverse Integer: Given a signed 32-bit integer x, return x 	. If 
reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0. Assume the environment does not allow you to store 64-bit integers (signed or unsigned). Constraints: 
•	-231 <= x <= 231 - 1 
 
Example 1: 
Input: x = 123 
Output: 321 
 
Example 2: 
Input: x = -123 
Output: -321 
 
Example 3: 
Input: x = 120 
Output: 21 
''' 
# def reverseInteger(x):
#     sign = -1 if x < 0 else 1
#     num = abs(x)
#     rev = 0

#     limit = 2147483648 if x < 0 else 2147483647

#     while num > 0:
#         digit = num % 10

#         if rev > limit // 10 or (rev == limit // 10 and digit > limit % 10):
#             return 0

#         rev = rev * 10 + digit
#         num //= 10

#     return rev * sign


# # Example
# x = 123
# print("Input:", x)
# print("Output:", reverseInteger(x))

'''
7.	Minimize Maximum Consecutive Zeros with Construction You are given two integers: 
•	L 	 length of a binary string  
•	K 	 number of ones (1s) in the string  
The remaining positions (L − K) are filled with zeros (0s). 
Your tasks are: 
1.	Generate all possible binary strings of length L containing exactly K ones.  
2.	For each string, determine the length of the longest contiguous block of zeros.  
3.	Identify the optimal arrangement(s) such that this maximum zero block is minimized.  
Output Requirements: 
•	Print all possible valid binary strings  
•	For each string, print its maximum consecutive zero length  
•	Print the optimal string(s) that achieve the minimum possible longest zero block  
•	Finally, print that minimum length  
 
Constraints: 
•	1 ≤ L ≤ 15 	 
•	0 ≤ K ≤ L 
Input Format: 
A single line containing two integers: 
L K 
Output Format: 
•	List all possible binary strings  • 	For each string:  string 	 max zero block  
•	Then print:  Optimal string(s) 
 Minimum longest zero block  
 
Example 1: 
Input: 4 2 Output: 
Possible Strings: 
1100 → max zeros = 2 
1010 → max zeros = 1 
1001 → max zeros = 2 
0110 → max zeros = 1 
0101 → max zeros = 1 
0011 → max zeros = 2 
Optimal Arrangement(s): 1010, 0110, 0101 Minimum Longest Zero Block: 1 Explanation: 
Strings where zeros are evenly distributed have the smallest maximum zero block. 
 
Example 2: 
Input: 5 0 Output: 
Possible Strings: 
00000 → max zeros = 5 
Optimal Arrangement(s): 00000 Minimum Longest Zero Block: 5 Explanation: 
All positions are zeros, so the longest block is the full length. 
 
Example 3: 
Input: 5 5 
Output: 
Possible Strings: 
11111 → max zeros = 0 
Optimal Arrangement(s): 11111 Minimum Longest Zero Block: 0 Explanation: 
No zeros present. 
'''
# def maxZeros(s):
#     count = 0
#     maximum = 0

#     for ch in s:
#         if ch == '0':
#             count += 1
#             maximum = max(maximum, count)
#         else:
#             count = 0

#     return maximum


# def generateStrings(L, K):
#     result = []

#     def generate(s, ones):
#         if len(s) == L:
#             if ones == K:
#                 result.append(s)
#             return

#         if ones < K:
#             generate(s + '1', ones + 1)

#         if len(s) - ones < L - K:
#             generate(s + '0', ones)

#     generate("", 0)
#     return result


# L = 4
# K = 2

# strings = generateStrings(L, K)

# minimum = L
# optimal = []

# print("Possible Strings:")

# for s in strings:
#     zeros = maxZeros(s)
#     print(s, "-> max zeros =", zeros)

#     if zeros < minimum:
#         minimum = zeros
#         optimal = [s]
#     elif zeros == minimum:
#         optimal.append(s)

# print("Optimal Arrangement(s):", ", ".join(optimal))
# print("Minimum Longest Zero Block:", minimum)

''' 
8. Merge Triplets to Form Target Triplet 
A triplet is an array of three integers. You are given a 2D integer array triplets, where triplets[i] = [ai, bi, ci] describes the ith triplet. You are also given an integer array target = [x, y, z] that describes the triplet you want to obtain. 
To obtain target, you may apply the following operation on triplets any number of times (possibly zero): 
•	Choose two indices (0-indexed) i and j (i != j) and update triplets[j] to become [max(ai, aj), max(bi, bj), max(ci, cj)]. 
•	For example, if triplets[i] = [2, 5, 3] and triplets[j] = [1, 7, 5], triplets[j] will be updated to [max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5]. 
Return true  target  [x, y, z]    triplets  false 	. 
 Constraints: 
•	1 <= triplets.length <= 105 
•	triplets[i].length == target.length == 3 
•	1 <= ai, bi, ci, x, y, z <= 1000 
 
Example 1: 
Input: triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5] 
Output: true 
The merging triplet to reach the target = [[2,5,3],[1,8,4]] 
Target = [2,7,5] 
Explanation: Perform the following operations: 
- Choose the first and last triplets [[2,5,3],[1,8,4],[1,7,5]].  
Update the last triplet to be [max(2,1), max(5,7), max(3,5)] = [2,7,5].  
triplets = [[2,5,3],[1,8,4],[2,7,5]] 
The target triplet [2,7,5] is now an element of triplets. 
 
Example 2: 
Input: triplets = [[3,4,5],[4,5,6]], target = [3,2,5] 
Output: false 
The merging triplet to reach the target = [[3,4,5],[4,5,6]] 
Target = none 
Explanation: It is impossible to have [3,2,5] as an element because there is no 2 in any of the triplets. 
 
Example 3: 
Input: triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [5,5,5] 
Output: true 
The merging triplet to reach the target = [[2,5,5],[5,2,3]] 
Target = [5,5,5] 
Explanation: Perform the following operations: 
-	Choose the first and third triplets [[2,5,3],[2,3,4],[1,2,5],[5,2,3]].  Update the third triplet to be [max(2,1), max(5,2), max(3,5)] = [2,5,5].  
triplets = [[2,5,3],[2,3,4],[2,5,5],[5,2,3]]. 
-	Choose the third and fourth triplets [[2,5,3],[2,3,4],[2,5,5],[5,2,3]].  Update the fourth triplet to be [max(2,5), max(5,2), max(5,3)] = [5,5,5].  
triplets = [[2,5,3],[2,3,4],[2,5,5],[5,5,5]]. 
The target triplet [5,5,5] is now an element of triplets. 
 '''
# def mergeTriplets(triplets, target):
#     found = [False, False, False]

#     for t in triplets:

#         if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
#             continue

#         for i in range(3):
#             if t[i] == target[i]:
#                 found[i] = True

#     return all(found)


# # Example
# triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
# target = [2, 7, 5]

# print("Triplets:", triplets)
# print("Target:", target)
# print("Output:", mergeTriplets(triplets, target))

'''
9. Palindromic Substrings with Pattern Listing 
You are given a string s consisting of lowercase English letters. 
A palindrome is a string that reads the same forward and backward. 
A substring is a contiguous sequence of characters within the string. 
Your Task: 
1.	Count the total number of palindromic substrings in the string  
2.	Also print all palindromic substrings (patterns)  
Duplicate substrings at different positions should be counted separately Constraints: 
•	1 ≤ s.length ≤ 1000 
•	s consists only of lowercase English letters 
 
Example 1: Input: s = "ababa" Output: 
Total Count: 9 
Palindromic Substrings: 
a b a b 
a aba bab aba ababa 
Explanation: 
Let’s identify all palindromic substrings: 
Step 1: Single character palindromes (always valid) 
	 	"a", "b", "a", "b", "a" → 5 substrings  
Step 2: Length 3 palindromes 
 	"aba" (from index 0–2)   	"bab" (from index 1–3)  
 	"aba" (from index 2–4)  → 3 substrings 
Step 3: Length 5 palindrome 
 	"ababa"  → 1 substring 
Total = 5 + 3 + 1 = 9 
 
Example 2: Input: s = "racecar" Output: 
Total Count: 10 Palindromic Substrings: 
r a c e c a r cec aceca racecar 
Explanation: 
	 	Single characters → 7  
	 	"cec" → 1  
	 	"aceca" → 1  
	 	"racecar" → 1  
Total = 10 
 
Example 3: Input: s = "level" Output: 
Total Count: 7 Palindromic Substrings: 
l e v e 
l 
eve level 
Explanation: 
	 	Single characters → 5  
	 	"eve" → 1  
	 	"level" → 1  
Total = 7 
'''
# def findPalindromes(s):
#     result = []

#     for length in range(1, len(s) + 1):

#         for i in range(len(s) - length + 1):

#             sub = s[i:i + length]

#             if sub == sub[::-1]:
#                 result.append(sub)

#     return result


# # Example
# s = "ababa"

# palindromes = findPalindromes(s)

# print("Input:", s)
# print("Total Count:", len(palindromes))
# print("Palindromic Substrings:")

# for p in palindromes:
#     print(p)

'''
10. Kth Smallest Element in a BST 
Given the root of a binary search tree, and an integer k, return 	 kth 
. 
Constraints: 
	 	The number of nodes in the tree is n. 
	 	1 <= k <= n <= 104 
	 	0 <= Node.val <= 104 
 
Example 1: 
Tree Structure 
          8 
        /   \ 
3	10 
      / \        \ 
    1   6      14 
        / \      / 
4	7   13 
Input: root = [8, 3, 10, 1, 6, null, 14, null, null, 4, 7, 13], k = 5 
Output: 5th smallest element = 7 
 
Example 2: 
        5 
       / \ 
     3   6 
    / \ 
  2   4 
  / 
1 
Input: root = [5,3,6,2,4,null,null,1], k = 3 
Output: 3 

 ''' 

#  class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


# def kthSmallest(root, k):
#     values = []

#     def inorder(node):
#         if node is None:
#             return

#         inorder(node.left)
#         values.append(node.val)
#         inorder(node.right)

#     inorder(root)

#     return values[k - 1]


# # Example
# root = Node(8)

# root.left = Node(3)
# root.right = Node(10)

# root.left.left = Node(1)
# root.left.right = Node(6)

# root.left.right.left = Node(4)
# root.left.right.right = Node(7)

# root.right.right = Node(14)
# root.right.right.left = Node(13)

# k = 5

# print("K:", k)
# print("Output:", kthSmallest(root, k))