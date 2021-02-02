# leetcode 09 回文数
from typing import List


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


a = Solution()
print(a.isPalindrome(-121))
