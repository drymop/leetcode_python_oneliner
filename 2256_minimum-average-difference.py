class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        return (lambda s,t:min((abs((t:=t+n)//(i+1)-(s-t)//(len(nums)-i-1 or 1)),i)for i,n in enumerate(nums))[1])(sum(nums),0)
