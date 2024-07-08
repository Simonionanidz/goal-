def series_sum(n):
    sum = 0.0
    denominator = 1.0
    
    for i in range(n):
        sum += 1 / denominator
        denominator += 3
    
    return f"{sum:.2f}"

print(series_sum(5))  # Output: "1.57"
print(series_sum(0))  # Output: "0.00"
print(series_sum(1))  # Output: "1.00"
print(series_sum(3))  # Output: "1.39"
