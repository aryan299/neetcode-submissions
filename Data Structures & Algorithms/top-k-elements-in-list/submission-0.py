class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        heap = []
        for value,count in freq.items():
            heapq.heappush(heap, (count,value))
            if len(heap) > k:
                heapq.heappop(heap)
        return [j for i,j in heap]