import re

def find(str):
    regex = r"\d+"
    matches = re.finditer(regex, str, re.MULTILINE)
    result = []
    for matchNum, match in enumerate(matches, start=1):
        result.append(int(match.group()) - 1)
    result[0] += 1
    return result

def p1():
    with open("input") as f:
        lines = f.readlines()
        stacks_line = []

        start_operation = 0
        for l in lines:
            start_operation += 1
            if l[1] == "1":
                stack_id = [int(id) for id in l.strip().split(" ") if id != ""]
                num_stacks = max(stack_id)
                print(num_stacks)
                break
            stacks_line.append(l)

        stacks = [['0'] for i in range(num_stacks)]
        for l in reversed(range(len(stacks_line))):
            line = stacks_line[l]
            max_s = len(line)//4
            for i in range(max_s):
                if line[1+4*i] != " ":
                    stacks[i].append(line[1+4*i])
        for s in stacks:
            print(s)
        operations = []
        for i in range(start_operation, len(lines)):
            if lines[i][0] == 'm':
                operation=find(lines[i])
                operations.append(operation)
                print(operation)
        for op in operations:
            num, start, end = op
            moved = stacks[start][-num:]
            stacks[start] = stacks[start][:-num]
            for i in reversed(range(len(moved))):
                stacks[end].append(moved[i])
        last = []
        for s in stacks:
            last.append(s[-1])
        print(last)

def p2():
    with open("input") as f:
        lines = f.readlines()
        stacks_line = []

        start_operation = 0
        for l in lines:
            start_operation += 1
            if l[1] == "1":
                stack_id = [int(id) for id in l.strip().split(" ") if id != ""]
                num_stacks = max(stack_id)
                print(num_stacks)
                break
            stacks_line.append(l)

        stacks = [['0'] for i in range(num_stacks)]
        for l in reversed(range(len(stacks_line))):
            line = stacks_line[l]
            max_s = len(line)//4
            for i in range(max_s):
                if line[1+4*i] != " ":
                    stacks[i].append(line[1+4*i])
        for s in stacks:
            print(s)
        operations = []
        for i in range(start_operation, len(lines)):
            if lines[i][0] == 'm':
                operation=find(lines[i])
                operations.append(operation)
                print(operation)
        for op in operations:
            num, start, end = op
            moved = stacks[start][-num:]
            stacks[start] = stacks[start][:-num]
            for i in range(len(moved)):
                stacks[end].append(moved[i])
        last = []
        for s in stacks:
            last.append(s[-1])
        print(last)

p2()