class Solution:
    def rob(self, nums: List[int]) -> int:
        # 處理長度 1 或 2 的邊界情況
        if len(nums) <= 2:
            return max(nums)

        def rob_linear(houses: List[int]) -> int:
            dp = [0] * len(houses)
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])  # 修正點 3：前兩間取較大值
            
            for i in range(2, len(houses)):
                dp[i] = max(houses[i] + dp[i - 2], dp[i - 1])
            return dp[-1]

        # 分別計算「不搶最後一間」與「不搶第一間」
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))