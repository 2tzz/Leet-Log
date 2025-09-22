class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sr = list(s1)

        for i in range(0,(len(s2)+ 1) - len(s1)) : 
            new_list = []
            j = 0 
            while j < len(s1) :
                new_list.append(s2[i+j])
                j += 1
            if sorted(new_list) == sorted(sr) :
                return True
        return False