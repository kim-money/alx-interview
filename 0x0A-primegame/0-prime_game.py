#!/usr/bin/python3
"""Eratosthenes algorithm for game winner determination"""


def isWinner(x, nums):
    """Determine the winner using the Eratosthenes prime sieving algorithm"""
    Ben, Maria = 0, 0
    n = max(nums)

    if x < 1 or not nums:
        return None

    isPrime = [True for _ in range(1, n + 1, 1)]
    isPrime[0] = False
    for i, is_prime in enumerate(isPrime, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            isPrime[j - 1] = False

    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, isPrime[0:n])))
        Ben += primes_count % 2 == 0
        Maria += primes_count % 2 == 1
    if Maria == Ben:
        return None
    return "Maria" if Maria > Ben else "Ben"
