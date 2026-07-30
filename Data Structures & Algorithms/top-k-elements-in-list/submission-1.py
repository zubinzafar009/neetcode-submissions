class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}

        for i in range(0, len(nums)):
            if nums[i] not in freq_dict:
                freq_dict[nums[i]] = 1
            else: 
                freq_dict[nums[i]] += 1

        sorted_freq_dict = dict(sorted(freq_dict.items(), key=lambda item: item[1]))
        return list(sorted_freq_dict)[-k:]
        