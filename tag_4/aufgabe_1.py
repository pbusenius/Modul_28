import hashlib


INPUT_PATH = "bestellbestätigung.txt"
OUTPUT_PATH= "bestellbestätigung_evil.txt"


def compute_hash(x: str) -> str:
    return hashlib.sha256(x.encode()).hexdigest()[:6]


def modify_auftragsnummer(data: str) -> str:
    auftragsnummer_line = data.split("\n")[0]
    auftragsnumer = int(auftragsnummer_line.split("Betreff: Bestellbestätigung - Auftragsnummer #2023-")[1])
    new_auftragsnummer_line = f"Betreff: Bestellbestätigung - Auftragsnummer #2023-{auftragsnumer + 1}"
    return data.replace(auftragsnummer_line, new_auftragsnummer_line)


def modify_bank_information(data: str) -> str:
    data = data.replace("Alice Hausbank", "Evil Corp. Headquarters Financial Services")
    data = data.replace("Alice Evasdottir", "Evil Eve")
    data = data.replace("DE12345678901234567890", "DE11111111111111111111")
    
    return data

def main():
    with open(INPUT_PATH, "r") as file:
        data = file.read()

    old_hash_value = compute_hash(data)

    data = modify_bank_information(data)

    for i in range(2**32):
        data = modify_auftragsnummer(data)
        if old_hash_value == compute_hash(data):
            with open(OUTPUT_PATH, "w") as file:
                file.write(data)

            print(f"collision found after {i} runs")
            break


if __name__ == "__main__":
    main()