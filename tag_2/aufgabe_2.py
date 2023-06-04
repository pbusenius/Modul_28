from typing import Tuple
from secrets import randbelow


g = 2
p = 10729219


def Gen() -> Tuple[int, int]:
    sk = randbelow(p-1)
    pk = pow(g, sk, p)

    return pk, sk


def Enc(pk: int, m: int) -> Tuple[int, int]:
    y = randbelow(p-1)
    k = pow(pk, y, p)

    c1 = pow(g, y, p)
    c2 = m * k % p

    return c1, c2


def Dec(sk: int, c: Tuple[int, int]) -> int:
    k = pow(c[0], sk, p)
    k_mod_inv = pow(k, -1, p)

    return c[1] * k_mod_inv % p


if __name__ == "__main__":
    m = 12345
    print(f"Plain message: {m}")

    # Alice pk and sk
    pk_a, sk_a = Gen()

    # encrypted message form Bob
    c = Enc(pk_a, m)
    print(f"Encrypted message: {c}")

    # decrypted message by Alice
    m_out = Dec(sk_a, c)

    print(f"Decrypted message: {m_out}")
    print(f"Message successfully decrypted: {m==m_out}")