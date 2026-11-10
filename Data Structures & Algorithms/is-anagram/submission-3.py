from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        word_fre=Counter(s)
        for char in t :
            if char not in word_fre or word_fre[char]==0:
                return False
            word_fre[char]-=1
        return True
        