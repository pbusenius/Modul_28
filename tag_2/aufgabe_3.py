from typing import Tuple


g = 2
p = 10729219
pk = 1130615
c = [9762726, 6202393]


def find_sk(p: int, g: int, pk) -> int:
    sk = None
    res = 1
    for i in range(1, p):
        res = res * g % p
        if res == pk:
            sk = i
            break

    return sk


def dec(sk: int, c: Tuple[int, int]) -> int:
    k = pow(c[0], sk, p)
    k_mod_inv = pow(k, -1, p)

    return c[1] * k_mod_inv % p



if __name__ == "__main__":
    sk = find_sk(p, g, pk)
    print(f"sk found by Eve: {sk}")

    m = dec(sk, c)
    print(f"Decrypted message by Eve: {m}")
    