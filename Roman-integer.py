
class Solution:
    def romanToDecimal(self, S): 
        # code here
        Roman = { "I": 1 , "V": 5, "X":10, "L": 50, "C":100, "D":500, "M": 1000}
        res = 0
        for i in range(len(S)):
            if i + 1 < len(S) and Roman[S[i]] < Roman [S[i+1]] :
                res -= Roman[S[i]]
            else:
                res += Roman[S[i]]
        return res
        
