import sys


def part_one(mapp: dict[complex, str]) -> int:
    node_list = {}
    for pos, val in mapp.items():
        if val != ".":
            if val in node_list:
                node_list[val].append(pos)
            else:
                node_list[val] = [pos]

    antinodes = set()
    for n in node_list:
        ant_list = node_list[n]

        for i in range(len(ant_list)):
            for j in range(i):
                new_pos = [
                    ant_list[i] + (ant_list[i] - ant_list[j]),
                    ant_list[j] + (ant_list[j] - ant_list[i]),
                ]

                for pos in new_pos:
                    if pos in mapp:
                        antinodes.add(pos)

    return len(antinodes)


def part_two(mapp: dict[complex, str]) -> int:
    node_list = {}
    for pos, val in mapp.items():
        if val != ".":
            if val in node_list:
                node_list[val].append(pos)
            else:
                node_list[val] = [pos]

    antinodes = set()
    for n in node_list:
        ant_list = node_list[n]

        for i in range(len(ant_list)):
            for j in range(len(ant_list)):
                if i != j:
                    diff = ant_list[i] - ant_list[j]
                    curr = ant_list[i]

                    while curr in mapp:
                        antinodes.add(curr)
                        curr += diff

    return len(antinodes)


input = sys.stdin.read().split(sep="\n")
mapp = {x + y * 1j: c for x, line in enumerate(input) for y, c in enumerate(list(line))}
print(part_one(mapp))
print(part_two(mapp))
