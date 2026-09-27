# My solution:
"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

# First attempt

def maxProfit(self, prices: list[int]) -> int:
    profit: int =0
    for i in range(len(prices)):
        for j in range(len(prices)):
            if (j>i and prices[j]-prices[i]>profit):
                profit=prices[j]-prices[i]

    return profit


# More time efficient solution

def maxProfit(self, prices: list[int]) -> int:
    left: int=0
    right: int = 1
    profit: int =0
    currProfit: int=0
    while (right<len(prices)):
        if (prices[left]<prices[right]):
            currProfit = prices[right]-prices[left]
            profit = max(profit,currProfit)
        else:
            left=right

        right+=1

    return profit


#Another more time efficient solution
def maxProfit(self, prices: list[int]) -> int:
    buy: int=prices[0]
    profit=0
    currProfit=0
    for price in prices[1:]:
        if (price>buy):
            currProfit = price-buy
            profit = max(profit,currProfit)
        else:
            buy = price

    return profit



"""
    THOUGHT PROCESS:
At first my thought process was to immediately resort to a brute force method regarding
a nested for loop solution, however I found out quickly that such a solution would likely
exceed the time limit.

Instead a two pointer strategy would be better. Strategy from NeetCode

Instead of using nested for loops we want to use a singular while loop that will break when the right pointer
reaches the max length of the list. The main logic is to first check if the right pointer has a greater value than the left
pointer, if it does we set the profit variable equal to the difference of the right and left pointer. And if the right pointer is instead
less than, we can simply set the left pointer equal to the right. We always add 1 to the right pointer for every loop. 

For the third go, instead of using two different variables as pointers, we can instead have one pointer be a variable
and the other be the iritable variable from the for loop that is looping from the prices list, starting with the 
1 index.
"""

