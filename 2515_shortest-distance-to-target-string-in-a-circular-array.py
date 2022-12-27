class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        return min((min(abs(i-startIndex),len(words)-abs(i-startIndex))for i,w in enumerate(words)if w==target),default=-1)
