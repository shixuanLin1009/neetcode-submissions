class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #dfs visit不要退回給其他路徑的用　# T(V+E)

        preMap={i:[]for i in range(numCourses)} #做　i 的先修的對應表
        for crs,pre in prerequisites:
            preMap[crs].append(pre)


        cycle=set() #找cycle
        visit=set() # 確認可以走的


        def dfs(i):

            if i in cycle: #如果出現圈就結束
                return False
            if  i in visit:# 確認可以修就True
                return True
           
            cycle.add(i)

            for pre in preMap[i]:
                if  not dfs(pre):return False

            visit.add(i)
            cycle.remove(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i):return False

        return True