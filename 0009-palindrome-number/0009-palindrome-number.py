class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers cannot be palindromes
        if x < 0:
            return False
        s = str(x)
        if len(s) < 2:
            return True
        else:
            return s == s[::-1]
           