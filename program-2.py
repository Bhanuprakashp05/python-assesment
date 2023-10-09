def generate_series_2(a):
    result = []
    for i in range(a):
        result.append(2*i + 1)
    return result

# Test
print(generate_series_2(4))  # [1, 3, 5, 7]
