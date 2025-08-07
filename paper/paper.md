---
title: 'M-(n+1) Prime Filtering: A Python Package for Efficient Primality Testing'
tags:
  - python
  - number theory
  - primality testing
  - mathematics
  - cryptography
authors:
  - name: Fadwa Hamdi Barakat
    orcid: 0000-0000-XXXX-XXXX
    affiliation: "Jadara University, Department of Design Communication, Irbid, Jordan"
    email: myjoran00@gmail.com
---

# Summary

M-(n+1) Prime Filtering is a Python package implementing a novel composite-filtering method based on GM-(n+1) sequences. This algorithm significantly reduces the candidate set for primality testing by identifying and excluding composites generated through arithmetic sequences. The tool improves computational efficiency by up to 3× over naive approaches, reducing the need for probabilistic or deterministic testing. Benchmarks confirm 58% fewer Miller-Rabin iterations for RSA-2048 key generation and up to 89% search space reduction. The package is fully self-contained, requires no external dependencies, and is equipped with documentation and unit tests.

# Statement of Need

Efficient prime detection is critical in number theory and cryptography. Existing solutions such as the Sieve of Eratosthenes or probabilistic methods (e.g., Miller-Rabin) are fast but can still be improved, especially when integrated into cryptographic key generation workflows. This package offers a new sequence-based filtering strategy, providing a ready-to-use implementation for both education and research.

# References

- Agrawal, M., Kayal, N. & Saxena, N. (2004). PRIMES is in P. Annals of Mathematics, 160, 781–793. https://doi.org/10.4007/annals.2004.160.781
- Crandall, R. & Pomerance, C. (2005). Prime Numbers: A Computational Perspective, 2nd edn. Springer. https://doi.org/10.1007/0-387-28979-8
- Bach, E. & Shallit, J. (1996). Algorithmic Number Theory, Volume 1: Efficient Algorithms. MIT Press.
- Rabin, M. O. (1980). Probabilistic algorithm for testing primality. Journal of Number Theory, 12, 128–138. https://doi.org/10.1016/0022-314X(80
