import sys


def part_one(mapp: dict[complex, str]) -> int:
    curr_pos = min(p for p in mapp if mapp[p] == "^")
    curr_dir = -1
    visited = set()

    while curr_pos in mapp and (curr_pos, curr_dir) not in visited:
        visited.add((curr_pos, curr_dir))

        new_pos = curr_pos + curr_dir

        if mapp.get(new_pos) == "#":
            curr_dir *= -1j
        else:
            curr_pos = new_pos

    uniq_nodes = {pos for pos, _ in visited}
    return uniq_nodes, curr_pos in uniq_nodes


def part_two(mapp: dict[complex, str]):
    start_pos = min(p for p in mapp if mapp[p] == "^")
    uniq_nodes = part_one(mapp)[0]
    res = 0

    for pos in uniq_nodes:
        temp_mapp = mapp.copy()
        if pos != start_pos:
            temp_mapp[pos] = "#"
        res += part_one(temp_mapp)[1]

    return res


input = sys.stdin.read().split(sep="\n")
mapp = {x + y * 1j: c for x, line in enumerate(input) for y, c in enumerate(list(line))}
print(len(part_one(mapp)[0]))
print(part_two(mapp))
