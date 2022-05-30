#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive = 0
        n = 0
        for n in nums :
            if nums[n] == nums[n+1]:
                consecutive = consecutive + 1
            n = n + 1
        print(consecutive)
# @lc code=end

