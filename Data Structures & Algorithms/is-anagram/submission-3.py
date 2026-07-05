class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_l = list(s)
        t_l = list(t)
        for i in range(len(s)):
            if s_l[i] in t_l:
                t_l.remove(s_l[i])
            else:
                return False
        return True