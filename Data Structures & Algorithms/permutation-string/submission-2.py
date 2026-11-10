from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_counts = Counter(s1)
        left = 0
        for right in range(len(s2)):

            if s2[right] not in char_counts:
                left = right + 1
                char_counts = Counter(s1)
                continue
            char_counts[s2[right]]-=1

            while char_counts[s2[right]] < 0: 
                char_counts[s2[left]]+=1
                left+=1
                

            if  right-left+1 == len(s1):
                return True
            
        return False

