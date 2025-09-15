class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1 :
            return True
        new_s = ''
        s = s.replace(" ", "")
        for char in s :
            if char.isalpha() or char.isdigit():
                new_s += char
        new_s = list(new_s.lower())
        print(new_s)
        s_len = int(len(new_s))
        print(s_len)
        new_rev = list(new_s[::-1])
        print(new_rev)
        for i in range(0,s_len):
            if new_s[i] == new_rev[i]:
                output = True
            else :
                return False
        return True
        