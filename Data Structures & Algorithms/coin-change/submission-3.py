class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # T 不是 O(len(coins))
        #每個金額 0～amount 最多算一次，每次跑過所有硬幣，
        #所以時間是 O(amount × len(coins))；空間是 O(amount)，包括 mem 和遞迴深度。
        
        mem={}

        def f(target):
            
            if target == 0:
                return 0
            if target < 0:
                return -1

            if target in mem: return mem[target]

            best = float('inf')
            for coin in coins:
                sub = f(target - coin)        # answer for what's left
                if sub != -1:
                    best = min(best, 1 + sub)

            if best == float('inf'):
                mem[target] = -1 #「不可能」的結果沒有存進 mem。
                #return -1 前沒寫 mem[target] = -1，
                #同一個湊不出的金額會一直重算。
                #我實測 coins=[4,6]：amount 61 呼叫了 1.5 萬次，101 呼叫了 430 萬次，是指數成長。
                return -1
            else:
                mem[target] = best
                return mem[target]

        return f(amount)

# coins = [1, 3, 4], amount = 6. Just trace f(6)
# mem={}
# f(6)
#   if target6 == 0 F
#   if target6 < 0 F
#   if target6 in mem F
#   best = float('inf')
#   for coin1 in coins:
#       sub = f(target6 - coin1)
#           if target5 == 0 F
#           if target5 < 0 F
#           if target5 in mem: F
#           best = float('inf')
#           for coin1 in coins: 一路到 f(0)
#               sub = f(target1 - coin1)  0 
#                   if target == 0:
#                       return 0
#               if sub != -1 T
#                   best1 = min(best, 1 + sub0)
#           for coin13 in coins: 一路到 f(0)
#               sub = f(target1 - coin3) ->-1  
#                   if target == 0: F
#                   if target < 0: T
#                       return -1
#               if sub != -1 F

