class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = dict()
        t_hash = dict()
        for i in s:
            if i in s_hash:
                s_hash[i] = s_hash[i] + 1
            else:
                s_hash[i] = 1

        for i in t:
            if i in t_hash:
                t_hash[i] = t_hash[i] + 1
            else:
                t_hash[i] = 1

        return s_hash == t_hash

sln = Solution()
print(sln.isAnagram("jar", "jam"))
