class Solution:
    def containsDuplicate(self, nums):
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

obj = Solution()
print(obj.containsDuplicate([1,2,3,4]))