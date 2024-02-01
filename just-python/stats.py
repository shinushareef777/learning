import math


def variance(arr: list) -> float:
	mean = round(sum(arr) / len(arr), 3)
	var = 0
	for i in arr:
		var += (i - mean)**2
	return round(var / (len(arr) - 1), 3)

def std(arr: list) -> float:
	return round(math.sqrt(variance(arr)), 3)

def calculate_sample_covariance(x, y):
    n = len(x)
    if n != len(y):
        raise ValueError("Number of data points for x and y must be equal.")
    
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    
    covariance = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y)) / (n - 1)
    return covariance

def calculate_correlation_coefficient(x, y):
    n = len(x)
    if n != len(y):
        raise ValueError("Number of data points for x and y must be equal.")
    
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    
    numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    denominator_x = math.sqrt(sum((xi - mean_x)**2 for xi in x))
    denominator_y = math.sqrt(sum((yi - mean_y)**2 for yi in y))
    
    correlation_coefficient = numerator / (denominator_x * denominator_y)
    
    return correlation_coefficient


data = [1, 5, 6, 4, 3, 4, 3]
bbk = [17, 13, 15, 10, 12, 18, 11]
# print(std(bbk))
# print(calculate_sample_covariance(data, bbk))
print(calculate_correlation_coefficient(data, bbk))
