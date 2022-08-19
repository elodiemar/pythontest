import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
numbers = input().split()

def closest_to_zero(numbers):
    closest = 5526
    if numbers:
        for num in numbers:
            if abs(int(num))== abs(closest):
                closest = abs(int(num))
            elif abs(int(num)) <= abs(closest):
                closest =int(num)
        return closest
    else:
        return 0

print(closest_to_zero(numbers))

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
