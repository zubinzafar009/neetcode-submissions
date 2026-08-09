class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1
        index = 0  # index of the smallest value found so far

        while l <= r:
            if nums[l] < nums[r]:
                if nums[l] < nums[index]:
                    index = l
                break

            mid = (l + r) // 2
            if nums[mid] < nums[index]:
                index = mid

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        left_result = self.bs(nums[0:index], target)
        if left_result != -1:
            return left_result

        right_result = self.bs(nums[index:], target)
        if right_result != -1:
            return right_result + index

        return -1

    def bs(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        return -1