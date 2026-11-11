from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
    #用滑動視窗維護由s1組成的hash table 具體來說是 字元頻率
    #對每個 char in s2 判對是否在 出現在hash table中，第一個符合是活動視窗的左邊.下一個符合就往右移，直到完全符合就找到，沒有就失敗
        s1_char_count = Counter(s1)
        left= 0
        for right,char in enumerate(s2):
            if char not in s1_char_count:
                left=right+1
                s1_char_count = Counter(s1)
                continue
            if char in s1_char_count:
                s1_char_count[char]-=1

            while s1_char_count[char]<0:
                s1_char_count[s2[left]]+=1
                left+=1
            
            if right - left + 1 ==len(s1):
                return True
        return False

# s1 = "abc", s2 = "lecabee"
# s1_char_count={a:1,b:1,c:1} | left=0
# for right,char in enumerate(s2) → 
#   right=0  char="l"
#   if char "l" not in s1_char_count={a:1,b:1,c:1} T -> left = 0+1=,1,s1_char_count={a:1,b:1,c:1},continue
#   right=1  char="e"
#   if char "e" not in s1_char_count={a:1,b:1,c:1} T -> left = 1+1=,2,s1_char_count={a:1,b:1,c:1},continue
#   right=2  char="c"
#   if char "c" not in s1_char_count={a:1,b:1,c:1} F | if char "c" in s1_char_count T -> s1_char_count=          {a:1,b:1,c:0} |  while s1_char_count[char] 0 <0 F| if right 2 - left 2 + 1 ==len(s1) 3 F  
#   right=3  char="a"
#   if char "a" not in s1_char_count={a:1,b:1,c:0} F | if char "a" in s1_char_count T -> s1_char_count={a:0,b:1,c:0}  |  while s1_char_count[char] 0 <0 F| if right 3 - left 2 + 1 ==len(s1) 3 F  
#   right=4  char="b"
#   if char "b" not in s1_char_count={a:0,b:1,c:0} F | if char "c" in s1_char_count T -> s1_char_count={a:0,b:0,c:0}  |  while s1_char_count[char] 0 <0 F| if right 4 - left 2 + 1 ==len(s1) 3 T  



                