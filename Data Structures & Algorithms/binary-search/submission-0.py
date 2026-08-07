class Solution:
    def search(self, nums: List[int], target: int) -> int:
        beg = 0
        end = len(nums) - 1

        while (beg <= end):
            mid = int((beg + end)/2)
            elem = nums[mid]

            if target > elem:
                beg = mid + 1
            elif target < elem:
                end = mid - 1
            else:
                return mid
        return -1
        