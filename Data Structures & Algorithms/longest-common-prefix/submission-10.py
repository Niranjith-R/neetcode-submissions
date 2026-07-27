class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        count = 1
        val = strs[0][:count]
        final = False

        if len(strs) == 1:
            return strs[0]



        while final != True and count <= len(strs[0]):
            val = strs[0][:count]
            for i in strs:
                if len(i)==1:
                    return i
                if i[:count] != val:
                    return strs[0][:count-1]
                    final = True
                    break
                    
            count+=1
        return strs[0][:count-1]    