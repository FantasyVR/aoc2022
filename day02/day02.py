def p1():
    stratagy =  {"A":"Y", "B":"Z", "C":"X"}
    stratagy2 = {"X": "B", "Y": "C", "Z":"A"}
    score_dic = {"X":1,"Y":2,"Z":3}
    with open("input") as f:
        lines = [line.strip() for line in f.readlines()]
        score = 0
        for line in lines:
            oponent, me = line.split(" ")
            print(line.split(" "))
            score += score_dic[me]
            if stratagy[oponent] == me: # win
                score += 6
            elif stratagy2[me] == oponent: #lose
                score += 0
            else: #draw
                score += 3
        print(score)

def p2():
    stratagy = {"X": "lose", "Y":"draw", "Z":"win"}
    round = ["A", "B", "C"]
    with open("input") as f:
        lines = [line.strip() for line in f.readlines()]
    score = 0
    for line in lines:
        oponent, stra = line.split(" ")
        idx = round.index(oponent)
        if stratagy[stra] == "win":
            m = {0:2,1:3,2:1}
            score += m[idx]
            score += 6
        elif stratagy[stra] == "draw":
            score += (idx + 1)
            score += 3
        else:
            m = {0:3,1:1,2:2}
            score += m[idx]
    print(score)
p2()