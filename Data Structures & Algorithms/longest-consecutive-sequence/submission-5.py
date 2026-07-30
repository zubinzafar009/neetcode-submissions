class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sorted_nums = sorted(set(nums))
        longest = 1
        sequence = 1

        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] - sorted_nums[i - 1] == 1:
                sequence += 1
            else:
                sequence = 1  # reset unconditionally — fresh run starts at length 1
            longest = max(longest, sequence)  # compare on *every* iteration

        return longest