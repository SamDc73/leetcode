#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res, maxCount = 0, 0

        for i in nums:
            count[i] = 1 + count.get(i, 0)
            if count[i] > maxCount:
                res = i
            else:
                res
            maxCount = max(count[i], maxCount)

        return res


# @lc code=end
