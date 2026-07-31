class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_arr = []
        for i in range(0, len(nums)):
            remaining_nums = nums.copy()
            remaining_nums.pop(i)
            prod_arr.append(self.compute_prod(remaining_nums))
        return prod_arr

    def compute_prod(self, prod_arr):
        prod = 1
        for i in range(0, len(prod_arr)):
            prod = prod * prod_arr[i]
        return prod