''' 11. Missing Number: Given an array nums containing n distinct numbers in the range [0, n], 
return 	 
 Constraints:  	n == nums.length  	1 <= n <= 104 
	 	0 <= nums[i] <= n 
	 	All the numbers of nums are unique. 
 
Example 1: 
Input: nums = [3,0,1] Output: 2 Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums. 
 
Example 2: 
Input: nums = [0,1] Output: 2 
Explanation: 
 
n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums. 
 
Example 3: 
Input: nums = [9,6,4,2,3,5,7,0,1] 
Output: 8 Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums. 
  

def missingNumber(nums):
    n = len(nums)
    total = n * (n + 1) // 2
    return total - sum(nums)


nums = [3, 0, 1]

print("Input:", nums)
print("Output:", missingNumber(nums))



12.	Coin Change: You are given an integer array coin representing coins of different denominations and an integer amount representing a total amount of money. 
Return 	. If that amount of money cannot be made up by any combination of the coins, return -1. 
You may assume that you have an infinite number of each kind of coin. 
 Constraints: 
	 	1 <= coins.length <= 12 
	 	1 <= coins[i] <= 231 - 1 
0	<= amount <= 104 
 
Example 1: 
Input: coins = [1,2,5], amount = 11 
Output: 3 
Explanation: 11 = 5 + 5 + 1 
 
Example 2: 
Input: coins = [2], amount = 3 
Output: -1 
 
Example 3: 
Input: coins = [1], amount = 0 
Output: 0 
  

def coinChange(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[amount] == amount + 1:
        return -1

    return dp[amount]


coins = [1, 2, 5]
amount = 11

print("Coins:", coins)
print("Amount:", amount)
print("Output:", coinChange(coins, amount))


13.	There are n cities connected by some number of flights. You are given an 
array flight where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei. 
You are also given three integers src, dst, and k, return 	 	 src 	 dst  k 	 If there is no such route, return -1. 
 Constraints: 
	 	2 <= n <= 100 
0	<= flights.length <= (n * (n - 1) / 2)  	flights[i].length == 3  	0 <= fromi, toi < n  	fromi != toi 
1	<= pricei <= 104 
	 	There will not be any multiple flights between two cities. 
 	0 <= src, dst, k < n  	src != dst 
 
Example 1: 
  
Input:  
n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1 
Output: 700 
Explanation: 
The graph is shown above. 
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700. 
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops. 
 
Example 2: 
  
Input:  
n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1 
Output: 200 
Explanation: 
The graph is shown above. 
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200. 
 
Example 3: 
  
Input:  
n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0 
Output: 500 
Explanation: 
The graph is shown above. 
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500. 

def cheapestFlight(n, flights, src, dst, k):
    cost = [float('inf')] * n
    cost[src] = 0

    for i in range(k + 1):
        temp = cost.copy()

        for u, v, price in flights:
            if cost[u] != float('inf'):
                temp[v] = min(temp[v], cost[u] + price)

        cost = temp

    if cost[dst] == float('inf'):
        return -1

    return cost[dst]


n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100],
           [1, 3, 600], [2, 3, 200]]

src = 0
dst = 3
k = 1

print("Source:", src)
print("Destination:", dst)
print("Maximum Stops:", k)
print("Output:", cheapestFlight(n, flights, src, dst, k))


14. Merge k Sorted Lists 
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order. 
 
Constraints: 
k == lists.length 
	 	0 <= k <= 104 
 	0 <= lists[i].length <= 500  	-104 <= lists[i][j] <= 104  	lists[i] is sorted in ascending order. 
	 	The sum of lists[i].length will not exceed 104. 
  
Example 1: 
Input: lists = [[1,4,5],[1,3,4],[2,6]] 
Output: [1,1,2,3,4,4,5,6] 
Explanation: The linked-lists are: 
[ 1->4->5, 
  1->3->4, 
  2->6 ] merging them into one sorted linked list: 
1->1->2->3->4->4->5->6 
 
Example 2: 
Input: lists = [[4,5],[1,6]] 
Output: [1,4,5,6] 
 
import heapq

def mergeKLists(lists):
    result = []

    for lst in lists:
        result.extend(lst)

    heapq.heapify(result)

    merged = []

    while result:
        merged.append(heapq.heappop(result))

    return merged


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]

print("Input:", lists)
print("Output:", mergeKLists(lists))


15. Reverse Bits: Reverse bits of a given 32 bits signed integer. 
Constraints:  	0 <= n <= 231 - 2  	n is even. 
 
Example 1: 
Input: n = 43261596 
Output: 964176192 
Explanation: 
Integer 	Binary 
43261596 	00000010100101000001111010011100
964176192	 00111001011110000010100101000000
 
Example 2: 
Input: n = 2147483644 Output: 1073741822 Explanation: 
Integer 	Binary 
2147483644	 01111111111111111111111111111100
1073741822	 00111111111111111111111111111110


def reverseBits(n):
    result = 0

    for i in range(32):
        result = result * 2 + n % 2
        n = n // 2

    return result


n = 43261596

print("Input:", n)
print("Output:", reverseBits(n))
'''