class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        return[points.sort(),t:=inf,sum(b>(t:=a)for a,b in reversed(points)if b<t)][2]
