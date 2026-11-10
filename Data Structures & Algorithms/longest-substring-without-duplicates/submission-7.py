class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len=0
        seen=set()
        left=0
        for right in range(len(s)):
            while s[right] in seen :
                seen.discard(s[left])
                left+=1
            else:
                seen.add(s[right])
            cur_len=right-left+1
            max_len=max(max_len,cur_len)
        return max_len
        
            