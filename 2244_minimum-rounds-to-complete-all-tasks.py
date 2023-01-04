class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        return max(-1,sum(-inf if n<2 else(n+2)//3 for n in Counter(tasks).values()))
