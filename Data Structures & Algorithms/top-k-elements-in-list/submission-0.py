class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n,0) + 1
        sortedCount = sorted(count.items(), key=lambda item:item[1], reverse=True)
        return [key for key, count in sortedCount[:k]]
