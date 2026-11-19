class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        char_cnt = collections.Counter(s1)
        left,right = 0,0
        while right < len(s2):
            if s2[right] not in char_cnt:
                left = right + 1
                char_cnt = collections.Counter(s1)
                right += 1
                continue
            
            char_cnt[s2[right]] -= 1

            while left < right and char_cnt[s2[right]] < 0:
                char_cnt[s2[left]]+=1
                left+=1

            if (right - left +1) == len(s1):
                return True

            right += 1 
        return False
# True
# s1 = "ab"、s2 = "eibcba"
# char_cnt = collections.Counter(s1)={a:1b:1}
# left,right = 0,0
# while right 0 < len(s2) 6 T
#   if s2[right0]e not in char_cnt T
#       left0 = right0
#       char_cnt = collections.Counter(s1)
#       right += 1
#       continue
# while right 1 < len(s2) 6 T
#   if s2[right1]i not in char_cnt T
#       left1 = right1
#       char_cnt = collections.Counter(s1)
#       right += 1
#       continue
# while right 2 < len(s2) 6 T
#   if s2[right2]b not in char_cnt F
#   char_cnt[rignt] -= 1,char_cnt={a:1,b:0}
#