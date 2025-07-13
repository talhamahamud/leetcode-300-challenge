from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        element=Counter(nums)
        se=[i for i, counter in element.items() if counter==1]
        return se[0]