class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans,start,current_sum=float("inf"),0,0
        for right in range(len(nums)):
            current_sum+=nums[right]
            while current_sum>=target:
                ans=min(ans,right-start+1)
                current_sum-=nums[start]
                start+=1
        return ans if ans!=float("inf") else 0
    
    
