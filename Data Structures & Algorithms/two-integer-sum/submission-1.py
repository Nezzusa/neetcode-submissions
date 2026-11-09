class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newDict = {}
        rest = target
        indices = []
        for idx, num in enumerate(nums):
            rest = target - num
            if rest in newDict.keys():
                indices = [newDict[rest], idx]
                return indices
            newDict[num] = idx
        return indices
        