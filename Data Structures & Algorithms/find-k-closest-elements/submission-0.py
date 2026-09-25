class Solution:

  def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    left = 0
    right = len(arr) - 1

    # Shrink the window until its size is k
    while right - left >= k:
      # Compare the distance of the left and right elements from x
      if abs(arr[left] - x) > abs(arr[right] - x):
        left += 1  # Left element is further, move left up
      else:
        right -= 1  # Right element is further (or equal, handle tie-breaker), move right down

    # Return the remaining window of size k
    return arr[left : right + 1]