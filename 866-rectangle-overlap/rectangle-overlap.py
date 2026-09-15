class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        a1,b1,a2,b2 = rec1
        a3,b3,a4,b4 = rec2
        if a2 <= a3 or a4 <= a1:
            return False
        if b2 <= b3 or b4 <= b1:
            return False
        return True
        