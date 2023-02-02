import itertools
""" Using itertools as range does not allow for unending increments,
    and itertools is apparently significantly faster (and looks nicer)
    than an infinite loop.                                              """

# Basics of this function borrowed from the Generators video provided:
def get_prime():
    # Handle the first prime
    yield 2
    prime_cache = [2] # Cache of primes

    # Loop over positive, odd integers
    for n in itertools.count(3, 2):
        # Check if n is prime
        for prime in prime_cache:
            if n % prime == 0:
                break
        else:
            # If n is prime, add it to the cache and yield it
            prime_cache.append(n)
            yield n


# Test the function
for prime in get_prime():
    print(prime)
    if prime > 100:
        break
