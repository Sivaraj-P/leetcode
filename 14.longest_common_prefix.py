#14.longest_common_prefix

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res=""
        for i in range (len(strs[0])):
            for s in strs:
                if i==len(s) or strs[0][i]!=s[i]:
                    return res
            res+=strs[0][i]

        return res