class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for word in strs:
            parts.append(str(len(word)) + '#' + word)
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            l = int(s[i:j])
            result.append(s[j+1:j+1+l])
            i = j + 1 + l
        return result