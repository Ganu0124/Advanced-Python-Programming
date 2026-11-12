r'''
61. Precious Metal Loan Management

A financial institution provides loans against Gold, Silver, and Platinum ornaments. The interest rate is determined based on the type of metal and its purity.

The loan officer must provide the following details to calculate the interest:

1. Metal type – Gold, Silver, or Platinum
2. Purity –
   Gold: 18K, 22K, or 24K
   Silver: 925, 950, or 999
   Platinum: 900, 950, or 999
3. Loan amount
4. Loan tenure in years

The bank wants to develop a Python program using a function:
calculate_interest(metal, purity, amount, tenure)

However, during loan processing, the loan officer may sometimes forget to provide one or more required details.

For example:
• The metal type may be missing.
• The purity/carat may be missing.
• The loan amount may be missing.
• The loan tenure may be missing.
• More than one argument may be missing.
• An invalid metal type or unsupported purity may be entered.

The program should use exception handling to identify and handle these situations without terminating abruptly.

Required Tasks

Write a Python program that:

1. Defines a function calculate_interest(metal, purity, amount, tenure).
2. Determines the applicable interest rate based on the metal type and purity.
3. Calculates the interest using the provided loan amount and tenure.
4. Handles missing function arguments using TypeError.
5. Handles invalid metal types or unsupported purity values using ValueError.
6. Uses try, except, else, and finally blocks appropriately.

Sample Missing Argument Cases

Case                         Function Call

Missing metal type           calculate_interest()
Missing purity               calculate_interest("gold")
Missing amount               calculate_interest("gold", 22)
Missing tenure               calculate_interest("gold", 22, 500000)
Missing multiple arguments   calculate_interest("silver")
Invalid metal                calculate_interest("diamond", 999, 100000, 2)
Invalid purity               calculate_interest("gold", 15, 100000, 2)
'''

# def calculate_interest(metal, purity, amount, tenure):

#     rates = {
#         "gold": {18: 8, 22: 7, 24: 6},
#         "silver": {925: 9, 950: 8, 999: 7},
#         "platinum": {900: 10, 950: 9, 999: 8}
#     }

#     metal = metal.lower()

#     if metal not in rates:
#         raise ValueError("Invalid metal type")

#     if purity not in rates[metal]:
#         raise ValueError("Invalid purity")

#     rate = rates[metal][purity]

#     interest = (amount * rate * tenure) / 100

#     print("Metal:", metal)
#     print("Purity:", purity)
#     print("Interest Rate:", rate, "%")
#     print("Interest Amount:", interest)
#     print("Total Amount:", amount + interest)


# try:
#     calculate_interest("gold", 22, 500000, 2)

# except TypeError as e:
#     print("Missing Argument:", e)

# except ValueError as e:
#     print("Invalid Input:", e)

# else:
#     print("Loan calculation completed successfully")

# finally:
#     print("Loan processing completed")

r'''
62. Rat in a Maze Using Backtracking

A rat is placed at the top-left corner of an N × N maze. The rat needs to reach the destination at the bottom-right corner of the maze.

The maze is represented by a binary matrix where:

• 1 represents an open path through which the rat can move.
• 0 represents a blocked cell through which the rat cannot move.

Write a Python program using the Backtracking technique to find a valid path from the starting position (0, 0) to the destination (N-1, N-1).

The rat can move in four directions: Up, Down, Left, and Right.

Your program should perform the following operations:

1. Initialize an N × N maze containing open and blocked cells.
2. Start the rat from position (0, 0).
3. Check whether the current cell is safe to visit (within maze boundaries, open, and not already visited).
4. Mark the current cell as part of the solution path.
5. Recursively explore the available directions.
6. If a path leads to a dead end, backtrack by unmarking the current cell and exploring another possible path.
7. Display the solution path if the destination is reached.
8. If no valid path exists, display an appropriate message.

Constraints:
• 2 ≤ N ≤ 10
• maze[i][j] can contain either 0 or 1.
• The starting and destination cells must be open.
• A cell cannot be visited more than once in a single path.

Understanding Backtracking

Backtracking follows three main steps:

1. Choose
Select a valid cell and mark it as visited.

2. Explore
Recursively explore the next possible movements.

3. Backtrack
If no valid movement is possible, unmark the cell and try another path.

Example 1

Input:

maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

Output:

Solution Path:

1 0 0 0
1 1 0 0
0 1 0 0
0 1 1 1

Explanation:

The rat starts at (0, 0) and reaches the destination (3, 3) by following the path:

(0,0) → (1,0) → (1,1) → (2,1) → (3,1) → (3,2) → (3,3)

The cells marked 1 in the solution matrix represent the path taken by the rat.

Example 2

Input:

maze = [
    [1, 0, 0],
    [0, 0, 0],
    [0, 0, 1]
]

Output:

No solution exists

Explanation:

The rat cannot reach the destination because all possible paths are blocked.
'''

# def solve_maze(maze, n, x, y, solution):

#     if x == n - 1 and y == n - 1:
#         solution[x][y] = 1
#         return True

#     if (0 <= x < n and 0 <= y < n
#             and maze[x][y] == 1
#             and solution[x][y] == 0):

#         solution[x][y] = 1

#         if solve_maze(maze, n, x + 1, y, solution):
#             return True

#         if solve_maze(maze, n, x, y + 1, solution):
#             return True

#         if solve_maze(maze, n, x - 1, y, solution):
#             return True

#         if solve_maze(maze, n, x, y - 1, solution):
#             return True

#         solution[x][y] = 0

#     return False


# maze = [
#     [1, 0, 0, 0],
#     [1, 1, 0, 1],
#     [0, 1, 0, 0],
#     [1, 1, 1, 1]
# ]

# n = len(maze)

# solution = [[0] * n for _ in range(n)]

# if solve_maze(maze, n, 0, 0, solution):
#     print("Solution Path:")

#     for row in solution:
#         print(*row)
# else:
#     print("No solution exists")


r'''
63. Debugging a Coin-Toss Game

You are developing a Coin Toss Prediction Game for an online gaming application.

The program asks the player to predict whether a randomly tossed coin will result in heads or tails.

The application is giving unexpected results during testing.

As a programmer, you need to use Python debugging techniques to examine the program execution, identify the values of variables at runtime, and verify that the game logic is working correctly.

Debugging Techniques Demonstrated

Technique                 Application in the scenario to inspect

Breakpoint                breakpoint() pauses execution

Variable inspection       p guess, p toss, p result

Type inspection            p type(guess)

Step execution             n executes the next statement

Continue                   c resumes execution

Logical debugging          Verify result == guess

Runtime analysis            Observe randomly generated values
'''

# import random

# guess = input("Predict the coin toss (heads (H) /tails (T) ): ").lower()

# breakpoint()

# toss = random.choice(["h", "t"])

# result = toss

# print("Your Guess:", guess)
# print("Coin Toss:", toss)

# if result == guess:
#     print("Congratulations! You won.")
# else:
#     print("Sorry! You lost.")

# print("Game completed")


r'''
64. Create a printer class and create three printer objects holding the details of printers such as print capacity, color/mono tone, type of printer:

- printer1
- printer2
- printer3

Display their object identities.
'''

# class Printer:

#     def __init__(self, capacity, color, printer_type):
#         self.capacity = capacity
#         self.color = color
#         self.printer_type = printer_type

#     def display(self):
#         print("Print Capacity:", self.capacity)
#         print("Color:", self.color)
#         print("Printer Type:", self.printer_type)


# printer1 = Printer(20, "Color", "Inkjet")
# printer2 = Printer(30, "Mono", "Laser")
# printer3 = Printer(25, "Color", "Laser")

# print("Printer 1")
# printer1.display()
# print("Object Identity:", id(printer1))

# print("\nPrinter 2")
# printer2.display()
# print("Object Identity:", id(printer2))

# print("\nPrinter 3")
# printer3.display()
# print("Object Identity:", id(printer3))


r'''
65. Create a MovieTicket class with a constructor accepting:

- movie_name
- theatre
- seat_number

Create three ticket objects.



'''


# class MovieTicket:

#     def __init__(self, movie_name, theatre, seat_number):
#         self.movie_name = movie_name
#         self.theatre = theatre
#         self.seat_number = seat_number

#     def display(self):
#         print("Movie Name:", self.movie_name)
#         print("Theatre:", self.theatre)
#         print("Seat Number:", self.seat_number)


# ticket1 = MovieTicket("Batman Begins", "PVR", "B2")
# ticket2 = MovieTicket("Batman The Dark Knigh", "INOX", "A1")
# ticket3 = MovieTicket("Batman The Dark Knight Rises", "Cinepolis", "C3")

# print("Ticket 1")
# ticket1.display()

# print("\nTicket 2")
# ticket2.display()

# print("\nTicket 3")
# ticket3.display()

