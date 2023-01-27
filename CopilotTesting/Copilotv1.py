# Program to estimate pi via Monte Carlo simulation

import random
import math
import time

def estimate_pi(n):
    """Estimate pi by simulating n random points in the unit square."""
    inside = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x*x + y*y < 1:
            inside += 1
    return 4 * inside / n

def main():
    n = 1000000
    t0 = time.time()
    pi = estimate_pi(n)
    t1 = time.time()
    print("Estimated pi =", pi)
    print("Error =", abs(pi - math.pi))
    print("Time =", t1 - t0)

if __name__ == "__main__":
    main()

# Path: CopilotTesting\Copilotv1.py