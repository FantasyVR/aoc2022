def p1():
    with open("input") as f:
        lines = f.readlines()
        line = lines[0].strip()
        window = line[:3]
        for i in range(3,len(line)):
            c = line[i]
            if c not in window:
                if  len(window) == 4:
                    print(i)
                    break
                else:
                    window += c
                    continue

            idx = window.index(c)
            window = window[idx+1:]
            window += c

def is_unique(message):
    m_dic = {}
    unique = True
    rep = ""
    for i, m in enumerate(message):
        if m in m_dic:
            rep = m
            m_dic[m].append(i)
            unique = False
        else:
            m_dic[m] = [i]
    if rep != "":
        return unique, m_dic[rep][-2]

def p2():
    with open("input") as f:
        lines = f.readlines()
        line = lines[0].strip()
        window = line[:13]
        unique, idx = is_unique(window)
        if not unique:
            window = window[idx+1:]
        for i in range(13,len(line)):
            if len(window) == 14:
                print(i)
                break
            c = line[i]
            if c not in window:
                    window += c
                    continue
            else:
                idx = window.index(c)
                window = window[idx+1:]
                window += c


p2()