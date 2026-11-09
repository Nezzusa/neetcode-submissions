class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        if len(s) != len(t):
            return False

        for ls in s:
            if ls not in count.keys():
                count[ls] = 1
            else:
                count[ls] += 1

        for lt in t:
            if lt not in count.keys():
                return False
            else:
                count[lt] -= 1
        
        is_zero = all(val == 0 for val in count.values())
        return is_zero
    