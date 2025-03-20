'''
Very similar to word_pattern.py

The key is identifying to use hash_set in the else condition.

Can also be used with two hash_maps as well

TC: O(n)
SC: O(1) as hash_map contains only ascii characters.

'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        hash_map = defaultdict(str)
        hash_set = set()

        for i in range(len(s)):

            if s[i] in hash_map:
                if (hash_map[s[i]]!=t[i]):
                    return False
            else:
                if t[i] not in hash_set:
                    hash_map[s[i]]=t[i]
                    hash_set.add(t[i])
                else:
                    return False
        return True


