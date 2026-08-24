

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        char_map_s={}
        char_map_t={}

        for i in s:
            char_map_s[i]=char_map_s.get(i,0)+1

        for i in t:
            char_map_t[i]=char_map_t.get(i,0)+1

        if char_map_t==char_map_s:
            return True

        else:
            return False

        