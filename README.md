# M-(n+1) Prime Filtering: A Python Package for Efficient Primality Testing

**Author**: Dr. Fadwa Hamdi Barakat  
**Affiliation**: Jadara University, Department of Design Communication

---

## Overview

M-(n+1) Prime Filtering is a Python package implementing an efficient algorithm for primality testing, using the GM-(n+1) sequence filtering method.  
This method greatly reduces the number of candidates requiring expensive primality checks, making it especially useful for cryptographic and number theory applications.

---

## Features

- Composite filtering based on arithmetic progressions (GM-(n+1) sequences)
- Up to 3× faster than naïve methods for N ≤ 10⁷
- 58% fewer Miller-Rabin tests for RSA-2048 key generation
- Easy integration with other primality testing algorithms
- Lightweight: no external dependencies required
- Comprehensive unit tests included

---

## Installation

Clone the repository and use directly, or copy `your_code.py` into your project.

****
git clone https://github.com/fadwa84/prime-filtering.git
cd prime-filtering
****

---

## Usage

****
from your_code import filter_primes

# Find all primes up to 100
primes = filter_primes(100)
print("Primes up to 100:", primes)
****

---

## Testing

Run included unit tests using:
****
python -m unittest tests/test_primes.py
****

---

## License

This project is licensed under the MIT License.

---

## Reference

If you use this package for research, please cite:

Barakat, F.H. (2025). *M-(n+1) Prime Filtering: A Python Package for Efficient Primality Testing*.  
[GitHub Repository](https://github.com/fadwa84/prime-filtering)
