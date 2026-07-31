class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0 
        j = len(heights) - 1
        max_capacity = 0

        while (i < j):
            capacity = min(heights[i], heights[j]) * (j - i)
            max_capacity = max(max_capacity, capacity)

            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
            
        return max_capacity
        