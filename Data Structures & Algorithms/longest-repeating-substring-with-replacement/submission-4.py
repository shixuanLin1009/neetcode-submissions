from collections import Counter,defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        seen = defaultdict(int)
        max_len=0
        for right in range(len(s)): 
            seen[s[right]]+=1

            max_freq = max(seen, key=seen.get) 
            len_sub_s = sum(seen.values())
            replace = len_sub_s - seen[max_freq]

            while replace > k:
                seen[s[left]]-=1
                left+=1
                max_freq = max(seen, key=seen.get) 
                len_sub_s = sum(seen.values())
                replace = len_sub_s - seen[max_freq]
            cur_left = right-left +1
            max_len = max(max_len,cur_left) 

        return max_len
            
