class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lookup = {}

        for num in nums:
            if num not in lookup:
                lookup[num] = True
                continue
            else:
                return True
        return False
            
                



        