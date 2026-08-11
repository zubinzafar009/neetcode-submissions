class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        maxPower = len(digits) - 1
        for i in range(len(digits)):
            number = number + digits[i] * pow(10, maxPower - i)
        number = number + 1

        return [int(x) for x in str(number)]
        