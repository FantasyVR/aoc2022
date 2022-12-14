from itertools import zip_longest


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left - right

    if isinstance(left, list) and isinstance(right, list):
        for l, r in zip_longest(left, right, fillvalue=None):
            if l is None:
                return -1
            if r is None:
                return 1
            cmp = compare(l, r)
            if cmp != 0:
                return cmp
        return 0

    if isinstance(left, int):
        left = [left]
    if isinstance(right, int):
        right = [right]
    return compare(left, right)


def is_right_order(f1, f2):
    return compare(eval(f1), eval(f2))


def p1():
    with open("test") as f:
        lines = [l.strip() for l in f.readlines()]
        right_order = 0
        count = 0
        num_right = 0
        for i in range(0, len(lines), 3):
            count += 1
            p1 = lines[i]
            p2 = lines[i+1]
            if is_right_order(p1, p2) < 0:
                num_right += 1
                right_order += count
                print(f">> {count} -th pair is the right order")
            else:
                print(f"{count} -th pair is not the right order")
        print(f"results: {right_order}")
        print(f"num of right order: {num_right}")
p1()