def p1():
    with open("input") as f:
        lines = [l.strip() for l in f.readlines()]
        wid, hig = len(lines[0]), len(lines)
        grid = {}
        num_visible = 0
        get_idx = lambda r, c: r * wid + c
        for r in range(hig):
            for c in range(wid):
                h_tree = int(lines[r][c])
                grid[get_idx(r,c)] = h_tree
        # outer
        for r in range(hig):
            for c in range(wid):
                h_tree = grid[get_idx(r,c)]
                if r == 0 or r == hig-1 or c == 0 or c == wid-1:
                    num_visible += 1

        def is_visible(r, c):
            lef_visible = True
            for i in range(c):
                if grid[get_idx(r,i)] >= grid[get_idx(r,c)]:
                    lef_visible = False
                    break
            right_visible = True
            for i in range(c+1, wid):
                if grid[get_idx(r,i)] >= grid[get_idx(r,c)]:
                    right_visible = False
                    break
            top_visible = True
            for i in range(r):
                if grid[get_idx(i,c)] >= grid[get_idx(r,c)]:
                    top_visible = False
                    break
            low_visible = True
            for i in range(r+1, hig):
                if grid[get_idx(i,c)] >= grid[get_idx(r,c)]:
                    low_visible = False
                    break
            return lef_visible or right_visible or top_visible or low_visible

        # inter
        for r in range(1, hig-1):
            for c in range(1, wid-1):
                if is_visible(r, c):
                    num_visible += 1

        print(num_visible)

p1()

def p2():
    with open("input") as f:
        lines = [l.strip() for l in f.readlines()]
        wid, hig = len(lines[0]), len(lines)
        grid = {}
        num_visible = 0
        get_idx = lambda r, c: r * wid + c
        for r in range(hig):
            for c in range(wid):
                h_tree = int(lines[r][c])
                grid[get_idx(r,c)] = h_tree

        scores = {}
        def compute_score(r, c):
            left_visible_tree = 0
            for i in reversed(range(c)):
                if grid[get_idx(r, i)] >= grid[get_idx(r, c)]:
                    left_visible_tree += 1
                    break
                else:
                    left_visible_tree += 1
            right_visible_tree = 0
            for i in range(c + 1, wid):
                if grid[get_idx(r, i)] >= grid[get_idx(r, c)]:
                    right_visible_tree += 1
                    break
                else:
                    right_visible_tree += 1
            top_visible_tree = 0
            for i in reversed(range(r)):
                if grid[get_idx(i, c)] >= grid[get_idx(r, c)]:
                    top_visible_tree += 1
                    break
                else:
                    top_visible_tree += 1
            low_visible_tree = 0
            for i in range(r + 1, hig):
                if grid[get_idx(i, c)] >= grid[get_idx(r, c)]:
                    low_visible_tree += 1
                    break
                else:
                    low_visible_tree += 1
            return top_visible_tree * low_visible_tree * left_visible_tree * right_visible_tree

        # inter
        for r in range(1, hig-1):
            for c in range(1, wid-1):
                score = compute_score(r, c)
                scores[get_idx(r, c)] = score

        max_scores = 0
        for s in scores:
            if scores[s] > max_scores:
                max_scores = scores[s]
        print(max_scores)

p2()