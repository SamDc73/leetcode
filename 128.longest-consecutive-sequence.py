# we're gonna reach the desired sequance from the smallest value to the biggest
# soulation taken form https://leetcode.com/problems/longest-consecutive-sequence/discuss/41057/Simple-O(n)-with-Explanation-Just-walk-each-streak
# https://leetcode.com/problems/longest-consecutive-sequence


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = set(nums)
        best = 0
        for x in nums:
            # Make sure your not reaching high number of what might be desired sequance^1
            if x - 1 not in nums:  # ELiminate each num have a higher value
                y = x + 1  # check for the higher values
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best


print(longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))


'''
1) in this example you don't skip 100 because it's not part of the end sequance, but 4 is skipped because 
it might be part of the desired sequance (since ther is a smaller number `3` in the set)
'''
