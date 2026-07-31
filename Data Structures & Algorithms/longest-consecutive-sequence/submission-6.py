class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = list(sorted(set(nums)))
        print(nums)

        i = 1 
        longest = 0
        sequence = 0

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                sequence += 1
            else:
                sequence = 0
            longest = max(longest, sequence)

        return longest + 1




