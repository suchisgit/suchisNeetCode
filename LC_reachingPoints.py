class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if sx>tx or sy>ty:
            return False
        if sx==tx:
            if (ty-sy)%sx==0:
                return True
            else:
                return False
        if sy==ty:
            if (tx-sx)%sy==0:
                return True
            else:
                return False
        if tx>ty:
            return Solution.reachingPoints(self,sx,sy,tx%ty,ty)
        elif tx<ty:
            return Solution.reachingPoints(self,sx,sy,tx,ty%tx)
        else:
            return False
