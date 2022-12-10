def p1():
    with open("input") as f:
        lines = [line.strip() for line in f.readlines()]
        X = 1
        cycle = 0
        signal = 0
        for l in lines:
            if "noop" in l:
                cycle += 1
                if cycle % 40 == 20:
                    signal += cycle * X
            else:
                cycle += 1
                if cycle % 40 == 20:
                    signal += cycle * X
                num = int(l.split(" ")[1])
                cycle += 1
                if cycle % 40 == 20:
                    signal += cycle * X
                X += num
        print(signal)
# p1()

def p2():
    with open("input") as f:
        lines = [line.strip() for line in f.readlines()]
        X = 1
        cycle = 0
        s = "."
        for i in range(39):
            s+= "."
        CRT = []
        for i in range(6):
            CRT.append(s)
        init_CRT = CRT.copy()

        def change(screen):
            fuck = False
            row = cycle // 40
            col = cycle % 40
            row = row % 6
            str = screen[row]
            ll = [s for s in str]
            if X == 0 and col in [0, 1]:
                ll[col] = "#"
                screen[row] = ''.join(ll)
            elif X == 39 and col in [38, 39]:
                ll[col] = "#"
                screen[row] = ''.join(ll)
            elif col in [X - 1, X, X + 1]:
                ll[col] = "#"
                screen[row] = ''.join(ll)
            if row == 5 and col == 39:
                fuck = True
                print("-------------------------------------------------------------------------------------")
                for i in range(6):
                    print(screen[i])
            return fuck

        for idx, l in enumerate(lines):
            if "noop" in l:
                restart = change(CRT)
                if restart:
                    CRT = init_CRT.copy()
                cycle += 1
            else:
                num = int(l.split(" ")[1])
                restart = change(CRT)
                if restart:
                    CRT = init_CRT.copy()
                cycle += 1
                restart = change(CRT)
                if restart:
                    CRT = init_CRT.copy()
                cycle += 1
                X += num




p2()