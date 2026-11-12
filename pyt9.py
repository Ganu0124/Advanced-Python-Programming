''' 
41. Find All Words in Grid You are given: 
	 	A 2D grid board (m × n) of characters  
	 	A list of words words[]  
Goal: Return all words that can be formed in the grid. 
Rules: 
	 	Move in 4 directions: up, down, left, right  
	 	Cannot reuse the same cell in a word  
 	Words must match exact sequence  Constraints: 
•	1 ≤ m, n ≤ 12 
•	1 ≤ words.length ≤ 3 × 10⁴ 
•	1 ≤ word.length ≤ 10 Key Idea 
Use Trie + Backtracking (DFS) 
	 	Trie 	 fast prefix checking  
	 	DFS 	 explore board paths  
 
Example 1 
  
Input: board =  
[ ["o","a","a","n"], 
  ["e","t","a","e"], 
  ["i","h","k","r"],   ["i","f","l","v"] ] 
words = ["oath","pea","eat","rain"] Output:  
["eat","oath"] 
Explanation: 
Found words: 
	 	"oath" 
Path: (0,0) → (0,1) → (1,1) → (2,1) 
	 	"eat" 
Path: (1,3) → (1,2) → (1,1) Not found: 
	 	"pea" → no valid path  
	 	"rain" → cannot form sequence  
 
Example 2: 
  
Input: board =  [ ["a","b"],   ["c","d"] ] 
words = ["abcb"] Output: [] Explanation: 
 	"abcb" requires reuse of 'b' cell   	Reusing cells is not allowed  
Hence, no valid words  
'''

def findWords(board, words):
    trie = {}

    for word in words:
        node = trie
        for ch in word:
            node = node.setdefault(ch, {})
        node["$"] = word

    rows = len(board)
    cols = len(board[0])
    result = []

    def dfs(r, c, parent):
        ch = board[r][c]

        if ch not in parent:
            return

        node = parent[ch]

        if "$" in node:
            result.append(node.pop("$"))

        board[r][c] = "#"

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                if board[nr][nc] != "#":
                    dfs(nr, nc, node)

        board[r][c] = ch

        if not node:
            parent.pop(ch)

    for i in range(rows):
        for j in range(cols):
            dfs(i, j, trie)

    return result


board = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"]
]

words = ["oath", "pea", "eat", "rain"]

print(findWords(board, words))


'''
42.	House Robber: You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. 
Given an integer array nums representing the amount of money of each house, return 
	 	. 
 Constraints: 
	 	1 <= nums.length <= 100 
	 	0 <= nums[i] <= 400 
 
Example 1: 
Input: nums = [1,2,3,1] 
Output: 4 
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3). Total amount you can rob = 1 + 3 = 4. 
 
Example 2: 
Input: nums = [2,7,9,3,1] 
Output: 12 
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1). Total amount you can rob = 2 + 9 + 1 = 12. 
'''
def rob(nums):
    prev2 = 0
    prev1 = 0

    for money in nums:
        current = max(prev1, prev2 + money)
        prev2 = prev1
        prev1 = current

    return prev1


print(rob([1, 2, 3, 1]))
print(rob([2, 7, 9, 3, 1]))



'''
43.	Find Euler Path 
You are given an undirected graph with:  	n vertices labeled from 0 to n-1   	A list of edges edges[i] = [u, v]  
Goal: Determine whether the graph contains an Euler Path. 
Your Task: 
1.	Check if an Euler Path exists  
2.	Print:  
	 	Degree of each node  
	 	Odd degree nodes  
	 	Starting node  
	 	Euler Path sequence (if exists)  
Definition: Euler Path: A path that visits every edge exactly once 
Conditions (Undirected Graph) 
 Graph must be connected 
 Number of vertices with odd degree: 
	 	0 	 Euler Circuit (also valid path)  
	 	2 	 Euler Path  
 	Otherwise 	 Not possible  Constraints: 
•	1 ≤ n ≤ 1000 
Key Idea 
•	Count degrees 	 check conditions 	 build path 
 
Example 1 Input: n = 4 
edges = [[0,1],[1,2],[2,0],[1,3]] Output: 
Euler Path Exists: true Node Degrees: 
0	→ 2 
1	→ 3 
2	→ 2 
3	→ 1 
 
Odd Degree Nodes: [1, 3] 
Start Node: 1 
Euler Path: 1 → 0 → 2 → 1 → 3 Explanation: 
	 	Node 1 and 3 have odd degree 
 Exactly 2 odd nodes → valid  
Start from node 1 
Traverse all edges once 
 
Example 2 Input: n = 4 
edges = [[0,1],[1,2],[2,3]] Output: 
Euler Path Exists: true Node Degrees: 
0	→ 1 
1	→ 2 
2	→ 2 
3	→ 1 
Odd Degree Nodes: [0, 3] 
Start Node: 0 
Euler Path: 0 → 1 → 2 → 3 
Explanation: 
	 	Nodes 0 and 3 are odd 
 Euler Path exists  
 
Example 3  Input: n = 4 
edges = [[0,1],[2,3]] Output: 
Euler Path Exists: false Node Degrees: 
0	→ 1 
1	→ 1 
2	→ 1 
3	→ 1 
Odd Degree Nodes: [0, 1, 2, 3] 
Reason: More than 2 nodes have odd degree and graph is disconnected 
'''


def findEulerPath(n, edges):
    graph = [[] for _ in range(n)]
    degree = [0] * n

    for i, (u, v) in enumerate(edges):
        graph[u].append((v, i))
        graph[v].append((u, i))
        degree[u] += 1
        degree[v] += 1

    odd = [i for i in range(n) if degree[i] % 2 == 1]

    print("Node Degrees:")
    for i in range(n):
        print(i, "->", degree[i])

    print("Odd Degree Nodes:", odd)

    active = [i for i in range(n) if degree[i] > 0]

    if not active:
        print("Euler Path Exists: True")
        print("Start Node: 0")
        print("Euler Path: []")
        return

    visited = set()
    stack = [active[0]]

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)

        for neighbor, edge_id in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)

    if len(visited.intersection(active)) != len(active) or len(odd) not in [0, 2]:
        print("Euler Path Exists: False")
        return

    start = odd[0] if len(odd) == 2 else active[0]

    print("Euler Path Exists: True")
    print("Start Node:", start)

    used = set()
    path = []
    stack = [start]

    while stack:
        node = stack[-1]

        while graph[node] and graph[node][-1][1] in used:
            graph[node].pop()

        if not graph[node]:
            path.append(stack.pop())
        else:
            neighbor, edge_id = graph[node].pop()
            if edge_id not in used:
                used.add(edge_id)
                stack.append(neighbor)

    path.reverse()

    print("Euler Path:", " -> ".join(map(str, path)))


findEulerPath(4, [[0, 1], [1, 2], [2, 0], [1, 3]])



'''
44.	Rotate Image: You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise). You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation. 
Constraints:  	n == matrix.length == matrix[i].length 
	 	1 <= n <= 20 
	 	-1000 <= matrix[i][j] <= 1000 
 
 
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]] 
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]] 
  
45.	You are climbing a staircase. It takes n steps to reach the top. 
Each time, you can either: 
	 	Climb 1 step, or  
 	Climb 2 steps  Your Task: 
1.	Determine the total number of distinct ways to reach the top  
2.	Also print all possible patterns of steps used to reach the top  Each pattern should clearly show how steps are combined Constraints: 
• 1 ≤ n ≤ 45 
 
Example 1: Input: n = 2 Output: Total Ways: 2 Patterns: 
1 + 1 
2 
Explanation: 
There are two ways to climb: 
1	step + 1 step  
2	steps  
 
Example 2: Input: n = 3 Output: 
Total Ways: 3 
Patterns: 
1 + 1 + 1 
1	+ 2 
2	+ 1 
Explanation: 
Ways to reach step 3: 
	 	1 + 1 + 1  
1	+ 2  
2	+ 1  
 
Example 3: Input: n = 4 Output: Total Ways: 5 
Patterns: 
1 + 1 + 1 + 1 
1 + 1 + 2 
1	+ 2 + 1 
2	+ 1 + 1 
2 + 2 
Explanation: 
All valid combinations using steps of 1 and 2 that sum to 4 are listed above. 
'''
def rotate(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

    return matrix


matrix = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]

print(rotate(matrix))



def climbStairs(n):
    result = []

    def backtrack(remaining, current):
        if remaining == 0:
            result.append(current[:])
            return

        if remaining >= 1:
            current.append(1)
            backtrack(remaining - 1, current)
            current.pop()

        if remaining >= 2:
            current.append(2)
            backtrack(remaining - 2, current)
            current.pop()

    backtrack(n, [])

    print("Total Ways:", len(result))
    print("Patterns:")

    for pattern in result:
        print(" + ".join(map(str, pattern)))


climbStairs(2)
climbStairs(3)
climbStairs(4)

''' 