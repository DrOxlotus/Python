def CalculatePrimeSum(a, b):
    primeSum = 0
    primes = []

    for i in range(2, b + 1):
        guard = 0 # Prevents the wrong values from augmenting the sum total
        for j in range(2, i // 2 + 1): # Using floor division to round to the smallest whole number
            if i % j == 0:
                guard = guard + 1
        if guard <= 0:
            primes.append(i)
            primeSum = primeSum + i
    return primeSum, primes

print(CalculatePrimeSum(2, 30))
