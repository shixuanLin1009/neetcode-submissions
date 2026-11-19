#13:20
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        preMap = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites :
            preMap[crs].append(pre)

        visit = set()  # 已經確認完成並加入 res 的課程
        cycle = set()  # 當前 DFS 路徑上的課程（用來抓環）

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)

            visit.add(crs)

            res.append(crs)

            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res

# 0->1
# preMap{0:1}
# for 0 in range(numCourses):
#   self.order =[]
#   if not dfs(0)
#       if 0 in visitSet F
#       if preMap[crs] == [] F
#       visitSet.add(crs0)
#       for 1 in preMap[0]:
#           if not dfs(1) -> T
#               if 1 in visitSet -> F
#               if preMap[1] == []-> T
#                   self.order.append(1)
#                   return True