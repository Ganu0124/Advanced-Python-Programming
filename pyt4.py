''' 
16. Separate Letters and Numbers from a String 
You are given a string consisting of lowercase alphabets and digits. 
Your task is to: 
1.	Extract all letters from the string (in the same order of appearance)  
2.	Extract all digits from the string (in the same order of appearance)  Return the result as a list containing: 
	 	First: concatenated letters string  
Second: concatenated digits string  
Constraints: 
•	1 ≤ length of string ≤ 10⁵ 
•	String contains only lowercase English letters and digits (0–9) Input Format: 
•	A single string s Output Format: 
•	Return a list of two strings: 
•	[letters, digits] 
 
Example 1: 
Input: 
s = "a1b2c3d4" Output: ["abcd", "1234"] Explanation: 
Letters extracted: a, b, c, d → "abcd" 
Digits extracted: 1, 2, 3, 4 → "1234" 
 
Example 2: 
Input: 
s = "x9y8z7" Output: 
["xyz", "987"] Explanation: 
Letters → x, y, z → "xyz" 
Digits → 9, 8, 7 → "987" 
 
Example 3: 
Input: 
s = "12345" Output: 
["", "12345"] 
Explanation: 
No letters present, so letters string is empty. 
 
Example 4: 
Input: 
s = "abcdef" Output: 
["abcdef", ""] 
Explanation: 
No digit’s present, so digits string is empty. 
 

def separate(s):
    letters = ""
    digits = ""

    for ch in s:
        if ch.isalpha():
            letters += ch
        else:
            digits += ch

    return [letters, digits]


s = "a1b2c3d4"

print("Input:", s)
print("Output:", separate(s))



17. Merge Intervals 
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return 	. 
 Constraints: 
 	1 <= intervals.length <= 104  	intervals[i].length == 2 
0 <= starti <= endi <= 104 
 
Example 1: 
Input: intervals = [[1,3],[2,6],[8,10],[15,18]] 
Output: [[1,6],[8,10],[15,18]] 
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6]. 
 
Example 2: 
Input: intervals = [[1,4],[4,5]] 
Output: [[1,5]] 
Explanation: Intervals [1,4] and [4,5] are considered overlapping. 
 
Example 3: 
Input: intervals = [[4,7],[1,4]] 
Output: [[1,7]] 
Explanation: Intervals [1,4] and [4,7] are considered overlapping. 


def mergeIntervals(intervals):
    intervals.sort()

    result = []

    for start, end in intervals:

        if not result or start > result[-1][1]:
            result.append([start, end])
        else:
            result[-1][1] = max(result[-1][1], end)

    return result


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

print("Input:", intervals)
print("Output:", mergeIntervals(intervals))


18.	Maximum Product Subarray: Given an integer array nums, find a subarray that has the largest product, and return 	. 
The test cases are generated so that the answer will fit in a 32-bit integer. 
Note that the product of an array with a single element is the value of that element. 
 Constraints: 
	 	1 <= nums.length <= 2 * 104 
	 	-10 <= nums[i] <= 10 
	 	The product of any subarray of nums is guaranteed to fit in a 32-bit integer. 
 
Example 1: 
Input: nums = [2,3,-2,4] 
Output: 6 
Explanation: [2,3] has the largest product 6. 
 
Example 2: 
Input: nums = [-2,0,-1] 
Output: 0 
Explanation: The result cannot be 2, because [-2,-1] is not a subarray. 
  

def maxProduct(nums):
    maximum = nums[0]
    minimum = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):

        if nums[i] < 0:
            maximum, minimum = minimum, maximum

        maximum = max(nums[i], maximum * nums[i])
        minimum = min(nums[i], minimum * nums[i])

        result = max(result, maximum)

    return result


nums = [2, 3, -2, 4]

print("Input:", nums)
print("Output:", maxProduct(nums))


19.	Minimum Team Selection to Cover Required Skills You are given: 
1.	A list of required technical skills for a project  
2.	A list of N candidates, where each candidate possesses a subset of these skills  Your task is to select the smallest possible team (minimum number of candidates) such that all required skills are covered. 
Return the indices of selected candidates (0-based indexing) forming the smallest team. 
 
Constraints: 
•	1 ≤ number of required skills ≤ 16 
•	1 ≤ N ≤ 60 
•	Each candidate has at least one skill 
•	Skills are strings (e.g., "Python", "SQL") 
•	There is at least one valid team Input Format: 
	 	First line: space-separated required skills  
	 	Second line: integer N  
	 	Next N lines: space-separated skills of each candidate  
 
Output Format: 
Print indices of selected candidates (in any order) forming the minimum team. 
 
Example 1: 
Input: 
 	Skills: Python SQL MachineLearning DataStructures 
 	N = 4 
Candidates: 
0	→ Python SQL 
1	→ SQL MachineLearning 
2	→ MachineLearning DataStructures 
3	→ DataStructures Output: 0 2 Explanation: 
	 	Candidate 0 → Python, SQL  
	 	Candidate 2 → MachineLearning, DataStructures 
Together they cover all required skills with minimum team size = 2.  
 
Example 2: 
Input: 
Skills: Java Python SQL N = 3 
Candidates: 
0	→ Java 
1	→ Python SQL 
2	→ SQL 
Output: 0 1 Explanation: 
	 	Candidate 0 → Java  
	 	Candidate 1 → Python, SQL 
All skills are covered with minimum 2 candidates.  
 
Example 3: 
Input: 
Skills: C++ Python DataStructures N = 4 
Candidates: 
0	→ C++ 
1	→ Python 
2	→ DataStructures 
3	→ C++ Python DataStructures 
 
Output: 3 
Explanation: 
Candidate 3 alone covers all required skills → optimal solution. 
 

 def smallestTeam(reqSkills, people):
    n = len(reqSkills)

    skillMap = {skill: i for i, skill in enumerate(reqSkills)}

    dp = {0: []}

    for i, person in enumerate(people):

        mask = 0

        for skill in person:
            if skill in skillMap:
                mask |= 1 << skillMap[skill]

        for oldMask, team in list(dp.items()):

            newMask = oldMask | mask

            if newMask not in dp or len(dp[newMask]) > len(team) + 1:
                dp[newMask] = team + [i]

    return dp[(1 << n) - 1]


reqSkills = ["Python", "SQL", "MachineLearning", "DataStructures"]

people = [
    ["Python", "SQL"],
    ["SQL", "MachineLearning"],
    ["MachineLearning", "DataStructures"],
    ["DataStructures"]
]

print("Output:", smallestTeam(reqSkills, people))


20.	You are given:  	A string s  
 	A dictionary of strings wordDict  Your task is to: 
1.	Determine whether the string s can be segmented into a space-separated sequence of one or more dictionary words  
2.	If possible, also print all valid segmentations (patterns)  
You are allowed to reuse words from the dictionary multiple times 
 
Constraints: 
•	1 ≤ s.length ≤ 300 
•	1 ≤ wordDict.length ≤ 1000 
•	1 ≤ wordDict[i].length ≤ 20 
•	All words consist of lowercase English letters 
•	All dictionary words are unique 
 
Example 1: 
Input: 
s = "AmritaMysuru" 
wordDict = ["Amrita", “Rita”, "Mysuru"] Output: 
Can Segment: true 
Segmentations: Amrita rita Mysuru Explanation: 
	 	" AmritaMysuru" → "Amrita" + "rita" + " Mysuru" 
✔	Valid segmentation exists  
 
Example 2: 
Input: s = "applepenapple" wordDict = ["apple","pen"] Output: 
Can Segment: true 
Segmentations: apple pen apple Explanation: 
	 	"applepenapple" → "apple" + "pen" + "apple" 
✔	Word reuse is allowed  
 
Example 3: 
Input: 
s = "catsanddog" 
wordDict = ["cat","cats","and","sand","dog"] Output: 
Can Segment: true 
Segmentations:  cats and dog  
 	 	cat sand dog 
Explanation: 
Two valid segmentations: 
	 	"cats" + "and" + "dog"  
	 	"cat" + "sand" + "dog"  
 
Example 4 (Invalid Case): 
Input: 
s = "catsandog" wordDict = ["cats","dog","sand","and","cat"] Output: 
Can Segment: false Segmentations: 
None 
Explanation: 
	 	No valid way to fully segment the string 
 Return false  

def wordBreak(s, wordDict):
    result = []

    def backtrack(start, current):

        if start == len(s):
            result.append(" ".join(current))
            return

        for word in wordDict:

            if s.startswith(word, start):
                backtrack(start + len(word), current + [word])

    backtrack(0, [])

    print("Can Segment:", len(result) > 0)
    print("Segmentations:")

    if result:
        for sentence in result:
            print(sentence)
    else:
        print("None")


s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]

wordBreak(s, wordDict)
'''