# https://leetcode.com/problems/valid-palindrome

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Stip out non chachters :
        s = " ".join(re.findall("[a-zA-Z0-9]", s))
        # strip out spaces and make chachters lower case
        s = s.replace(" ", "").lower()

        # define 2 pointers, left and right pointers
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
