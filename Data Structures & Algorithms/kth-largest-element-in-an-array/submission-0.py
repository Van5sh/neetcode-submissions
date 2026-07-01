class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ks=nums[:k]
        heapq.heapify(ks)
        for x in nums[k:]:
            if x>ks[0]:
                heapq.heapreplace(ks,x)
        return ks[0]
        