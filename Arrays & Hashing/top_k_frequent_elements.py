class Solution:
    def topKFrequentElements(self, nums, k):
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        result = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        print(count)
        for num, count in count.items():
            freq[count].append(num)
        print(freq)

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result


obj = Solution()
print(obj.topKFrequentElements([1,1,1,2,2,3], 2))