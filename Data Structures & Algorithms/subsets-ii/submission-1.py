class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def subset(idx,arr):
            if idx==len(nums):
                res.append(arr[::])
                return
            arr.append(nums[idx])
            subset(idx+1,arr)
            arr.pop()
            while idx+1<len(nums) and nums[idx]==nums[idx+1]:
                idx+=1
            subset(idx+1,arr)
        subset(0,[])
        return res