# Based on https://gist.github.com/amitsaha/2036026
import random


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
    print 'Run across a single CPU'

    # Number of points to simulate (50 million)
    n = 50000000

    # Run simulation
    count = monte_carlo_pi_part(n)

    print "Estimated value of Pi:: ", count / (n * 1.0) * 4