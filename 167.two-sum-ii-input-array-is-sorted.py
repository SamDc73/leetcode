'''
We will have two pointers left and right 
if the sum of the indeces of the tow pointer is : 
    1. bigger than the target shift the lef pointer to the right 
    2. samaller than the target shift the right pointer to the left
    3. equels the target return true
'''


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Define the left and the right pointers
        l = 0
        r = len(numbers) - 1

        # it's true that means we didn't get through all possible combinations yet
        while l < r:
            currentSum = numbers[l] + numbers[r]
            if currentSum > target:
                r = r - 1
            elif currentSum < target:
                l = l + 1
            else:
                return (l + 1, r + 1)
