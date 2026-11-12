''' 
21. Number of 1 Bits:  
Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight). 
Constraints: 
	 	1 <= n <= 231 - 1 
 
Example 1: 
Input: n = 11 
Output: 3 
Explanation: 
The input binary string 1011 has a total of three set bits. 
 
Example 2: 
Input: n = 128 Output: 1 
Explanation: 
The input binary string 10000000 has a total of one set bit. 
 
Example 3: 
Input: n = 2147483645 Output: 30 
Explanation: 
The input binary string 1111111111111111111111111111101 has a total of thirty set bits. 
 ''' 

# def hammingWeight(n):
#     count = 0
#     while n:
#         n = n & (n - 1)
#         count += 1
#     return count

# n = 128
# print(hammingWeight(n))


'''
22. Midpoint of Line Segment 
You are given the coordinates of two endpoints of a line segment: (x₁, y₁) and (x₂, y₂). Your task is to compute the midpoint of the line segment. Return the midpoint as a pair of coordinates (mx, my). 
Constraints: 
• −10⁴ ≤ x₁, y₁, x₂, y₂ ≤ 10⁴ 
 
Example 1: 
Input: 
Point 1: (0,0) 
Point 2: (4,4) 
Output: (2,2) Explanation: 
Midpoint formula: 
mx = (x₁ + x₂)/2 = (0 + 4)/2 = 2 
my = (y₁ + y₂)/2 = (0 + 4)/2 = 2 
 
Example 2: 
Input: 
Point 1: (1,3) 
Point 2: (5,7) 
Output: (3,5) Explanation: mx = (1 + 5)/2 = 3 
my = (3 + 7)/2 = 5 
 
Example 3: 
Input: 
Point 1: (-2,4) 
Point 2: (2,0) 
Output: (0,2) Explanation: 
mx = (-2 + 2)/2 = 0 
my = (4 + 0)/2 = 2 
'''

# def midpoint(x1, y1, x2, y2):
#     mx = (x1 + x2) / 2
#     my = (y1 + y2) / 2
#     return (mx, my)

# print(midpoint(0, 0, 4, 4))
# print(midpoint(1, 3, 5, 7))
# print(midpoint(-2, 4, 2, 0))


'''
23. Sum of Cubes in a Given Range 
You are given two integers a and b representing a range. 
Your task is to compute the sum of cubes of all integers from a to b (inclusive). 
Mathematically, you need to calculate: 
𝒂𝟑+(𝒂+𝟏)𝟑+(𝒂+𝟐)𝟑+⋯+𝒃𝟑 
Constraints: 	
 	 	 
Input Format:  	1 ≤ a ≤ b ≤ 10⁵ 
 	 	 
Output Format:  	Two integers: a b 
 	 	 	Print a single integer representing the sum of cubes from a to b. 
 
Example 1: 
Input: 4 9 Output: 1989 Explanation: 
We compute cubes of each number from 4 to 9: 
Number 	Cube
4 	64 
5 	125 
6 	216 
7 	343 
8 	512 
9 	729 
Now sum them: 64+125+216+343+512+729=1989 
 
Example 2: 
Input: 1 3 
Output: 36 
Explanation: 13+23+33 =1+8+27=36 
 
Example 3: 
Input: 5 5 
Output: 125 
Explanation: Only one number:53 =125 
'''

# def sumOfCubes(a, b):
#     def cubeSum(n):
#         return (n * (n + 1) // 2) ** 2

#     return cubeSum(b) - cubeSum(a - 1)

# a = 4
# b = 9
# print(sumOfCubes(a, b)


'''
24. Closest Pair of Points 
You are given a list of n points in a 2D plane, where each point is represented as (x, y). 
Your task is to determine the minimum Euclidean distance between any two distinct points. Return the minimum distance between any pair of points. 
 
Constraints: 
•	2 ≤ n ≤ 10⁴ 
•	−10⁴ ≤ x, y ≤ 10⁴ 
 
Example 1: 
Input: points = [(0,0), (1,1)] 
Output: √2 
Explanation: 
Distance between (0,0) and (1,1): 
√((1−0)² + (1−0)²) = √(1 + 1) = √2 
 
Example 2: 
Input: points = [(1,1), (2,2), (5,5)] 
Output: √2 
Explanation: 
Distances: 
Between (1,1) and (2,2) → √2 
Between (2,2) and (5,5) → √18 
Between (1,1) and (5,5) → √32 Minimum distance is √2. 
 
Example 3: 
Input: points = [(0,0), (3,4), (6,8)] 
Output: 5 
Explanation: 
Distances: 
(0,0) to (3,4) → √(9+16) = 5 
(3,4) to (6,8) → 5 
(0,0) to (6,8) → 10 
Minimum distance = 5. 
'''

import math

def closestPair(points):
    px = [(x, y, i) for i, (x, y) in enumerate(points)]
    px.sort()
    py = sorted(px, key=lambda p: p[1])

    def distance(p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    def solve(px, py):
        n = len(px)

        if n <= 3:
            return min(
                (distance(px[i], px[j])
                 for i in range(n)
                 for j in range(i + 1, n)),
                default=float('inf')
            )

        mid = n // 2
        left = px[:mid]
        right = px[mid:]

        left_ids = {p[2] for p in left}
        left_y = [p for p in py if p[2] in left_ids]
        right_y = [p for p in py if p[2] not in left_ids]

        d = min(solve(left, left_y), solve(right, right_y))

        strip = [p for p in py if abs(p[0] - px[mid][0]) < d]

        for i in range(len(strip)):
            for j in range(i + 1, min(i + 8, len(strip))):
                d = min(d, distance(strip[i], strip[j]))

        return d

    return solve(px, py)

points = [(0, 0), (1, 1)]
print(closestPair(points))




'''
25. Count Trailing Zeros in Binary:  
Trailing zeros are counted from the rightmost side until the first ‘1’ appears. 
 
Example 1: 
Input: n = 8 
Output: 3 Binary: 1000 
Explanation: 
Binary: 1000 → three zeros after last ‘1’. 
 
Example 2: 
Input: n = 12 
Output: 2 Binary: 1100 
Explanation: 
Binary: 1100 → two trailing zeros. 
'''

# def trailingZeros(n):
#     count = 0

#     while n > 0 and n % 2 == 0:
#         count += 1
#         n //= 2

#     return count

# print(trailingZeros(8))
# print(trailingZeros(12))
