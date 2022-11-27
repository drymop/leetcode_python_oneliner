class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return (lambda D:next([i,D[target-n]]for i,n in enumerate(nums) if D.get(target-n,i)!=i))({x:i for i,x in enumerate(nums)})