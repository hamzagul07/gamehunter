# Sprague-Grundy values of the Foursquare subtraction game (normal play).
# From a heap of n: if n mod 4 == 1, subtract any positive square <= n;
# otherwise subtract 3, 8 or 9. a(n) = 0 exactly at the P-positions.
from math import isqrt

def foursquare(nmax):
    a = [0] * (nmax + 1)
    for n in range(1, nmax + 1):
        if n % 4 == 1:
            moves = [k * k for k in range(1, isqrt(n) + 1)]
        else:
            moves = [s for s in (3, 8, 9) if s <= n]
        reach = {a[n - s] for s in moves}
        g = 0
        while g in reach:
            g += 1
        a[n] = g
    return a

print(foursquare(59))
