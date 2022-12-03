def p1():
    with open("input") as f:
        lines = [line.strip("\n") for line in f.readlines()]
        score = 0
        for line in lines:
            l = len(line)
            fpack = line[0:l//2]
            spack = line[l//2:]
            com = {}
            for f in fpack:
                com[f] = 1
            for s in spack:
                if s in com:
                    if ord(s) - ord('a') >= 0:
                        score += ord(s) - ord('a') + 1
                    else:
                        score += ord(s) - ord('A') + 27
                    break
        print(score)
def p2():
    with open("input") as f:
        lines = [line.strip("\n") for line in f.readlines()]
        score = 0
        for idx in range(0,len(lines),3):
            com1 = {}
            for c in lines[idx]:
                if c in com1:
                    com1[c] += 1
                else:
                    com1[c] = 1
            com2 = {}
            for c in lines[idx+1]:
                if c in com2:
                    com2[c] += 1
                else:
                    com2[c] = 1
            com3 = {}
            for c in lines[idx+2]:
                if c in com3:
                    com3[c] += 1
                else:
                    com3[c] = 1
            for c in com1:
                if c in com2 and c in com3:
                    if ord(c) - ord('a') >= 0:
                        score += ord(c) - ord('a') + 1
                    else:
                        score += ord(c) - ord('A') + 27
        print(score)

p2()