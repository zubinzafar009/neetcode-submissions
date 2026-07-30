class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        anagram_list = []
        for word in strs:
            key = ''.join(sorted(word))
            if key not in anagram_dict:
                anagram_dict[key] = [word]
            else:
                anagram_dict[key].append(word)

        for value in anagram_dict.values():
            anagram_list.append(value)

        return anagram_list

        


        

        

            