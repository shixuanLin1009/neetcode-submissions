from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map=defaultdict(list)
        
        for word in strs:
            char_count=[0]*26
            for char in word:
                char_count[ord(char)-ord('a')]+=1
            hash_map[tuple(char_count)].append(word)
        res=[]
        for key,value in hash_map.items():
            res.append(value)
        return res