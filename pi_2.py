# Based on https://gist.github.com/amitsaha/2036026

import random
import multiprocessing
from multiprocessing import Pool


# Calculate the number of points in the unit circle
def monte_carlo_pi_part(n):
    count = 0
    for i in range(n):
        x = random.random()
        y = random.random()

        # if it is within the unit circle
        if x * x + y * y <= 1:
            count += 1

    return count


if __name__ == '__main__':
    print 'Run across 4 CPUs'
    np = 4

    # Number of points to simulate (50 million)
    n = 50000000

    # Split up across CPUs
    part_count = [n / np for i in range(np)]

    # Run simulation in parallel
    pool = Pool(processes=np)
    count = pool.map(monte_carlo_pi_part, part_count)

    print 'Estimated value of Pi:: ', sum(count) / (n * 1.0) * 4

