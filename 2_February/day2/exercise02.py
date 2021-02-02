from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]


a = Solution()
s1 = ["h", "e", "l", "l", "o"]
print(a.reverseString(s1))
