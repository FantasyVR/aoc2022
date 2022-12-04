def is_overlape(first, second):
    if first[0] >= second[0] and first[1] <= second[1]:
        return True
    if first[0] <= second[0] and first[1] >= second[1]:
        return True

def p1():
    with open("input") as f:
        lines = [line.strip() for line in f.readlines()]
        overlape = 0
        for line in lines:
            one, two = line.split(",")
            fir_sec = [int(i) for i in one.split("-")]
            sec_sec = [int(i) for i in two.split("-")]
            if is_overlape(fir_sec, sec_sec):
                overlape+=1
        print(overlape)
p1()

def is_cross(first, second):
    if first[1] < second[0] or first[0] > second[1]:
        return False
    return True

def p2():
    with open("input") as f:
        lines = [line.strip() for line in f.readlines()]
        overlape = 0
        for line in lines:
            one, two = line.split(",")
            fir_sec = [int(i) for i in one.split("-")]
            sec_sec = [int(i) for i in two.split("-")]
            if is_cross(fir_sec, sec_sec):
                overlape+=1
        print(overlape)

p2()