class Solution:
    def scoreOfString(self, s: str) -> int:
        
        a = 0
        score = 0

        while a + 1 < len(s):
            su = ord(s[a]) - ord(s[a+1])
            su = abs(su)
            score+=su
            a+=1


        return score