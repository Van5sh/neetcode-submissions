class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def findSum(start,ans,total):
            if total==target:
                res.append(ans.copy())
                return
            if total>target:
                return
            for i in range(start,len(nums)):
                ans.append(nums[i])
                findSum(i, ans, total + nums[i])
                ans.pop()
        findSum(0,[],0)
        return res
