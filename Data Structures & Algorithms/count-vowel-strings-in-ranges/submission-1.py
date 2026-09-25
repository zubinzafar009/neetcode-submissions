class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowelWords = []
        for word in words:
            if word[0] in vowels and word[len(word) - 1] in vowels:
                vowelWords.append(1)
            else:
                vowelWords.append(0)
        
        final = []

        for query in queries:
            count = 0
            start = query[0]
            end = query[1]
            count += sum(vowelWords[start: end + 1])
            final.append(count)

        return final

        