''' 

36.	Generate Parentheses 
Given n pairs of parentheses, write a function to 
. 
 Constraints: 
	 	1 <= n <= 8 
 
Example 1: 
Input: n = 3 
Output: ["((()))","(()())","(())()","()(())","()()()"] 
 
Example 2: 
Input: n = 1 
Output: ["()"] 
 '''

# def generateParenthesis(n):
#     result = []

#     def backtrack(current, openCount, closeCount):
#         if len(current) == 2 * n:
#             result.append(current)
#             return

#         if openCount < n:
#             backtrack(current + "(", openCount + 1, closeCount)

#         if closeCount < openCount:
#             backtrack(current + ")", openCount, closeCount + 1)

#     backtrack("", 0, 0)
#     return result

# print(generateParenthesis(3))
# print(generateParenthesis(1))

'''
37.	Spiral Matrix:  
Given an m x n matrix, return 	 matrix 	. 
Constraints: 
 	m == matrix.length  	n == matrix[i].length  	1 <= m, n <= 10 
	 	-100 <= matrix[i][j] <= 100 
 
Example 1: 
  
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]] 
Output: [1,2,3,6,9,8,7,4,5] 
 
Example 2: 
  
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]] 
Output: [1,2,3,4,8,12,11,10,9,5,6,7] 
'''
# def spiralOrder(matrix):
#     result = []

#     top = 0
#     bottom = len(matrix) - 1
#     left = 0
#     right = len(matrix[0]) - 1

#     while top <= bottom and left <= right:

#         for i in range(left, right + 1):
#             result.append(matrix[top][i])
#         top += 1

#         for i in range(top, bottom + 1):
#             result.append(matrix[i][right])
#         right -= 1

#         if top <= bottom:
#             for i in range(right, left - 1, -1):
#                 result.append(matrix[bottom][i])
#             bottom -= 1

#         if left <= right:
#             for i in range(bottom, top - 1, -1):
#                 result.append(matrix[i][left])
#             left += 1

#     return result

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(spiralOrder(matrix))

# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# print(spiralOrder(matrix))








'''
38.	Container With Most Water 
You are given an integer array height of length n. 
 	Each element represents a vertical line at position i   	The height of the line is height[i]  
 	Two lines together with the x-axis form a container  Your Task: 
Find two lines such that the container formed between them holds the maximum amount of water. 
Important Rule: 
	 	The container cannot be tilted  
	 	The water level is determined by the shorter of the two lines  
Formula Used: 
	Area	right index	left index	 
Constraints: 
•	2 ≤ n ≤ 10⁵ 
•	0 ≤ height[i] ≤ 10⁴ 
 
Example 1 
Input: height = [1,8,6,2,5,4,8,3,7] 
Output: 49 
Explanation: 
  
Choose: 
	 	Left = index 1 → height = 8  
 	Right = index 8 → height = 7  width = 8 - 1 = 7 height = min(8, 7) = 7 
area = 7 × 7 = 49 
Maximum area = 49 
 
Example 2 
Input: height = [1,1] Output: 1 Explanation: width = 1 height = min(1,1) = 1 
area = 1 × 1 = 1 
 
Example 3  
Input height = [4,3,2,1,4] 
Output: 16 
 
Explanation: 
Choose: 
	 	Left = index 0 → height = 4  
	 	Right = index 4 → height = 4  
 
Step 1: Width width = 4 - 0 = 4 Step 2: Height min(4, 4) = 4 Step 3: Area area = 4 × 4 = 16 
 
Why this is optimal? 
Check another pair: 
	 	index (0,3) → heights (4,1)  
width = 3 height = 1 area = 3 × 1 = 3 	 Much smaller than 16 
 Maximum area = 16 
 '''
# def maxArea(height):
#     left = 0
#     right = len(height) - 1
#     maximum = 0

#     while left < right:
#         width = right - left
#         h = min(height[left], height[right])
#         maximum = max(maximum, width * h)

#         if height[left] < height[right]:
#             left += 1
#         else:
#             right -= 1

#     return maximum

# print(maxArea([1,8,6,2,5,4,8,3,7]))
# print(maxArea([1,1]))
# print(maxArea([4,3,2,1,4]))

'''

39. Matrix Chain Multiplication  
You are given a sequence of matrices: 	 
Each matrix 	has dimensions: 	 
Goal: Determine the minimum number of scalar multiplications needed to multiply the entire chain of matrices. 
Important Note: 
	 	Matrix multiplication is associative  
 	But the order of multiplication affects cost  Your Task: 
1.	Return the minimum multiplication cost  
2.	Also print:  
	 	Optimal parenthesization (order of multiplication)  
 	Step-by-step multiplication sequence  Constraints: 
•	1 ≤ n ≤ 100 
•	Matrix dimensions are positive integers 
Key Idea: We try all possible split points: 	 
Approach 
1.	Use DP table  
2.	Try all partition points  
3.	Store minimum cost  
4.	Track split to reconstruct solution 
 
Example 1 
Input: Dimensions = [10, 30, 5, 60] Matrices: 
A1 = 10×30 
A2 = 30×5 
A3 = 5×60 
 
Output: Minimum Cost: 4500 
Optimal Parenthesization: ((A1 × A2) × A3) Multiplication Sequence: 
Step 1: (A1 × A2) → cost = 10×30×5 = 1500 
Step 2: (Result × A3) → cost = 10×5×60 = 3000 Total Cost: 1500 + 3000 = 4500 Explanation: 
Two possible ways: 
1.	→ cost = 4500  
2.	→ cost = 27000  
 Choose minimum 
 
Example 2 
Input: Dimensions = [40, 20, 30, 10, 30] 
Output: Minimum Cost: 26000 
Optimal Parenthesization: ((A1 × (A2 × A3)) × A4) Multiplication Sequence: 
Step 1: (A2 × A3) → cost = 20×30×10 = 6000 
Step 2: (A1 × Result) → cost = 40×20×10 = 8000 
Step 3: (Result × A4) → cost = 40×10×30 = 12000 Total Cost: 6000 + 8000 + 12000 = 26000 Explanation: 
We try all possible splits and pick the minimum cost 
Dynamic Programming avoids recomputation 
'''

#  def matrixChain(dims):
#     n = len(dims) - 1

#     dp = [[0] * n for _ in range(n)]
#     split = [[0] * n for _ in range(n)]

#     for length in range(2, n + 1):
#         for i in range(n - length + 1):
#             j = i + length - 1
#             dp[i][j] = float('inf')

#             for k in range(i, j):
#                 cost = (
#                     dp[i][k] +
#                     dp[k + 1][j] +
#                     dims[i] * dims[k + 1] * dims[j + 1]
#                 )

#                 if cost < dp[i][j]:
#                     dp[i][j] = cost
#                     split[i][j] = k

#     def parenthesize(i, j):
#         if i == j:
#             return f"A{i + 1}"

#         k = split[i][j]
#         return "(" + parenthesize(i, k) + " × " + parenthesize(k + 1, j) + ")"

#     def steps(i, j):
#         if i == j:
#             return

#         k = split[i][j]

#         steps(i, k)
#         steps(k + 1, j)

#         left = parenthesize(i, k)
#         right = parenthesize(k + 1, j)

#         print(f"{left} × {right} -> cost = {dims[i] * dims[k + 1] * dims[j + 1]}")

#     print("Minimum Cost:", dp[0][n - 1])
#     print("Optimal Parenthesization:", parenthesize(0, n - 1))
#     print("Multiplication Sequence:")
#     steps(0, n - 1)


# matrixChain([10, 30, 5, 60])
# matrixChain([40, 20, 30, 10, 30])


'''
40. Validate and complete a 9×9 Sudoku Board 
You are given a partially filled 9 × 9 Sudoku board, where: 
	 	Each cell contains:  
	 	A digit '1' to '9', or  
 	'.' representing an empty cell  Your Task: 
1.	Validate whether the given Sudoku board is valid based on Sudoku rules  
2.	If the board is valid, fill all empty cells (.) to generate a complete valid Sudoku solution  
3.	Print the completed Sudoku board in proper table format  
4.	If the board is invalid, return false and specify the reason  Sudoku Rules: 
1.	Each row must contain digits 1–9 without repetition  
2.	Each column must contain digits 1–9 without repetition  
3.	Each 3 × 3 sub-box must contain digits 1–9 without repetition  Important Notes: 
	 	Only filled cells need to be validated initially  
 	You must ensure the final board is fully valid and complete   	You may assume that:  
 	The input has at least one valid solution  Constraints: 
•	board.length == 9 
•	board[i].length == 9 
•	board[i][j]  {'1'–'9', '.'} 
 
Example 1 (Valid Case): Input: board =  
[["5","3",".",".","7",".",".",".","."], 
["6",".",".","1","9","5",".",".","."], 
[".","9","8",".",".",".",".","6","."], 
["8",".",".",".","6",".",".",".","3"], 
["4",".",".","8",".","3",".",".","1"], 
["7",".",".",".","2",".",".",".","6"], 
[".","6",".",".",".",".","2","8","."], 
[".",".",".","4","1","9",".",".","5"], 
[".",".",".",".","8",".",".","7","9"]] 
 
Output: Valid Sudoku: true Completed Sudoku: 
5	3  4 | 6  7  8 | 9  1  2 
6	7  2 | 1  9  5 | 3  4  8 
1  9  8 | 3  4  2 | 5  6  7 
--------------------------- 8  5  9 | 7  6  1 | 4  2  3 
4  2  6 | 8  5  3 | 7  9  1 
7  1  3 | 9  2  4 | 8  5  6 
--------------------------- 9  6  1 | 5  3  7 | 2  8  4 
2	8  7 | 4  1  9 | 6  3  5 
3	4  5 | 2  8  6 | 1  7  9 
 
Explanation: 
Step 1: Validation  Check all filled cells: 
	 	No duplicate in any row  
	 	No duplicate in any column  
	 	No duplicate in any 3×3 sub-grid  
Board is valid 
Step 2: Completion 
	 	Fill each empty cell (.) such that:  
	 	It satisfies row, column, and sub-grid constraints  
	 	Continue until all cells are filled  
 Final board satisfies all Sudoku rules 
 
Example 2 (Invalid Case): Input: board =  
[["8","3",".",".","7",".",".",".","."], 
["6",".",".","1","9","5",".",".","."], 
[".","9","8",".",".",".",".","6","."], 
["8",".",".",".","6",".",".",".","3"], 
["4",".",".","8",".","3",".",".","1"], 
["7",".",".",".","2",".",".",".","6"], 
[".","6",".",".",".",".","2","8","."], 
[".",".",".","4","1","9",".",".","5"], 
[".",".",".",".","8",".",".","7","9"]] 
Output: Valid Sudoku: false 
Reason: Duplicate '8' found in the top-left 3×3 sub-grid 
'''
def printBoard(board):
    for i in range(9):
        print(" ".join(board[i][:3]), "|",
              " ".join(board[i][3:6]), "|",
              " ".join(board[i][6:9]))

        if i in [2, 5]:
            print("-------------------------")


board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

valid, reason = validateSudoku(board)

print("Valid Sudoku:", valid)

if valid:
    if solveSudoku(board):
        print("Completed Sudoku:")
        printBoard(board)
    else:
        print("No solution exists")
else:
    print("Reason:", reason)



def validateSudoku(board):
    for i in range(9):
        values = [x for x in board[i] if x != '.']
        if len(values) != len(set(values)):
            return False, f"Duplicate found in row {i + 1}"

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            values = []

            for r in range(i, i + 3):
                for c in range(j, j + 3):
                    if board[r][c] != '.':
                        values.append(board[r][c])

            if len(values) != len(set(values)):
                return False, f"Duplicate found in 3x3 box ({i // 3 + 1}, {j // 3 + 1})"

    for j in range(9):
        values = [board[i][j] for i in range(9) if board[i][j] != '.']

        if len(values) != len(set(values)):
            return False, f"Duplicate found in column {j + 1}"

    return True, "Sudoku is valid"


def solveSudoku(board):
    for i in range(9):
        for j in range(9):

            if board[i][j] == '.':
                for num in "123456789":

                    if num not in board[i]:
                        if all(board[r][j] != num for r in range(9)):

                            boxRow = (i // 3) * 3
                            boxCol = (j // 3) * 3

                            valid = True

                            for r in range(boxRow, boxRow + 3):
                                for c in range(boxCol, boxCol + 3):
                                    if board[r][c] == num:
                                        valid = False

                            if valid:
                                board[i][j] = num

                                if solveSudoku(board):
                                    return True

                                board[i][j] = '.'

                return False

    return True
