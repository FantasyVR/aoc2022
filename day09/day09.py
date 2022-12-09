def p1():
    with open("input") as f:
        lines = [l.strip() for l in f.readlines()]
        ops = {}
        for i, l in enumerate(lines):
            dir, steps = l.split(" ")
            ops[i] = [dir, int(steps)]
        for op in ops:
            print(f"{op}: {ops[op]}")

        tail = [0, 0]
        head = tail.copy()

        def update_tail():
            index = str(tail)
            if index in traversed_grid:
                traversed_grid[index] += 1
            else:
                traversed_grid[index] = 1

        def is_adjacent(a, b):
            is_ad = False
            for i in range(-1, 2, 1):
                for j in range(-1,2,1):
                    if b[0] + i == a[0] and b[1] + j == a[1]:
                        is_ad = True
            return is_ad

        dir_op = {"R": [1, 0], "L": [-1, 0], "U": [0, 1], "D": [0, -1]}

        traversed_grid = {str(tail): 1}
        for op in ops:
            dir, steps = ops[op]
            for s in range(steps):
                init_head = head.copy()
                move = dir_op[dir]
                head[0] += move[0]
                head[1] += move[1]
                if not is_adjacent(head, tail):
                    tail[0] = init_head[0]
                    tail[1] = init_head[1]
                    update_tail()

        # print(len(traversed_grid))


# p1()

def p2():
    with open("input") as f:
        lines = [l.strip() for l in f.readlines()]
        ops = {}
        for i, l in enumerate(lines):
            dir, steps = l.split(" ")
            ops[i] = [dir, int(steps)]
        for op in ops:
            print(f"{op}: {ops[op]}")

        rope = [[0,0] for i in range(10)]

        def update_tail():
            index = str(f"{rope[9][0]},{rope[9][1]}")
            if index in traversed_grid:
                traversed_grid[index] += 1
            else:
                traversed_grid[index] = 1

        def is_adjacent(a, b):
            is_ad = False
            for i in range(-1, 2, 1):
                for j in range(-1,2,1):
                    if b[0] + i == a[0] and b[1] + j == a[1]:
                        is_ad = True
            return is_ad

        def show(r):
            print("-------------start----------------")
            for j in reversed(range(-10, 16)):
                for i in range(-15, 15):
                    if [i, j] in r:
                        idx = r.index([i,j])
                        print(f" {idx} ", end="")
                    else:
                        print(" . ", end="")
                print("\n")
            print("--------------end---------------")


        def is_move_diag(r1, r2):
            return abs(r1[0] - r2[0]) + abs(r1[1] - r2[1]) == 2

        def is_align(a, b):
            return a[0] == b[0] or a[1] == b[1]

        dir_op = {"R": [1, 0], "L": [-1, 0], "U": [0, 1], "D": [0, -1]}

        traversed_grid = {str(f"{rope[9][0]},{rope[9][1]}"): 1}
        for op in ops:
            dir, steps = ops[op]
            for s in range(steps):
                init_rope = [[i, j] for [i, j] in rope]
                # show(init_rope)
                move = dir_op[dir]
                rope[0][0] += move[0]
                rope[0][1] += move[1]
                for i in range(1, 10):
                    if not is_adjacent(rope[i], rope[i-1]):
                        if is_move_diag(rope[i-1], init_rope[i-1]):
                            if is_align(rope[i], rope[i-1]):
                                a, b = rope[i], rope[i-1]
                                if a[0] == b[0]:
                                    rope[i][1] +=int((rope[i-1][1] - rope[i][1]) / 2)
                                else:
                                    rope[i][0] += int((rope[i-1][0] - rope[i][0]) / 2)
                            else:
                                rope[i][0] += rope[i-1][0] - init_rope[i-1][0]
                                rope[i][1] += rope[i-1][1] - init_rope[i-1][1]
                        else:
                            rope[i][0] = init_rope[i-1][0]
                            rope[i][1] = init_rope[i-1][1]
                update_tail()

        print(len(traversed_grid))

        def show_tail():
            print("\n\n\n")
            for j in reversed(range(-15, 15)):
                for i in range(-15, 15):
                    if f"{i},{j}" in traversed_grid:
                        print(" # ", end="")
                    else:
                        print(" . ", end="")
                print("\n")
            print("\n\n\n")

        # show_tail()

p2()

