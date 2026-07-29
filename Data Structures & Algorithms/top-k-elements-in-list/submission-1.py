class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n,0) + 1
        n = len(nums)
        bucket = [[] for _ in range(n+1)]
        for num, count in count.items():
            bucket[count].append(num)
        res =[]
        for i in range(n,0,-1):
            for j in bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res