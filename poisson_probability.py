import math

def poisson_pmf(k, lambda_):
    return (lambda_**k / math.factorial(k)) * math.exp(-lambda_)

# Parameters for the Poisson distribution
lambda_ = 5  # The mean or average rate of the Poisson distribution

# (a) Calculate P(Y ≤ 4)
probability_less_than_4 = sum(poisson_pmf(k, lambda_) for k in range(5))
print(f"P(Y ≤ 4) = {probability_less_than_4}")

# (b) Calculate P(Y > 4) using the fact that P(Y > 4) = 1 - P(Y ≤ 4)
probability_greater_than_4 = 1 - probability_less_than_4
print(f"P(Y > 4) = {probability_greater_than_4}")

