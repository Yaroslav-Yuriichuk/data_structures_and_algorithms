def solve(piles, h):
    max_pile = max(piles)
    low, high = 1, max_pile
    
    while high >= low:
        k = low + (high - low) // 2
        
        required_h = 0
        for x in piles:
            required_h += (x - 1) // k + 1
            
        if required_h <= h:
            min_speed = k
            high = k - 1
        elif required_h > h:
            low = k + 1
    
    return min_speed


if __name__ == "__main__":
    print(solve([3, 6, 7, 11], 8))
    print(solve([30, 11, 23, 4, 20], 5))
    print(solve([30, 11, 23, 4, 20], 6))
