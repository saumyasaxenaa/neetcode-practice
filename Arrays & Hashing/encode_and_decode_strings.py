class Solution:
    def encode(self, strs):
        result = ''
        for s in strs:
            result += str(len(s)) + '#' + s
        return result

    def decode(self, s):
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            result.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return result

obj = Solution()
print(obj.decode(obj.encode(['Hello, World'])))