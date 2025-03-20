'''
My Initial solution consists of looking up in hash_map.values().Since it add's additional complexity when the hash_map keys are not constant, changed the approach to use hash_set.

TC : O(n)
SC : O(1) --> As Hash_map keys are constant
'''



# Solution --> Most optimal
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split(" ") # To split the words

        if(len(pattern)!=len(words)):
            return False

        words_set = set(words)

        pattern_set = set(pattern)

        if len(words_set)!=len(pattern_set):
            return False

        hash_map = defaultdict(str)
        hash_set = set()

        for i in range(len(pattern)):
            if pattern[i] in hash_map: # if the word exist in hash_map, if the match doesn't happen, straight way return False
                if (hash_map[pattern[i]]!=words[i]):
                    return False
            else:
                if words[i] in hash_set:# Initially I was using hash_map.values(). Although it works for this problem as hash_map is constant only 26 values.
                    return False
                hash_map[pattern[i]] = words[i]
                hash_set.add(words[i])


        return True


## Solution 2 --> Optimal
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split(" ")

        if(len(pattern)!=len(words)):
            return False

        words_set = set(words)

        pattern_set = set(pattern)

        if len(words_set)!=len(pattern_set):
            return False
        hash_map = defaultdict(str)
        hash_map2 = defaultdict(str)

        for i in range(len(pattern)):
            if pattern[i] in hash_map:
                if (hash_map[pattern[i]]!=words[i]):
                    return False
            else:
                hash_map[pattern[i]] = words[i]
            if words[i] in hash_map2:
                  if (hash_map2[words[i]]!=pattern[i]):
                    return False
            else:
                hash_map2[words[i]] = pattern[i]

        return True
