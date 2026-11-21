class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        


        res = []
        # right, down,left,top  
        directions = [[0,1],[1,0],[0,-1],[-1,0]]

        rows, cols = len(matrix),len(matrix[0])
        visit = set()
        r, c =0, 0
        res.append(matrix[r][c])
        visit.add((r,c))
        while len(res) != rows*cols:
            for dr,dc in directions:
                while r + dr in range(rows) and c +dc in range(cols) and (r + dr,c +dc) not in visit:
                    r, c = r + dr, c +dc
                    res.append(matrix[r][c])
                    visit.add((r,c))
        return res
            
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
# r, c =0, 0 , visit = set(),res = [],directions = [[0,1],[1,0],[0,-1],[-1,0]]
# for 0, 1 in directions:
#    while 0 in range(3) and 0 in range(3) and (0,0) not in visit:
#       res.append(1), res = [1]
#       visit.add((0,0)),visit=((0,0))
#       0, 1 = 0 + 0, 0 + 1
#    while 0 in range(3) and 1 in range(3) and (0,1) not in visit:
#       res.append(2),res = [1,2]
#       visit.add((0,1)),visit=((0,0),(0,1))
#       0, 2 = 0 + 0, 1 + 1 
#    while 0 in range(3) and 2 in range(3) and (0,2) not in visit:
#       res.append(3),res = [1,2,3]
#       visit.add((0,0)),visit=((0,0),(0,1),(0,2))
#       0, 3 = 0 + 0, 2 + 1 
#    while 0 in range(3) and 3 in range(3) and (0,3) not in visit F
#    0, 2 = 0 - 0, 3 - 1
# for 1, 0 in directions:
#    while 0 in range(3) and 2 in range(3) and (0,) not in visit:
#       res.append(1), res = [1]
#       visit.add((0,0)),visit=((0,0))
#       0, 1 = 0 + 0, 0 + 1
#    while 0 in range(3) and 1 in range(3) and (0,1) not in visit:
#       res.append(2),res = [1,2]
#       visit.add((0,1)),visit=((0,0),(0,1))
#       0, 2 = 0 + 0, 1 + 1 
#    while 0 in range(3) and 2 in range(3) and (0,2) not in visit:
#       res.append(3),res = [1,2,3]
#       visit.add((0,0)),visit=((0,0),(0,1),(0,2))
#       0, 3 = 0 + 0, 2 + 1 
#    while 0 in range(3) and 3 in range(3) and (0,3) not in visit F
#    0, 2 = 0 - 0, 3 - 1