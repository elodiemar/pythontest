def high_and_low(numbers):
    numbers = [int(num) for num in numbers.split(" ")]
    print(numbers)
    return f"{max(numbers)} {min(numbers)}"
