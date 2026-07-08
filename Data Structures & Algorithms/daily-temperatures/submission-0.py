class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]*n
        stack = []
        for current_day in range(n):
            current_temp = temperatures[current_day]
            while stack and current_temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                result[prev_day] = current_day - prev_day
            stack.append(current_day)
        return result