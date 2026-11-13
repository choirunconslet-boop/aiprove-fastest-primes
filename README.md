# fastest-primes

Count primes <= N (1 <= N <= 5,000,000), read from stdin, print the count.

Run: `python3 main.py`

Approach: Sieve of Eratosthenes over a `bytearray`, with the inner
marking done by C-speed slice assignment (`s[i*i:n+1:i] = b'\x00' * k`).
Python startup is low (~25 ms) and the sieve itself is C-speed, which
beats a Node implementation on the same machine (Node startup alone is
~80 ms). Verified: N=5,000,000 -> 348513 in ~75 ms wall-clock locally.
