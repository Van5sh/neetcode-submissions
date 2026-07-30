class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.dfs(nums[1:]),self.dfs(nums[:-1]))
    def dfs(self,nums):
        if len(nums)==1:
            return nums[0]
        if not nums:
            return 0
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for idx in range(2,len(nums)):
            dp[idx]=max(dp[idx-1],nums[idx]+dp[idx-2])
        return dp[-1]
