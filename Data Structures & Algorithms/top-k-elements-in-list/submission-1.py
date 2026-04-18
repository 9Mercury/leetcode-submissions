class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(list)
        leng = []
        result = []
        for num in nums:
            res[num].append(num)
        for num,cnt in res.items():
            leng.append([len(cnt),num])
        leng.sort(reverse=True)
        for i in range(k):
            result.append(leng[i][1])
        return result