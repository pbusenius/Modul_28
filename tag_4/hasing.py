import hashlib


def main(x: str):
    y = hashlib.sha256(x.encode()).hexdigest()
    print(y)


if __name__ == "__main__":
    x = "Hello World!"
    main(x)

    x = "Hello Wolrd!!"
    main(x)
    