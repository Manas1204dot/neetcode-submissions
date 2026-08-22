class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        freq = [[] for i in range(len(nums)+ 1)]

        for n in nums:
            result[n] = 1 + result.get(n,0)
        for n , c in result.items():
            freq[c].append(n)
        final = [] 
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                final.append(n)
                if len(final) == k:
                    return final 