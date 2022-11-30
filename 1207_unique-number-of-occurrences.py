class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(c:=Counter(arr))==len({*c.values()})
