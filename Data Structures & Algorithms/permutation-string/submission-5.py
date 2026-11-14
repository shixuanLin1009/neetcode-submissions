from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # maintain a sliding window represent s1 word frequent more speci
        # usg this sliding window search substring in s2 O(n)
        # if char in s2 and s1 - char_frequent
        # if all the char_frequent equal 0 return 0 
        # if char not is s2 just pass
        # if nothing find return False
        # Time O(n) Memory O(1)
        char_freq = Counter(s1)

        left = 0
        for right,char in enumerate(s2):
            if char not in char_freq:
                left = right + 1
                char_freq = Counter(s1)
                continue

            char_freq[char]-=1

            while char_freq[char] < 0 :
                char_freq[s2[left]] +=1
                left += 1
            
            if right - left +1 == len(s1):
                return True
        return False

# Output: true
# Input: s1 = "abc", s2 = "lecabee"
# cf={a1,b1,c1}, l=0
# for r=0,char="l"->char"l" not in cf T -> l=r0+1=1 continue
# for r=1,char="e"->char"e" not in cf T -> l=r1+1=2 continue
# for r=2,char="c"->char"c" not in cf F -> cf[c]-=1,cf={a1,b1,c0}->while cf[c]<0 F -> r2-l2+1=1 == len(s1) F
# for r=3,char="a"->char"a" not in cf F -> cf[a]-=1,cf={a0,b1,c0}->while cf[a]<0 F -> r3-l2+1=2 == len(s1) F
# for r=4,char="b"->char"b" not in cf F -> cf[b]-=1,cf={a0,bb,c0}->while cf[b]<0 F -> r4-l2+1=3 == len(s1) T->return True



