class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        

        if not t:
            return False       
        if not s:
            return True

        mi = 0
        for ele in s:
            for j in range(mi, len(t)):
                if t[j] == ele:
                    mi = j+1
                    break
            else:
                return False

        return True
    


