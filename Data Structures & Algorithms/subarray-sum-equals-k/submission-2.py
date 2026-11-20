class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cur = 0
        prefixsum={0:1}

        for num in nums:
            cur += num
            diff  = cur - k
            res += prefixsum.get(diff,0)
            prefixsum[cur] = 1 + prefixsum.get(cur,0)
        return res