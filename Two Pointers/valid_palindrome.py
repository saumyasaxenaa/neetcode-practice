class Solution:
    def isPalindrome(self, s):
        if len(s) == 0:
            return True
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

obj = Solution()
print(obj.isPalindrome('race a car'))