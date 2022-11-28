class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        return (lambda P,L:[[p for p in P if L[p]==c]for c in(0,1)])(sorted({p for m in matches for p in m}),Counter(l for _,l in matches))

#=======================
# Explanation

# Fairly straight-forward, only need to use lambda to store temp variables
# P=players and L=losses

# Original solution
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = sorted({p for m in matches for p in m})
        losses = Counter(l for _,l in matches)
        return [[p for p in players if losses[p]==c]for c in(0,1)]