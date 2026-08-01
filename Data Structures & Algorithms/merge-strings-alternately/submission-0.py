class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        a = 0
        b = 0
        s = ""
        for i in range(max(len(word1), len(word2))):
            if a<len(word1):
                s+=word1[a]
                a+=1
            if b<len(word2):
                s += word2[b]
                b +=1
        
        return s