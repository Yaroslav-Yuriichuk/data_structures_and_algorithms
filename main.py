from functools import lru_cache
import math


def solve(x, n):
    if n == 1:
        return len(x) if x.count('0') == 0 else -1

    int_x = int(x, 2)
    powers = set()
    length_in_binary = {}

    
    num = 1
    while num < pow(2, len(x)):
        powers.add(num)
        length_in_binary[num] = len(bin(num)) - 2
        num *= n

    @lru_cache(maxsize=None)
    def solve_recursive(number, reverse_start_pos):
        if number == 0:
            return 0

        result = math.inf

        if not x[-(reverse_start_pos+1)] == '0':
            for power in powers:
                if reverse_start_pos + 1 >= length_in_binary[power]:
                    shifted_power = power << (reverse_start_pos - length_in_binary[power] + 1)
                    if shifted_power & number == shifted_power:
                        result = min(result, solve_recursive(number - shifted_power, reverse_start_pos - length_in_binary[power]))

        return result + 1

    result = solve_recursive(int_x, len(x) - 1)
    return -1 if result == math.inf else result


if __name__ == '__main__':
    x = input()
    n = int(input())

    print(solve(x, n))
