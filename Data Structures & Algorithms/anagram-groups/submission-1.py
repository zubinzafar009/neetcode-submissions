class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_list = []
        word_hash = {}
        seen = {}

        for i in range(0, len(strs)):
            j = len(strs) - 1
            if strs[i] in seen:
                continue
            
            seen[strs[i]] = True
            anagram_list = []
            anagram_list.append(strs[i])

            while (j > i):
                if len(strs[j]) == len(strs[i]):
                    is_anagram = self.check_anagram(strs[i], strs[j])
                    if is_anagram:
                        seen[strs[j]] = True
                        anagram_list.append(strs[j])
                        j -= 1
                    else:
                        j -= 1
                else:
                    j -= 1
            
            final_list.append(anagram_list)
        return final_list

    def check_anagram(self, a, b):
        seen = {}

        for i in range(0, len(a)):
            if a[i] not in seen:
                seen[a[i]] = 1
            else:
                seen[a[i]] += 1

        for i in range(0, len(b)):
            if b[i] not in seen:
                return False
            else:
                seen[b[i]] -= 1

        for value in seen.values():
            if value != 0:
                return False

        return True






        

        

            