class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        need = Counter(t)
        required = len(need)


        left = 0
        right = 0
        formed = 0  
        window_counts = defaultdict(int)


        ans = (float('inf'), None, None)

        while right < len(s):
            char = s[right]
            window_counts[char] += 1

            if char in need and window_counts[char] == need[char]:
                formed += 1

            while left <= right and formed == required:
                char = s[left]

                if (right - left + 1) < ans[0]:
                    ans = (right - left + 1, left, right)

                window_counts[char] -= 1
                if char in need and window_counts[char] < need[char]:
                    formed -= 1

                left += 1

            right += 1

        return "" if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]
