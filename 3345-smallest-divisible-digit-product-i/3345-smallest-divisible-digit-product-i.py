class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for num in range(n, n + 10):
            
            prod = 1
            for digit in str(num):
                prod *= int(digit)
            if prod % t == 0:
                return num