class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 用stack存 等到條件成立（比自己更大）的值，當遇到時，index相減就是答案
        res=[0]*len(temperatures)
        stack = []

        for i, val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                tepVal,tepI = stack.pop()
                I = i - tepI
                res[tepI]=I
            stack.append([val,i])
        return res
#expect: [1,4,1,2,1,0,0]
#Input: temperatures = [30,38,30,36,35,40,28]
#res=[0,0,0,0,0,0,0], stack=[]
#i=0,val=30 -> while stack=[] -> stack=[[30,0]]
#i=1,val=38 -> while val=30 > stack[-1][0]=30 ->tepVal=30,tepI=0,res[0]=1-0 -> stack=[[38,1]]
#i=2,val=30 -> while val=30 <stack[-1][0]=38 ->stack=[[38,1],[30,2]]
#Time = O(n) for each element in temp ,Spcae:O(n) for maintail stack