class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        #對每個格子的四個方向做bfs T(mn 4^L) mn 是格子長寬，Ｌ是word長度
        visit = set()
        rows, cols = len(board), len(board[0])


        def bfs(r,c,i): #代表這個格子當起點找得到word嗎
            if board[r][c] != word[i]:return False
            if i == len(word)-1 : return True
           

            visit.add((r,c))
            directions = [[1,0],[-1,0],[0,1],[0,-1]]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr in range(rows) and nc in range(cols) and (nr, nc) not in visit:
                    if bfs(nr,nc,i+1):
                        return True
                        
            visit.remove((r,c))

            return False
                



        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if bfs(r,c,0):
                        return True
        return False