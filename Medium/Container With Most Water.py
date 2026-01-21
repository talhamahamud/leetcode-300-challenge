class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        maxx=0

        while left<right:
            width=right-left

            current=width*min(height[left], height[right])
            maxx=max(maxx, current)
            if height[left]<height[right]:
                left=left+1
            else:
                right=right-1

        return maxx