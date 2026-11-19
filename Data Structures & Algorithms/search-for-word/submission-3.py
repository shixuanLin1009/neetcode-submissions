#回溯題不是 O(n)。每個起點最多走 4 個方向、深度是 word 長度 L，
#所以時間是 O(m·n·4^L)。空間是 O(L)，包括遞迴深度和 visit 裡最多 L 格。
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows,cols = len(board),len(board[0])

        visit = set()

        def dfs(r,c,i):

            if i == len(word):
                return True
            if r not in range(rows) or c not in range(cols) or (r,c) in visit or board[r][c] != word[i]:
                return False

            visit.add((r,c))
            directions=[[1,0],[-1,0],[0,1],[0,-1]]
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                if dfs(r+dr,c+dc,i + 1):
                    
                    return True
            visit.remove((r,c))     
        
            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True

        return False

# dfs(0,0,0)
#    if i0 >=len(word)3 F
#    if board[r][c] == word[0] T return