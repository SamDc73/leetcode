def productExceptSelf(nums):
    if not nums:
        return False

    arr = [1] * len(
        nums
    )  # To print an array filled with ones that have the same size of the given array
    pi = pj = 1

    for i in range(len(nums)):
        j = -1 - i
        arr[i] = arr[i] * pi
        print(pj)
        arr[j] = arr[j] * pj
        # print(arr[j])
        pi = pi * nums[i]
        pj = pj * nums[j]

    return arr


productExceptSelf(nums=[1, 2, 3, 4])
# print(productExceptSelf(nums=[1, 2, 3, 4]))
