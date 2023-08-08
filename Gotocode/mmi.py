def extended_euclidean_algorithm(b,m):
    if b == 0:
        return (m, 0, 1)
    else:
        GCD, x1, y1 = extended_euclidean_algorithm(m % b, b)
        x = y1 - (m // b) * x1
        y = x1
        return (GCD, x, y)
def modular_multiplicative_inverse(b, m):
    GCD, x, y = extended_euclidean_algorithm(b, m)
    if GCD == 1:
        return x % m
    else:
        return None

a = 7
b = 3
m = 11
b_inverse = modular_multiplicative_inverse(b, m)

if b_inverse is not None:
    result = ((a % (m*b)) * (b_inverse % m)) % m
    print("The modulo of %d/%d by %d is %d." % (a, b, m, result))
else:
    print("The modular inverse of %d modulo %d does not exist." % (b, m))
