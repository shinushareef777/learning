import math


def evaluate_expression(m):
    return math.log10(m + 1) - 0.5 * math.log(m + 1, 0.01)


results = {}

for m in range(1, 366):
    result = evaluate_expression(m)
    results[m] = result

# Calculate the sum of all values
total_sum = sum(results.values())

# Add the total sum to the dictionary
results["total"] = total_sum

print(results)
