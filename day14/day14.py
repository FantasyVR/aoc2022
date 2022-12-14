import math

class vec2:
    def __init__(self, x, y=None):
        if isinstance(x, int):
            self.x = x
            self.y = y
        elif isinstance(x, tuple):
            self.x = x[0]
            self.y = x[1]
    def __sub__(self, pos):
        x = self.x - pos.x
        y = self.y - pos.y
        return vec2(x,y)
    def __add__(self, pos):
        x = self.x + pos.x
        y = self.y + pos.y
        return vec2(x,y)
    def __mul__(self, other):
        return vec2( int(self.x * other), int(self.y * other))
    def __rmul__(self, other):
        return vec2( int(self.x * other), int(self.y * other))
    def n(self):
        res = vec2(0,0)
        len = self.dis()
        if len > 0:
            res = vec2(int(self.x/len), int(self.y/len))
        return res
    def dis(self):
        return int(math.sqrt(self.x * self.x + self.y * self.y))
    def dir(self):
        if self.x != 0:
            return 1
        elif self.y != 0:
            return -1
    def __str__(self):
        return f"({self.x}, {self.y})"
    def __repr__(self):
        return f"({self.x}, {self.y})"

def p1():
    with open("test") as f:
        lines = [l.strip() for l in f.readlines()]
        rocks = set()
        for line in lines:
            pos = [eval(x) for x in line.split("->")]
            for i in range(len(pos)-1):
                v1 = vec2(pos[i])
                v2 = vec2(pos[i+1])
                d = v2 - v1
                l = d.dis()
                n = d.n()
                rocks.add((v1.x, v1.y))
                for i in range(l):
                    p = v1 + (i+1) * n
                    rocks.add((p.x, p.y))

        max_y = 0
        for r in rocks:
            if r[1] > max_y:
                max_y = r[1]
        print(f"max_y: {max_y}")
        floor_y = max_y + 2

        print(len(rocks))
        dir = [vec2(0, 1), vec2(-1, 1), vec2(1, 1)]

        def step(sand):
            for d in dir:
                res = sand + d
                if (res.x, res.y) not in rocks:
                    return res
            return sand

        def is_rest(sand):
            all_rocks = True
            for d in dir:
                p = sand + d
                if (p.x, p.y) not in rocks:
                    all_rocks = False
            return all_rocks


        num_rest = 0
        terminate = False
        rest_sand = []
        while(not terminate):
            sand = vec2(500, 0)
            if is_rest(sand):
                num_rest += 1
                rest_sand.append(sand)
                continue
            num_steps = 0
            while(not terminate):
                next_sand = step(sand)
                num_steps += 1
                if is_rest(next_sand):
                    num_rest += 1
                    rest_sand.append(next_sand)
                    rocks.add((next_sand.x, next_sand.y))
                    break
                else:
                    sand = next_sand
                if num_steps > 1000000:
                    terminate = True

        print(f"P1: {num_rest}")

p1()

def p2():
    with open("input") as f:
        lines = [l.strip() for l in f.readlines()]
        rocks = set()
        for line in lines:
            pos = [eval(x) for x in line.split("->")]
            for i in range(len(pos)-1):
                v1 = vec2(pos[i])
                v2 = vec2(pos[i+1])
                d = v2 - v1
                l = d.dis()
                n = d.n()
                rocks.add((v1.x, v1.y))
                for i in range(l):
                    p = v1 + (i+1) * n
                    rocks.add((p.x, p.y))

        max_y = 0
        for r in rocks:
            if r[1] > max_y:
                max_y = r[1]
        # print(f"max_y: {max_y}")
        floor_y = max_y + 2

        # print(len(rocks))
        dir = [vec2(0, 1), vec2(-1, 1), vec2(1, 1)]

        def step(sand):
            for d in dir:
                res = sand + d
                if (res.x, res.y) not in rocks:
                    return res
            return sand

        def is_rest(sand, max_y):
            all_rocks = True
            for d in dir:
                p = sand + d
                if (p.x, p.y) not in rocks and p.y != max_y:
                    all_rocks = False
            return all_rocks


        num_rest = 0
        terminate = False
        rest_sand = []
        while(not terminate):
            sand = vec2(500, 0)
            if is_rest(sand, floor_y):
                num_rest += 1
                rest_sand.append(sand)
                terminate = True
            num_steps = 0
            while(not terminate):
                next_sand = step(sand)
                num_steps += 1
                if is_rest(next_sand, floor_y):
                    num_rest += 1
                    rest_sand.append(next_sand)
                    rocks.add((next_sand.x, next_sand.y))
                    break
                else:
                    sand = next_sand

        print(f"P2: {num_rest}")

p2()

