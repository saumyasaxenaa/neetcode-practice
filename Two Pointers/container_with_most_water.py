class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        result = 0

        while left < right:
            area = (right - left) * min(height[left], height[right])
            result = max(result, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return result

obj = Solution()
print(obj.maxArea([1,8,6,2,5,4,8,3,7]))