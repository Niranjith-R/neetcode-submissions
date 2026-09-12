class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        #split based on gender
        count=0
        for i in details:
            if int(i[-4:-2]) > 60:
                count += 1
            
        return count