def count_multiples(numbers):
    divisors = [1,2,3,4,5,6,7,8,9]
    result = {}
    
    for d in divisors:
        count = 0
        for n in numbers:
            if n % d == 0:
                count += 1
        result[d] = count

    return result

# Test
numbers = [1,2,8,9,12,46,76,82,15,20,30]
print(count_multiples(numbers))  # {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}
