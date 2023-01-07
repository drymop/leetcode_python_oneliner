class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        return[t:=-1,min((t:=t+gas[i-1]-cost[i-1],i)for i in range(len(gas)))[1]][t>-2]
