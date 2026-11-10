from collections import Counter,defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        seen = defaultdict(int)
        max_len=0
        max_freq=0
        for right in range(len(s)): 
            seen[s[right]]+=1

            max_freq = max(max_freq, seen[s[right]])
            len_sub_s = right - left + 1

            while (right - left + 1) - max_freq > k:
                seen[s[left]]-=1
                left+=1
        
            cur_left = right-left +1
            max_len = max(max_len,cur_left) 

        return max_len
            
