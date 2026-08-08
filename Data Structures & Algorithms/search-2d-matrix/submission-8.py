class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ourRow = [] 
        l = 0
        r = len(matrix) - 1

        while (l <= r):
            mid = (l + r) // 2
            print(mid)
            if (max(matrix[mid]) >= target and matrix[mid][0] <= target):
                ourRow = matrix[mid]
                break
            elif (target > max(matrix[mid])):
                l = mid + 1
            else:
                r = mid - 1

        print(ourRow)
        if target in ourRow:
            return True
        else:
            return False

        