from collections import Counter

class Solution:
    def validAnagram(self, str1, str2):
        if len(str1) != len(str2):
            return False
        dic1 = Counter(str1)
        dic2 = Counter(str2)

        if dic1 == dic2:
            return True
        return False

obj = Solution()
print(obj.validAnagram('rat', 'car'))