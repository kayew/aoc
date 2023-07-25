import hashlib

INPUT = "yzbqklnj"


def day04(inp):
    idx = 0
    p1_idx = 0
    p2_idx = 0

    while p2_idx == 0:
        byte_inp = (inp + str(idx)).encode()
        hash = hashlib.md5(byte_inp).hexdigest()

        if hash.startswith("0" * 5) and p1_idx == 0:
            p1_idx = idx
        if hash.startswith("0" * 6) and p2_idx == 0:
            p2_idx = idx

        idx += 1

    return (p1_idx, p2_idx)


if __name__ == "__main__":
    p1, p2 = day04(INPUT)
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")
