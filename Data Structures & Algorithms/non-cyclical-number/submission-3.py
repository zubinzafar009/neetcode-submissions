class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        sum = 0
        while True:
            sum = self.getSumSquare(n)
            if sum not in seen:
                seen.append(sum)
            else:
                return False
            print (seen)
            if sum == 1:
                return True
            n = sum
        return False

    def getSumSquare(self, n):
        sumSquare = 0
        while (n > 0):
            digit = n%10
            sumSquare = sumSquare + (digit * digit)
            n = int(n/10)
        print(sumSquare)
        return sumSquare
        