import tqdm
import time
import random
from math import sqrt
from secrets import randbelow


TIME_THRESHOLD = 5
OUTPUT_FILE = "aufgabe_1.txt"


def probedivision(n: int) -> bool:
    wurzel = int(sqrt(n))

    for i in range(2, wurzel + 1):
        if n % i == 0:
            return False
        
    return True



def miller_rabin(n: int, rounds:int=60) -> bool:
    is_prime_results = []

    if n == 2:
        return True
    elif n % 2 == 0:
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


def perform_probedivision(n):
    start_time = time.time()
    probedivision(n)
    end_time = time.time()

    return end_time - start_time


def perform_miller_rabin(n):
    start_time = time.time()
    miller_rabin(n)
    end_time = time.time()

    return end_time - start_time


if __name__ == "__main__":
    perform_probedivision(46478236839118759)
    """
    d = 5
    try_probedivison = True
    try_miller_rabin = True

    with open(OUTPUT_FILE, "w") as file:
        for _ in tqdm.tqdm(range(1000)):
            counter = 1
            while counter <= 100:
                n = int(''.join(["{}".format(random.randint(1, 9)) for num in range(3, d)]))

                if try_probedivison:
                    elapsed_time = perform_probedivision(n)
                    if elapsed_time >= TIME_THRESHOLD:
                        file.write(f"Probedivision: {d}, {n}Z\n")
                        try_probedivison = False
                    
                if try_miller_rabin:
                    elapsed_time = perform_miller_rabin(n)
                    if elapsed_time >= TIME_THRESHOLD:
                        file.write(f"Miller-Rabin: {d}, {n}\n")
                        try_miller_rabin = False
                        break
                    
                counter += 1

            d += 1
    """
