class Solution:
    def reverse(self, x: int) -> int:
        tmp = int((str(x) if x > 0 else str(-x) + "-")[::-1])
        return tmp if -2 ** 31 < tmp < 2 ** 31 - 1 else 0


a = Solution()
print(a.reverse(170))
