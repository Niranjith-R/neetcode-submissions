class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_l = list(s)
        t_l = list(t)
        for i in s:
            if i in t_l:
                t_l.remove(i)
            else:
                return False
        return True