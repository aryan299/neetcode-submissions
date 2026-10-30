class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for word in strs:
            sorted_word = tuple(sorted(word))
            if sorted_word not in result:
                result[sorted_word] = []
            result[sorted_word].append(word)
        return list(result.values())