class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i, num in enumerate(nums):
            temp = target - num
            if temp in seen:
                j = seen[temp]
                return [j,i]
            else:
                seen[num] = i