class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def permutation(idx):
            if idx==len(nums):
                res.append(nums[:])
                return
            for i in range(idx,len(nums)):
                nums[idx],nums[i]=nums[i],nums[idx]
                permutation(idx+1)
                nums[idx],nums[i]=nums[i],nums[idx]
        permutation(0)
        return res
                   
