class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        final_list = []
        for i in range(0, len(nums)):
            complement = 0 - nums[i]
            j = i + 1
            k = len(nums) - 1
            while (j < k):
                if nums[j] + nums[k] > complement:
                    k -= 1
                elif nums[j] + nums[k] < complement:
                    j += 1
                else:
                    if([nums[i], nums[j], nums[k]]) not in final_list:
                        final_list.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
        return final_list
        