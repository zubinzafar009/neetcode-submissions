class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        flowers = [0] + flowerbed + [0]

        for i in range(1, len(flowers) - 1):
            if flowers[i - 1] == 0 and flowers[i] == 0 and flowers[i + 1] == 0 :
                flowers[i] = 1
                n -= 1

                if n == 0:
                    break
        
        return n == 0
        