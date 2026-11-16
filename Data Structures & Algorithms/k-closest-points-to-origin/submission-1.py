class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #取所有點當中k個距離原點最小的
        res=[]

        def cal_distance(x,y):
            return (x - 0)**2 + (y - 0)**2
        
        distances = [(cal_distance(point[0],point[1]),point[0],point[1]) for point in points]#O(n)
        heapq.heapify(distances)#O(n)
        print(distances)
        for _ in range(k):#O(klogn)
            point = heapq.heappop(distances)
            res.append([point[1],point[2]])

        return res

# Output: [[0,2]]

# Input: points = [[0,2],[2,2]], k = 1
# distances = {(2,0,2),(2(2),2,2)}
# for _ in range k ->
#   point=(2,0,2),res=[[0,2]]
# return res