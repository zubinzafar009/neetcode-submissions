class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.bs(nums, target, True)
        right = self.bs(nums, target, False)
        return [left, right]

    def bs(self, nums, target, leftBias):
        beg = 0 
        end = len(nums) - 1
        index = -1

        while beg <= end:
            mid = (beg + end) // 2
            if target > nums[mid]:
                beg = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                index = mid
                if leftBias:
                    end = mid - 1
                else:
                    beg = mid + 1
        return index
        
