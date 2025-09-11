class Solution:
    def decodeString(self, s: str) -> str:
        is_in = True
        i = 0
        while is_in:
            if "[" not in s and "]" not in s:
                is_in = False

            if s[i] == "]":
                temp = ""
                new_word = ""
                rep = ""

                for j in range(i - 1, -1, -1):
                    if s[j] == "[":
                        k = j - 1
                        while k >= 0 and s[k].isdigit():
                            rep = s[k] + rep   
                            k -= 1
                        repeat_count = int(rep)
                        for _ in range(repeat_count):
                            new_word += temp[::-1]
                        s = s[:k + 1] + new_word + s[i + 1:]
                        i = -1   
                        break
                    else:
                        temp += s[j]
            i += 1
        return s



        
            
        