class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = {}  # hash table: number → last index where we saw it

        for i, num in enumerate(nums):
            if num in seen:
                if abs(i - seen[num]) <= k:
                    return True
            seen[num] = i  # always update to the most recent index

        return False