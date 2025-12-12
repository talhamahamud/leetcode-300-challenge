class Solution:
    def maxSubArray(self, nums):
        max_sum=nums[0]
        current_sum=0

        for i in nums:
            current_sum = current_sum+i
            max_sum=max(max_sum, current_sum)

            if current_sum<0:
                current_sum=0
        return max_sum
 