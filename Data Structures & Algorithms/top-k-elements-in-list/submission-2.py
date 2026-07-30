class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        n = len(nums)
        bucket = [[] for _ in range(0, n+1)]
        for num, count in count.items():
            bucket[count].append(num)
        res = []
        for count in range(n,0,-1):
            for n in bucket[count]:
                res.append(n)
                if len(res) == k:
                    return res
