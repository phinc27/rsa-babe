from Crypto.Util.number import bytes_to_long, getPrime
import gmpy2

from secret import flag_1

p = getPrime(24)
q = getPrime(24)

N = p * q
print(N)
# N = 118457404333379
e = 65537
m = bytes_to_long(flag_1)
print(m)
c = pow(m, e, N)
print(c)
# c = 26546747908451
