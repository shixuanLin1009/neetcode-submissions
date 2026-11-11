class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_val= []
    def push(self, val: int) -> None:

        self.stack.append(val)
        if not self.min_val or val <= self.min_val[-1]:
            self.min_val.append(val)

    def pop(self) -> None:
 
        if self.stack[-1]==self.min_val[-1]:
            self.min_val.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val[-1]
        
# minStack 只存數字嗎？ 先假定只有數字好了
# solution need O(1) for every function use heap for min? 用哈希存值和指標 min 找最新值？ 
# 如何在 O(1)下 找到最小值？ 若最小值最做後面，stack 可以是O(1)
# 如何讓 最小值一直出現在最後一位？# pop,top,getmin效果差不多吧？
# 放進去之後就要調整？
# stack = [], min=[]-> push1 跟目前的做小值比較輸了就放最後面，沒輸就放前面 
# stack = [1],min=[1]->push 2
# stack = [1,2],min=[1]->push 0
# stack = [1,2,0],min=[1,0]
# stack = [1,2,0],min=[1,0]->pop min_val=[1],stack=[1,2]


# 不能排序
# stack =[4,5,0]
# pop掉最小值 怎辦？
# 維護最小值的陣列？