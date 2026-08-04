class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = []
        for i in range(len(temperatures)):
            count = 1
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    days.append(count)
                    break
                else:
                    count += 1
                if j == len(temperatures) - 1:
                    days.append(0)

        diff = len(temperatures) - len(days)
        for i in range(0, diff):
            days.append(0)
        return days

        