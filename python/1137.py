class Solution:
    def tribonacci(self, n: int) -> int:
        sum_dict = {}
        sum_dict[0] = 0
        sum_dict[1] = 1
        sum_dict[2] = 1
        if n in sum_dict:
            return sum_dict[n]
        for i in range(3, n + 1):
            sum_dict[i] = sum_dict[i - 3] + sum_dict[i - 2] + sum_dict[i - 1]
        return sum_dict[n]


print(Solution.tribonacci(None, 25))
print(Solution.tribonacci(None, 4))
