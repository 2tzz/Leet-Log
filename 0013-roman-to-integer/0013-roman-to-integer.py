class Solution:
    def romanToInt(self, s: str) -> int:
        I = 1
        V = 5
        X = 10
        L = 50
        C = 100
        D = 500
        M = 1000
        total = 0
        val = []
        keyz = list(s)
        for key in keyz :
            if key == 'I' :
                val.append(1)
            elif key == 'V' :
                val.append(5)
            elif key == 'X' :
                val.append(10)
            elif key == 'L' :
                val.append(50)
            elif key == 'C' :
                val.append(100)
            elif key == 'D' :
                val.append(500)
            elif key == 'M' :
                val.append(1000)
        print(val , len(val))

        for i in range(len(val)-1, -1, -1): 
            if i == len(val) - 1: 
                total += val[i]
            elif val[i] < val[i+1]:  
                total -= val[i]
            else:  
                total += val[i] 
                
        return total
       

