def is_prime(num):
    if num <=1:
        return False
    for number in range(2, 100000):
        if num % number == 0 and num != number:
            return False
    return True
