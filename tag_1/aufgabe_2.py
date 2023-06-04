import math
from secrets import randbelow


INPUT_FILE = "tag_1_rsa_moduli.txt"
OUTPUT_FILE = "tag_1_rsa_moduli_result.txt"

def is_prime(n: int, rounds:int=60) -> bool:
    is_prime_results = []

    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    elif n == 1:
        return False

    for _ in range(rounds):
        a = randbelow(n - 3) + 2
        
        u = n - 1
        j = 0
        while u % 2 == 0:
            j += 1
            u = u // 2

        is_prime = False
        for i in range(1, j+1):
            result = pow(a, (u*2**i), n)
            if result in [-1, 1]:
                is_prime = True
                break
        
        is_prime_results.append(is_prime)
    
    return False not in is_prime_results


def main():
    moduli_list = []
    with open(INPUT_FILE, "r") as file:
        for line in file.readlines():
            moduli_list.append(int(line))


    with open(OUTPUT_FILE, "w") as file:
        for n_one in moduli_list[:-1]:
            for n_two in moduli_list[1:]:
                p = math.gcd(n_one, n_two)
                if is_prime(p):
                    q_one = n_one // p
                    q_two = n_two // p
                    if is_prime(q_one) and is_prime(q_two):
                        file.write(f"{p} * {q_one} = {n_one}\n")
                        file.write(f"{p} * {q_two} = {n_two}\n")
                

if __name__ == "__main__":
    main()