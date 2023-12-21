#!/usr/bin/env python3

from pathlib import Path


def parseInput(file: list):
    workflows = {}
    split = file.index("")

    for line in file[:split]:
        name, steps = line.split("{")
        steps = [x.split(":") for x in steps.rstrip("}").split(",")]
        workflows[name] = steps

    return workflows


def change_conds(cond: str, curr_set: dict[str, list[int]]):
    cat = cond[0]
    sym = cond[1]
    num = int(cond[2:])
    pass_set = {key: value[:] for key, value in curr_set.items()}
    fail_set = {key: value[:] for key, value in curr_set.items()}
    
    if sym == '<':
        pass_set[cat][1] = num - 1
        fail_set[cat][0] = num + 1
    elif sym == '>':
        pass_set[cat][0] = num + 1
        fail_set[cat][1] = num - 1
    
    return pass_set, fail_set


def checkWorkflow(workflows: dict[str, list[str]]):
    start_wf = workflows['in']
    starting_set = {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}
    final_set = []
    
    def dfs(curr_wf, curr_set):
        # print(curr_set)
        # print(curr_wf)
        # print(curr_wf[curr_step])
        # print(list(workflows.keys())[list(workflows.values()).index(curr_wf)])
        for i in range(len(curr_wf)):
            curr_wf_step = curr_wf[i]

            if len(curr_wf_step) == 1:
                rslt = curr_wf_step[0]
                pass_set = {key: value[:] for key, value in curr_set.items()}
            else:
                cond, rslt = curr_wf_step
                pass_set, fail_set = change_conds(cond, curr_set)
        
            if rslt == 'A':
                print('accepted', pass_set)
                final_set.append(pass_set)
                continue
            elif rslt == 'R':
                continue
            else:
                dfs(workflows[rslt], pass_set)
    
    dfs(start_wf, starting_set)
    
    ans = 0
    for s in final_set:
        combi = 1
        for start, end in s.values():
            combi = combi * (end - start + 1)
        ans += combi
    
    return ans


def main():
    here = Path(__file__).parent
    with open(here / "test.txt") as file:
        test_data = file.read().splitlines()
        test_workflows = parseInput(test_data)

    with open(here / "workflow_parts.txt") as file:
        puzzle_data = file.read().splitlines()
        puzzle_workflows = parseInput(puzzle_data)

    # print(test_workflows)
    print(checkWorkflow(test_workflows))
    # print(f"Test Answer: {checkAllParts(test_parts, test_workflows)}")
    # print(f"Puzzle Answer: {checkAllParts(puzzle_parts, puzzle_workflows)}")


if __name__ == "__main__":
    main()

# 167_409_079_868_000
# 496_534_091_000_000