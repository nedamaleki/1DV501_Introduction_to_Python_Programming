def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True

def next_prime(n):
    candidate = n + 1
    # Loop until we find a prime number
    while not is_prime(candidate):
        candidate += 1
    return candidate
