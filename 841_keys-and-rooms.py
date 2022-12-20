class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        return (lambda S:all(S and not(lambda r:S.extend(rooms[r]or[])or rooms.__setitem__(r,None))(S.pop())for _ in iter(int,1))or all(r is None for r in rooms))([0])
