#!/usr/bin/env python3

from pathlib import Path


def parseInput(file: list):
    workflows = {}
    parts = []
    split = file.index("")

    for line in file[:split]:
        name, steps = line.split("{")
        steps = [x.split(":") for x in steps.rstrip("}").split(",")]
        workflows[name] = steps

    for line in file[split + 1 :]:
        values = line.strip("{}").split(",")
        part = {}

        for val in values:
            cat, num = val.split("=")
            part[cat] = int(num)

        parts.append(part)

    return workflows, parts


def checkPart(part: list, workflows: dict[str, list[str]], curr_wf: str) -> bool:
    workflow = workflows[curr_wf]
    final_result = None

    for check in workflow[:-1]:
        cond, rslt = check

        if eval(cond, part):
            final_result = rslt
            break

    if final_result is None:
        final_result = workflow[-1][0]

    if final_result == "A":
        return True
    elif final_result == "R":
        return False
    else:
        return checkPart(part, workflows, final_result)


def checkAllParts(parts: list[dict[str, int]], workflows: dict[str, list[str]]):
    total_rating = 0

    for part in parts:
        curr_rating = sum(part.values())
        if checkPart(part, workflows, "in"):
            total_rating += curr_rating

    return total_rating


def main():
    here = Path(__file__).parent
    with open(here / "test.txt") as file:
        test_data = file.read().splitlines()
        test_workflows, test_parts = parseInput(test_data)

    with open(here / "workflow_parts.txt") as file:
        puzzle_data = file.read().splitlines()
        puzzle_workflows, puzzle_parts = parseInput(puzzle_data)

    print(f"Test Answer: {checkAllParts(test_parts, test_workflows)}")
    print(f"Puzzle Answer: {checkAllParts(puzzle_parts, puzzle_workflows)}")


if __name__ == "__main__":
    main()

