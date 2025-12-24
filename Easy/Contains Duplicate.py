class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if set(nums)!=nums and len(set(nums))!=len(nums):
            return True
        else:
            return False