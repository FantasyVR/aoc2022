def p1():
    with open("input") as f:
        lines = [l.strip() for l in f.readlines()]
        width, height = len(lines[0]), len(lines)
        S_pos = []
        E_pos = []
        for c in range(width):
            for r in range(height):
                if lines[r][c] == "S":
                    S_pos = [r, c]
                elif lines[r][c] == "E":
                    E_pos = [r, c]
                    lines[r] = lines[r][:c] + "z" + lines[r][c+1:]
        print(f"Start pos: {S_pos}, End pos: {E_pos}")

        traversed = [False for i in range(height) for j in range(width)]
        from_pos = [[-1, -1] for i in range(height) for j in range(width)]
        ord_pos = [0 for i in range(height) for j in range(width)]

        def idx(r, c):
            return r * width + c

        stack = [S_pos]
        traversed[idx(S_pos[0], S_pos[1])] = True
        while len(stack) > 0:
            r, c = stack.pop(0)
            elevation = ord(lines[r][c])
            if r == S_pos[0] and c == S_pos[1]:
                elevation = ord('a')

            if r - 1 >= 0 and ord(lines[r - 1][c]) - elevation <= 1 and not traversed[idx(r-1,c)]:
                stack.append([r - 1, c])
                traversed[idx(r-1,c)] = True
                from_pos[idx(r-1,c)] = [r, c]
                ord_pos[idx(r-1,c)] = ord_pos[idx(r,c)] + 1
            if r + 1 < height and ord(lines[r + 1][c]) - elevation <= 1 and not traversed[idx(r+1, c)]:
                stack.append([r + 1, c])
                traversed[idx(r+1, c)] = True
                from_pos[idx(r+1, c)] = [r, c]
                ord_pos[idx(r+1, c)] = ord_pos[idx(r,c)] + 1
            if c - 1 >= 0 and ord(lines[r][c - 1]) - elevation <= 1 and not traversed[idx(r, c-1)]:
                stack.append([r, c - 1])
                traversed[idx(r, c-1)] = True
                from_pos[idx(r, c-1)] = [r, c]
                ord_pos[idx(r, c-1)] = ord_pos[idx(r,c)] + 1
            if c + 1 < width and ord(lines[r][c + 1]) - elevation <= 1 and not traversed[idx(r,c + 1)]:
                stack.append([r, c + 1])
                traversed[idx(r,c + 1)] = True
                from_pos[idx(r,c + 1)] = [r, c]
                ord_pos[idx(r,c + 1)] = ord_pos[idx(r,c)] + 1

        for i in range(height):
            for j in range(width):
                print(ord_pos[idx(i, j)], end=" ")
            print("\n")

        print("result:")
        print(ord_pos[idx(E_pos[0], E_pos[1])])
# p1()


def p2():
    with open("input") as f:
        lines = [l.strip() for l in f.readlines()]
        width, height = len(lines[0]), len(lines)
        S_pos = []
        E_pos = []
        S_pos_list = []
        for c in range(width):
            for r in range(height):
                if lines[r][c] == "S":
                    S_pos = [r, c]
                    lines[r] = lines[r][:c] + "a" + lines[r][c + 1:]
                elif lines[r][c] == "E":
                    E_pos = [r, c]
                    lines[r] = lines[r][:c] + "z" + lines[r][c+1:]

        for c in range(height):
            S_pos_list.append([c, 0])

        print(f"Start pos: {S_pos}, End pos: {E_pos}")

        def compute_dis(start_pos, end_pos):
            traversed = [False for i in range(height) for j in range(width)]
            from_pos = [[-1, -1] for i in range(height) for j in range(width)]
            ord_pos = [0 for i in range(height) for j in range(width)]

            def idx(r, c):
                return r * width + c

            stack = [start_pos]
            traversed[idx(start_pos[0], start_pos[1])] = True
            while len(stack) > 0:
                r, c = stack.pop(0)
                elevation = ord(lines[r][c])
                if r == start_pos[0] and c == start_pos[1]:
                    elevation = ord('a')

                if r - 1 >= 0 and ord(lines[r - 1][c]) - elevation <= 1 and not traversed[idx(r-1,c)]:
                    stack.append([r - 1, c])
                    traversed[idx(r-1,c)] = True
                    from_pos[idx(r-1,c)] = [r, c]
                    ord_pos[idx(r-1,c)] = ord_pos[idx(r,c)] + 1
                if r + 1 < height and ord(lines[r + 1][c]) - elevation <= 1 and not traversed[idx(r+1, c)]:
                    stack.append([r + 1, c])
                    traversed[idx(r+1, c)] = True
                    from_pos[idx(r+1, c)] = [r, c]
                    ord_pos[idx(r+1, c)] = ord_pos[idx(r,c)] + 1
                if c - 1 >= 0 and ord(lines[r][c - 1]) - elevation <= 1 and not traversed[idx(r, c-1)]:
                    stack.append([r, c - 1])
                    traversed[idx(r, c-1)] = True
                    from_pos[idx(r, c-1)] = [r, c]
                    ord_pos[idx(r, c-1)] = ord_pos[idx(r,c)] + 1
                if c + 1 < width and ord(lines[r][c + 1]) - elevation <= 1 and not traversed[idx(r,c + 1)]:
                    stack.append([r, c + 1])
                    traversed[idx(r,c + 1)] = True
                    from_pos[idx(r,c + 1)] = [r, c]
                    ord_pos[idx(r,c + 1)] = ord_pos[idx(r,c)] + 1

            for i in range(height):
                for j in range(width):
                    print(ord_pos[idx(i, j)], end=" ")
                print("\n")

            # print("result:")
            # print(ord_pos[idx(end_pos[0], end_pos[1])])
            return ord_pos[idx(end_pos[0], end_pos[1])]

        dis = []
        for s in S_pos_list:
            dis.append(compute_dis(s, E_pos))
        print("The shorted path: ")
        print(sorted(dis)[0])
p2()
