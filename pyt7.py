''' 

31.	You are given a list of drawn cards from a standard 52-card deck. Each card is represented as a string (e.g., "AH", "10D", "KS"). 
Your task is to: 
1.	Calculate the probability of drawing each category:  
o	Ace  
o	Face card (J, Q, K)  
o	Red card (Hearts, Diamonds)  
2.	Identify the most frequent category among the above  
3.	Compute the probability of drawing a black card  Constraints: 
•	1 ≤ N ≤ 10⁵ 
•	Valid cards from standard deck 
•	Cards may repeat (sampling with replacement) 
 
Input:  
cards = ["AH", "10D", "KC", "QS", "2H", "JD", "7C", "KH"] Output: 
P(Ace)=0.125 P(Face)=0.50 P(Red)=0.50 
Most Frequent Category: Face P(Black)=0.50 Explanation: 
Step 1: Count occurrences 
	 	Ace → AH → 1  
	 	Face → KC, QS, JD, KH → 4  
	 	Red → AH, 10D, 2H, JD → 4  
	 	Black → KC, QS, 7C, KH → 4  
Total cards = 8 
 
Step 2: Compute probabilities 
	 	P(Ace) = 1/8 = 0.125  
	 	P(Face) = 4/8 = 0.50  
	 	P(Red) = 4/8 = 0.50  
	 	P(Black) = 4/8 = 0.50  
 
Step 3: Most frequent category 
Face cards = highest frequency 
'''

# def cardProbability(cards):
#     total = len(cards)

#     ace = 0
#     face = 0
#     red = 0
#     black = 0

#     for card in cards:
#         rank = card[:-1]
#         suit = card[-1]

#         if rank == "A":
#             ace += 1

#         if rank in ["J", "Q", "K"]:
#             face += 1

#         if suit in ["H", "D"]:
#             red += 1
#         else:
#             black += 1

#     print("P(Ace) =", ace / total)
#     print("P(Face) =", face / total)
#     print("P(Red) =", red / total)

#     categories = {"Ace": ace, "Face": face, "Red": red}
#     mostFrequent = max(categories, key=categories.get)

#     print("Most Frequent Category:", mostFrequent)
#     print("P(Black) =", black / total)

# cards = ["AH", "10D", "KC", "QS", "2H", "JD", "7C", "KH"]
# cardProbability(cards)



'''
32. Toggle K-th Bit:  
XOR flips the selected bit. 
 
Example 1: 
Input: n = 5, k = 1 
Output: 7 
Explanation: 
5 → 101 
Toggle bit1 → 111 = 7 
 
Example 2: 
Input: n = 4, k = 2 
Output: 0 Explanation: 
4 → 100 
Toggle bit2 → 000 = 0 
'''


# def toggleBit(n, k):
#     return n ^ (1 << k)

# print(toggleBit(5, 1))
# print(toggleBit(4, 2))


'''
33. Plus One:  
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's. 
Increment the large integer by one and return 	. 
 Constraints: 
 	1 <= digits.length <= 100  	0 <= digits[i] <= 9  	digits do not contain any leading 0's. 
 
Example 1: 
Input: digits = [1,2,3] 
Output: [1,2,4] 
Explanation: The array represents the integer 123. 
Incrementing by one gives 123 + 1 = 124. 
Thus, the result should be [1,2,4]. 
 
Example 2: 
Input: digits = [4,3,2,1] 
Output: [4,3,2,2] 
Explanation: The array represents the integer 4321. 
Incrementing by one gives 4321 + 1 = 4322. 
Thus, the result should be [4,3,2,2]. 
 
Example 3: 
Input: digits = [9] 
Output: [1,0] 
Explanation: The array represents the integer 9. 
Incrementing by one gives 9 + 1 = 10. 
Thus, the result should be [1,0]. 
'''


def plusOne(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits

        digits[i] = 0

    return [1] + digits

print(plusOne([1, 2, 3]))
print(plusOne([4, 3, 2, 1]))
print(plusOne([9]))


'''
34. String Transformation with Given Substring You are given: 
	 	A string s consisting of lowercase English letters  
 	A substring sub which is guaranteed to be a contiguous part of s  You must perform the following operation: 
 	Replace each character in the substring with its previous character in the English alphabet  
 	'b' 	 'a', 'c' 	 'b', …, 'a' 	 'z'  Your task is to: 
1.	Apply the transformation only on the given substring  
2.	Return the resulting string  Constraints: 
•	1 ≤ length of s ≤ 10⁵ 
•	sub is a valid substring of s 
•	s contains only lowercase English letters 
 
Example 1: 
Input: 
s = "hackerrank"   sub = "hack" Output: gzbjerrank Explanation: 
Step 1: Identify substring "hack" in s Step 2: Transform each character: 
 	h → g   	a → z   	c → b   	k → j  
Step 3: Replace substring in original string 
Original: hackerrank 
Updated: gzbjerrank 
 
Example 2: 
Input: 
s = "programming"   sub = "gram" Output: profqzlming  Explanation:  	g → f   	r → q   	a → z  
	 	m → l  
Final string → profqzlming 
 
Example 3: 
Input: 
s = "apple"   sub = "a" Output: zpple Explanation:  	a → z 
Only first character changes 
 '''

def transformString(s, sub):
    start = s.index(sub)
    result = list(s)

    for i in range(start, start + len(sub)):
        result[i] = chr((ord(result[i]) - ord('a') - 1) % 26 + ord('a'))

    return "".join(result)

print(transformString("hackerrank", "hack"))
print(transformString("programming", "gram"))
print(transformString("apple", "a"))




 '''
35. Trapping Rain Water  
You are given an array height of n non-negative integers where: 
	 	Each value represents the height of a bar  
	 	Each bar has width = 1  
After raining, water gets trapped between the bars. 
Your Task: Compute the total amount of water that can be trapped. 
 
Core Idea: Water trapped at any index depends on: 
	Water at i	left max right max	 
Intuition 
 At each position: 
	 	Look left 	 highest wall  
	 	Look right 	 highest wall  
 	Water level is limited by the shorter of the two  Constraints: 
 	n == height.length  	1 <= n <= 2 * 104 
0	<= height[i] <= 105 
 
Example 1 
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1] 
Output: 6 
 
Step-by-Step Explanation 
  
Let’s analyze each index: 
Index 	Height 	Left Max 	Right Max 	Water 
0 	0 	0 	3 	0 
1 	1 	1 	3 	0 
2 	0 	1 	3 	1 
3 	2 	2 	3 	0 
4 	1 	2 	3 	1 
5 	0 	2 	3 	2 
6 	1 	2 	3 	1 
7 	3 	3 	3 	0 
8 	2 	3 	2 	0 
9 	1 	3 	2 	1 
10 	2 	3 	2 	0 
11 	1 	3 	1 	0 
 
Water Accumulated 
1	+ 1 + 2 + 1 + 1 = 6 
Total trapped water = 6 units 
 
Key Observation 
	 	Water is trapped only in valleys  
	 	Higher bars on both sides act as boundaries  
 
Example 2 
Input: height = [4,2,0,3,2,5] 
Output: 9
'''

# def trap(height):
#     left = 0
#     right = len(height) - 1
#     leftMax = 0
#     rightMax = 0
#     water = 0

#     while left < right:
#         if height[left] < height[right]:
#             if height[left] >= leftMax:
#                 leftMax = height[left]
#             else:
#                 water += leftMax - height[left]
#             left += 1
#         else:
#             if height[right] >= rightMax:
#                 rightMax = height[right]
#             else:
#                 water += rightMax - height[right]
#             right -= 1

#     return water

# print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# print(trap([4, 2, 0, 3, 2, 5]))
