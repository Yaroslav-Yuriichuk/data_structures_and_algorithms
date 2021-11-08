from functools import lru_cache
import math

def solve(x, n):
    if n == 1:
        return len(x) if x.count('0') == 0 else -1

    powers = set()

    num = 1
    while num < pow(2, len(x)):
        powers.add(bin(num)[2:])
        num *= n

    @lru_cache(maxsize=None)
    def solve_rec(x):
        if x in powers:
            return 1
        elif x == '0':
            return math.inf    

        result = math.inf
        for i in range(1, len(x)):
            result = min(result, solve_rec(x[:i]) + solve_rec(x[i:]))

        return result

    result = solve_rec(x)
    return -1 if result == math.inf else result


if __name__ == '__main__':
    x = input()
    n = int(input())

    print(solve(x, n))
