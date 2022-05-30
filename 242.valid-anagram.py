#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=starts

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False  
        s_count = {}
        t_count = {}

        for i in range(len(s)) : 
            s_count[s[i]] = 1 + s_count.get(s[i], 0)
            t_count[t[i]] = 1 + t_count.get(t[i], 0)

        for c in s_count :
            if s_count[c] != t_count.get(c, 0) :
                return False 

        return True 



# @lc code=end
