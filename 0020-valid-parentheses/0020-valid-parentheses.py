class Solution:
    def isValid(self, s: str) -> bool:
        type1 = ['(', '{', '[']
        type2 = [')', '}', ']']
        stack = []
        
        for val in s:
            if val in type1:  
                stack.append(val)
            else:  
                if not stack:  
                    return False
                last = stack[-1]
                
                if type1.index(last) == type2.index(val):
                    stack.pop()
                else:
                    return False
                    
        return not stack
