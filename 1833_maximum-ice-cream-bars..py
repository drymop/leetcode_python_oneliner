class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        return costs.sort()or sum(c<=coins>(coins:=coins-c)for c in costs)
      
# Explanation
# Sort the costs in ascending order, then greedy pick
#
# c <= coins > (coins:=coins-c)
# - evaluate to 0 if c > coins (don't have enough to buy next ice cream)
# - evaluate to 1 if c <= coins (can buy next ice cream) and also execute coins = coins - c
# sum over all of that will give the number of ice cream that can be bought.
