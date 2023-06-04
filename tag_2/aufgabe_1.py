g = 2
p = 10729219
q = p - 1

X = 9888508
Y = 3930036


def find_exponent(p: int, g: int, pk) -> int:
    sk = None
    res = 1
    for i in range(1, p):
        res = res * g % p
        if res == pk:
            sk = i
            break

    return sk


def compute_key(sk: int, pk: int, p: int) -> int:
    return pow(pk, sk, p)


if __name__ == "__main__":
    x = find_exponent(p, g, X)
    y = find_exponent(p, g, Y)

    print(f"Alice x: {x} X: {X}")
    print(f"Bob   y: {y} Y: {Y}")

    key_a = compute_key(y, X, p)
    key_b = compute_key(x, Y, p)

    print(f"Eve attacked and found the following keys: \n\tEve {key_a}\n\tBob {key_b}")
    print(f"Was the attack successful and both keys are the same? \n\t{key_a == key_b}")
