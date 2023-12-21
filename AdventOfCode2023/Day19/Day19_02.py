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
        fail_set[cat][0] = num
    elif sym == '>':
        pass_set[cat][0] = num + 1
        fail_set[cat][1] = num
    
    return pass_set, fail_set


def checkWorkflow(workflows: dict[str, list[str]]):
    start_wf = workflows['in']
    starting_set = {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}
    final_set = []
    ans = 0
    
    def dfs(curr_wf, curr_step, curr_set):
        nonlocal ans
        
        if curr_step == len(curr_wf):
            return
        
        curr_wf_step = curr_wf[curr_step]
        
        if curr_step != len(curr_wf) - 1:
            cond, rslt = curr_wf_step
            pass_set, fail_set = change_conds(cond, curr_set)
            
            if rslt in ['A', 'R']:
                if rslt == 'A':
                    combi = 1
                    for start, end in pass_set.values():
                        combi *= (end - start + 1)
                    ans += combi
                dfs(curr_wf, curr_step+1, fail_set)
            else:
                dfs(workflows[rslt], 0, pass_set)
                dfs(curr_wf, curr_step+1, fail_set)
        else:
            rslt = curr_wf_step[0]
            
            if rslt in ['A', 'R']:
                if rslt == 'A':
                    combi = 1
                    for start, end in curr_set.values():
                        combi *= (end - start + 1)
                    ans += combi
            else:
                dfs(workflows[rslt], 0, curr_set)
        
        pass
    
    dfs(start_wf, 0, starting_set)
    
    return ans


def main():
    here = Path(__file__).parent
    with open(here / "test.txt") as file:
        test_data = file.read().splitlines()
        test_workflows = parseInput(test_data)

    with open(here / "workflow_parts.txt") as file:
        puzzle_data = file.read().splitlines()
        puzzle_workflows = parseInput(puzzle_data)

    print(f"Test Answer: {checkWorkflow(test_workflows)}")
    print(f"Puzzle Answer: {checkWorkflow(puzzle_workflows)}")


if __name__ == "__main__":
    main()

# 167_409_079_868_000
# 167_245_503_449_662