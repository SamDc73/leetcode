class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1] * len(nums)  # Array with the size of nums
        prefix = postfix = 1

        for i in range(len(nums)):
            j = -1 - i
            arr[i] = arr[i] * prefix
            arr[j] = arr[j] * postfix
            prefix = prefix * nums[i]
            postfix = postfix * nums[j]
        return arr
