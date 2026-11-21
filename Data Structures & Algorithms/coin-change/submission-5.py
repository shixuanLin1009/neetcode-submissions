class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # state 是 dp[i] = 湊出 i 元的最少硬幣數，
        #transition 是 dp[i] = min(1 + dp[i - c])。寫出來
        
        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        for i in range(amount+1):
            
            for c in coins:
                if i - c >= 0:
                    dp[i]=min(dp[i], 1 + dp[i - c])
    
        return -1 if dp[amount]== float("inf") else dp[amount]
    
        # namecheck =coins,amount,dp,i,c