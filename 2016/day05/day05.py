import hashlib

INPUT = "abbhdwsy"
EX_INPUT = "abc"


def day04(inp):
    idx = 0
    p1_pass = ""
    p2_pass = [""] * 8
    avail = [x for x in '01234567']

    while avail:
        byte_inp = (inp + str(idx)).encode()
        hash = hashlib.md5(byte_inp).hexdigest()

        if hash.startswith("0" * 5):
            pos = hash[5]
            char = hash[6]
            if len(p1_pass) < 8:
                p1_pass += hash[5]
            if pos in avail and not p2_pass[int(pos)]:
                p2_pass[int(pos)] = char
                avail.remove(pos)

        idx += 1

    return (p1_pass, ''.join(p2_pass))


if __name__ == "__main__":
    p1, p2 = day04(INPUT)
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")
