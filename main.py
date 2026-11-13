import sys

n = int(sys.stdin.buffer.read())
if n < 2:
    print(0)
    sys.exit(0)
s = bytearray(b"\x01") * (n + 1)
s[0:2] = b"\x00\x00"
sq = int(n ** 0.5)
for i in range(2, sq + 1):
    if s[i]:
        s[i * i:n + 1:i] = b"\x00" * ((n - i * i) // i + 1)
print(sum(s))
