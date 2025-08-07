import math
from typing import List, Set

def is_prime(num: int) -> bool:
    """Primality test via trial division."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(num)) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True

def generate_gm_sequences(max_num: int) -> Set[int]:
    """Generate all GM-(n+1) composites up to max_num."""
    composites = set()
    for n in range(1, int(math.sqrt(max_num)) + 1):
        composites.update(range(n + 1, max_num + 1, n + 1))
    return composites

def filter_primes(max_num: int) -> List[int]:
    """Return primes ≤ max_num using GM-(n+1) filtering."""
    composites = generate_gm_sequences(max_num)
    return [num for num in range(2, max_num + 1) if num not in composites and is_prime(num)]

# Example usage:
if __name__ == "__main__":
    print("Primes up to 100:", filter_primes(100))
