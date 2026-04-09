class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        longest=0
        lasts=float("-inf")
        for i in range(0,len(nums)):
            if nums[i]-1==lasts:
                count+=1
                lasts=nums[i]
            elif nums[i] !=lasts:
                count=1
                lasts=nums[i]
            longest=max(longest,count)
        return longest            
