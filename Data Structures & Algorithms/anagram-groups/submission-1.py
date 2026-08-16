from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        result = []

        for i in strs:
            sorted_i = tuple(sorted(i))
            map[sorted_i].append(i)

        for val in map.values():
            result.append(val)
        return result