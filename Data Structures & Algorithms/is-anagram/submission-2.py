class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = 0
        l = []
        for k in t:
            l.append(k)
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            for j in range(len(l)):
                if s[i]==l[j]:
                    counter += 1
                    l.pop(j)
                    break
        if counter == len(s):
            return True
        else:
            return False