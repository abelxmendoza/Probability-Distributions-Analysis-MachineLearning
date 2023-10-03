def mle_bernoulli_parameter(data):
    n = len(data)
    sum_xi = sum(data)
    
    if n == 0:
        return None  # Handle the case where the dataset is empty
    
    mle_p = (n - sum_xi) / n
    return mle_p

# Example usage:
data = [1, 0, 1, 1, 0, 1, 0, 0, 1]  # Replace with your dataset
mle_estimate = mle_bernoulli_parameter(data)
print(f"Maximum Likelihood Estimate (MLE) for p: {mle_estimate}")

