class Solution:
    def productsExceptSelf(self, nums):
        result = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            result[i] *= prefix
            prefix *= nums[i]
        prefix = 1
        for i in range(len(nums) - 1, -1 , -1):
            result[i] *= prefix
            prefix *= nums[i]
        return result
    
obj = Solution()
print(obj.productsExceptSelf([1,2,3,4]))