# https://leetcode.com/problems/top-k-frequent-elements


# def topKFrequent(nums, k):
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
count = {}  # {'num' : 'counut'}
    freq = [
        [] for i in range(len(nums) + 1)
    ]  # To Return the size of the freq based on the given list

    # TO count each int and add it count{}
    for n in nums:
        count[n] = 1 + count.get(n, 0)

    # based on count{} make a list 'where the count is the index'
    for n, c in count.items():
        freq[c].append(n)

    # Return the Results
    res = []
    for i in range(
        len(freq) - 1, 0, -1
    ):  # You need to approch the freq form the end to the beging
        if (
            freq[i] != [] and len(res) != k
        ):  # TO strip out empty entries in the freq list and to know when should i Stop
            for n in freq[
                i
            ]:  # Each entry in the freq is a list (because the index is the count is the index )
                res.append(n)
    return res


# print(topKFrequent([3, 0, 1, 0], k=1))
