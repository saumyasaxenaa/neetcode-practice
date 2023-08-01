class Solution:
    def twoSum(self, nums, target):
        dic = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dic:
                return [dic[diff], i]
            dic[nums[i]] = i

obj = Solution()
print(obj.twoSum([3,2,4], 6))