class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a', 'e', 'i', 'o', 'u']
        count = 0
        final = []

        for query in queries:
            count = 0
            start = query[0]
            end = query[1]

            for i in range(start, end + 1):
                word = words[i]
                if word[0] in vowels and word[len(word) - 1] in vowels:
                    count += 1
            final.append(count)

        return final

        