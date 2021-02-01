class Solution:
    def isValid(self, s):
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''

    def isTrue(self, x):
        while x:
            print('n')


a = Solution()

s1 = "()"
s2 = "()[]{}"
s3 = "(]"
s4 = "([)]"
s5 = "{[]}"

# print(a.isValid(s2))


print(a.isTrue(0))
