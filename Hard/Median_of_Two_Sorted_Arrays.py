class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1+nums2)%2==0:
            listt=nums1+nums2
            listt.sort()
            median=int(len(listt)/2)
            # print((listt[median], listt[median]))
            return (listt[median-1]+listt[median])/2
        else:
            listt=nums1+nums2
            listt.sort()
            median=int(len(listt)/2)
            return listt[median]
            #what kind of mistake i made?
            #1. we can measure the length of list.sort() directly.
            #2. and so much about the variable name.

            #But the things is, i solved this, Alhamdulliah!