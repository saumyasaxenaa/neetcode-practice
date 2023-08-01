from collections import defaultdict

class Solution:
    def groupAnagrams(self, words):
        res = defaultdict(list)

        for word in words:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(word)
        return res.values()

obj = Solution()
print(obj.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))