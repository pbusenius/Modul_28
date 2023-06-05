import time
import hashlib


def main():
    values = {}
    for i in range(2**64):
        x = str(i).encode()
        y = hashlib.sha256(x).hexdigest()
        y_values = y[:8]
        if y_values in values:
            print(f"collision found:\n\t{y}, {i}\n\t{values[y_values][0]}, {values[y_values][1]}")
        else:
            values[y_values] = (y, i)


if __name__ == "__main__":
    main()