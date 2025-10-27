# 🔗 https://leetcode.com/problems/palindrome-number/

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_elem=Counter(nums)
        listt=[i for i, count in num_elem.items() if count>(len(nums)/2)]
        return listt[0]

        # i learn about the collections and Counter by solving the previous
        #problem, it return the total number of i, in a list repeated.


# This the another solution.
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_count=0
        main=0
        for i in set(nums):
            if nums.count(i)>max_count:
                max_count=nums.count(i)
                main=i
                
        return main
