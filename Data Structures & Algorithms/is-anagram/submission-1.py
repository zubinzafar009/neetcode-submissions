class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lookup = {}
        lookup_2 = {}

        for char in s:
            if char not in lookup:
                lookup[char] = 1
            else:
                lookup[char] += 1

        for char in t:
            if char not in lookup:
                return False
            else:
                if char not in lookup_2:
                    lookup_2[char] = 1
                else:
                    lookup_2[char] += 1
        
        for key in lookup:
            if key not in lookup_2 or lookup[key] != lookup_2[key]:
                return False

        return True

        