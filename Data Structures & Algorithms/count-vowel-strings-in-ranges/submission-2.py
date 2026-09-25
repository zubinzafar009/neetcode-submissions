class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a', 'e', 'i', 'o', 'u']
        current_cnt = 0
        prefix_cnt = [0] * (len(words) + 1)

        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                current_cnt += 1
            prefix_cnt[i + 1] = current_cnt

        ans = []
        for l, r in queries:
            ans.append(prefix_cnt[r + 1] - prefix_cnt[l])

        return ans