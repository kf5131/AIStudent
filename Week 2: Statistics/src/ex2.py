# Probability Theory and Simulation
#
# Tasks:
# 1.
# Simulate 1000 coin tosses, calculate the probability of getting heads, 
# and compare it with the theoretical probability.
#
# 2.
# Simulate 1000 dice rolls, calculate the probability of getting a prime number, 
# and compare it with the theoretical probability. 
# Calculate the conditional probability of getting a prime number given that the number is odd.
#
# 3.
# Use Monte Carlo Simulation to estimate the value of pi by generating random points
# within a unit square and counting the number of points that fall within a unit circle.

# 1
# /// script
# dependencies = [
#   "numpy==1.26.4",
# ]
# ///

import numpy as np

# Set random seed for reproducibility
#np.random.seed(42)

# Simulate 1000 coin tosses (0 = tails, 1 = heads)
n_tosses = 1000
tosses = np.random.binomial(n=1, p=0.5, size=n_tosses)

# Calculate empirical probability of heads
heads_count = np.sum(tosses)
empirical_prob = heads_count / n_tosses

# Theoretical probability
theoretical_prob = 0.5

print("1. Coin Tosses")
print(f"Number of coin tosses: {n_tosses}")
print(f"Number of heads: {heads_count}")
print(f"Empirical probability of heads: {empirical_prob:.3f}")
print(f"Theoretical probability of heads: {theoretical_prob}")
print(f"Difference: {abs(empirical_prob - theoretical_prob):.3f}")
print("\n")

# 2

# Simulate 1000 dice rolls
n_rolls = 1000
rolls = np.random.randint(1, 7, size=n_rolls)

# Define prime numbers for a six-sided die
primes = {2, 3, 5}

# Calculate counts and probabilities
prime_rolls = np.array([roll in primes for roll in rolls])
odd_rolls = rolls % 2 == 1
prime_and_odd = prime_rolls & odd_rolls

# Calculate empirical probabilities
empirical_prob_prime = np.sum(prime_rolls) / n_rolls
empirical_prob_prime_given_odd = np.sum(prime_and_odd) / np.sum(odd_rolls)

# Calculate theoretical probabilities
theoretical_prob_prime = len(primes) / 6
theoretical_prob_odd = 3 / 6  # {1,3,5}
theoretical_prob_prime_given_odd = 2 / 3  # {3,5} out of {1,3,5}

print("2. Dice Rolls")
print(f"Number of dice rolls: {n_rolls}")
print(f"Number of prime rolls: {np.sum(prime_rolls)}")
print(f"Empirical probability of prime: {empirical_prob_prime:.3f}")
print(f"Theoretical probability of prime: {theoretical_prob_prime:.3f}")
print(f"Difference: {abs(empirical_prob_prime - theoretical_prob_prime):.3f}")
print("\nConditional Probability:")
print(f"P(prime|odd) empirical: {empirical_prob_prime_given_odd:.3f}")
print(f"P(prime|odd) theoretical: {theoretical_prob_prime_given_odd:.3f}")
print(f"Difference: {abs(empirical_prob_prime_given_odd - theoretical_prob_prime_given_odd):.3f}")
print("\n")


# 3

# 3. Monte Carlo simulation to estimate π

# Number of points to generate
n_points = 10000

# Generate random points in unit square
x = np.random.uniform(0, 1, n_points)
y = np.random.uniform(0, 1, n_points)

# Check which points fall inside quarter circle
# A point (x,y) is inside if x^2 + y^2 <= 1
inside_circle = np.sum(x**2 + y**2 <= 1)

# Calculate π estimate
# Area of quarter circle = πr^2/4, where r=1
# Area of unit square = 1
# Ratio = (πr^2/4)/1 = π/4
# Therefore π = 4 * ratio
pi_estimate = 4 * inside_circle / n_points

print("3. Monte Carlo Estimation of π")
print(f"Number of points: {n_points}")
print(f"Points inside quarter circle: {inside_circle}")
print(f"Estimated value of π: {pi_estimate:.6f}")
print(f"Actual value of π: {np.pi:.6f}")
print(f"Absolute error: {abs(pi_estimate - np.pi):.6f}")

