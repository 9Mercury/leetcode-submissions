class Solution:
    def isPalindrome(self, s: str) -> bool:
        prefix = []
        postfix = []
        for i in s:
            if (i=='?' or i=='!' or i == ' ' or i == ','or i == "'" or i == '"' or i == '.'or i == ':'or i == ';'):
                continue
            prefix.append(i.lower())
        for j in range(len(s)-1,-1,-1):
            if (s[j]=='?' or s[j]=='!' or s[j]==' 'or s[j] == ','or s[j] == "'" or s[j] == '"' or s[j] == '.' or s[j] == ':' or s[j] == ';'):
                continue
            postfix.append(s[j].lower())
        return postfix==prefix
        