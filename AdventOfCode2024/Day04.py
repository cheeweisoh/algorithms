import sys


def part_one(s: dict[complex, str]) -> int:
    res = 0

    for c in coords:
        for d in [1, 1j, 1 + 1j, 1 - 1j, -1, -1j, -1 + 1j, -1 - 1j]:
            if (
                coords.get(c, "")
                + coords.get(c + d, "")
                + coords.get(c + d * 2, "")
                + coords.get(c + d * 3, "")
                == "XMAS"
            ):
                res += 1

    return res


def part_two(s: dict[complex, str]) -> int:
    res = 0

    for c in coords:
        for d in [1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j]:
            if (
                coords.get(c - d, "") + coords.get(c, "") + coords.get(c + d, "")
                == "MAS"
                and coords.get(c - d * 1j, "")
                + coords.get(c, "")
                + coords.get(c + d * 1j, "")
                == "MAS"
            ):
                res += 1

    return res


input = sys.stdin.read().split(sep="\n")[:-1]
coords = {x + 1j * y: c for y, r in enumerate(input) for x, c in enumerate(r)}
print(part_one(coords))
print(part_two(coords))
