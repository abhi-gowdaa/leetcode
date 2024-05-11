class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {
            # num: index
        }
        for i, num in enumerate(nums):
            diff = target - num
            if diff in mapping:
                return [mapping[diff],i]
            mapping[num]=i
        return
            