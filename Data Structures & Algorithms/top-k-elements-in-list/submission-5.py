class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if(len(nums)==1):
            return [nums[0]]
        counts={}
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if nums[i]==nums[j]:
                    count+=1
            counts[nums[i]]=count
        ans=sorted(counts,key=lambda x:counts[x],reverse=True)
        return ans[:k]