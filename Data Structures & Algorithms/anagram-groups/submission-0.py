class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dir = defaultdict(list)
        for s in strs:
            Ssorted = ''.join(sorted(s))
            dir[Ssorted].append(s)
        return list(dir.values())
        