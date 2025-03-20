'''
Initially I was using anagrams sorting which results O(n * m logm)

Changing to use charCounter makes
TC: O(n*m)
SC : O(n)

Observations:

1. You can have only Immutables as keys of hash_maps.
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_map = defaultdict(list)

        for word in strs:

            char_counter = [0]*26

            for i in word:
                char_counter[ord(i)-ord('a')]+=1

            hash_map[tuple(char_counter)].append(word)

        return list(hash_map.values()) ## Initi


