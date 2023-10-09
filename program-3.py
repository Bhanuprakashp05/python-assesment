def generate_series_3(a):
    if a % 2 == 0:
        a -= 1
    return [i for i in range(1, 2*a, 2)]

# Example
print(generate_series_3(4))  # Expected output: [1, 3, 5]
