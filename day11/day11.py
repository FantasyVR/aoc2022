import re


class Monkey:
    def __init__(self, id, items, op, op_num, div_num, true_to, false_to):
        self.id = id
        self.items = items
        self.op = op
        self.op_num = op_num
        self.div_num = div_num
        self.true_to = true_to
        self.false_to = false_to

    def remove_item(self):
        return self.items.pop(0)

    def add_item(self, item):
        self.items.append(item)


def p1():
    with open("input") as f:
        lines = [l.strip() for l in f.readlines()]
        monkey_lines = []
        for i in range(0,len(lines),7):
            monkey_lines.append(lines[i:i+6])

        monkes = []
        for m in monkey_lines:
            print(m)
            regex = r"\d"
            matches = re.finditer(regex, m[0], re.MULTILINE)
            monkey_id = 0
            for match in matches:
                monkey_id = int(match.group())
            regex = r"\d+"
            items = []
            matches = re.finditer(regex, m[1], re.MULTILINE)
            for match in matches:
                items.append(int(match.group()))
            regex = r"[\+*-/]"
            op = ""
            matches = re.finditer(regex, m[2], re.MULTILINE)
            for match in matches:
                op = match.group()
            op_num = ""
            regex = r"\d+"
            matches = re.finditer(regex, m[2], re.MULTILINE)
            for match in matches:
                op_num = match.group()
            if op_num == "":
                op_num = "old"
            div_num = 1
            matches = re.finditer(regex, m[3], re.MULTILINE)
            for match in matches:
                div_num = int(match.group())
            true_to = -1
            matches = re.finditer(regex, m[4], re.MULTILINE)
            for match in matches:
                true_to = int(match.group())
            false_to = -1
            matches = re.finditer(regex, m[5], re.MULTILINE)
            for match in matches:
                false_to = int(match.group())
            print(f"true: {true_to}, false: {false_to}")
            m = Monkey(monkey_id, items, op, op_num, div_num, true_to, false_to)
            monkes.append(m)

        print("P1: ")
        start round
        inspect_dic = {}
        for r in range(20):
            print(f"{r} -th round")
            for m in monkes:
                mid, m_items, m_op, m_op_num, m_div_num, m_true_to, m_false_to = m.id, m.items, m.op, m.op_num, m.div_num, m.true_to, m.false_to
                if mid not in inspect_dic:
                    inspect_dic[mid] = len(m_items)
                else:
                    inspect_dic[mid] += len(m_items)
                for i in m_items:
                    wl = i
                    op_old = True if m_op_num == "old" else False
                    if op_old:
                        op_num = wl
                    else:
                        op_num = int(m_op_num)
                    if m_op == "*":
                        wl *= op_num
                    elif m_op == "+":
                        wl += op_num
                    elif m_op == "-":
                        wl -= op_num
                    elif m_op == "/":
                        wl /= op_num
                    else:
                        print("This is not a valid op type!!!!!!!!!!!")
                    wl = int(wl/3)
                    divisible = True if wl % m_div_num == 0 else False
                    if divisible:
                        monkes[m_true_to].add_item(wl)
                    else:
                        monkes[m_false_to].add_item(wl)
                x = len(m_items)
                for i in range(x):
                    monkes[mid].remove_item()

            print(f"After {r} -th round: ------------------")
            for m in monkes:
                mid, m_items, m_op, m_op_num, m_div_num, m_true_to, m_false_to = m.id, m.items, m.op, m.op_num, m.div_num, m.true_to, m.false_to
                print(f"Monkey {mid}: {m_items} ")

            print(f"--------------------------------------")
            for mid in inspect_dic:
                print(f"{mid}: {inspect_dic[mid]}")
            print("\n")

        print("P2: ")
        inspect_dic = {}
        for r in range(10000):
            print(f"{r+1} -th round")
            gcd = 1
            for m in monkes:
                m_div_num = m.div_num
                gcd *= m_div_num
            for m in monkes:
                mid, m_items, m_op, m_op_num, m_div_num, m_true_to, m_false_to = m.id, m.items, m.op, m.op_num, m.div_num, m.true_to, m.false_to
                if mid not in inspect_dic:
                    inspect_dic[mid] = len(m_items)
                else:
                    inspect_dic[mid] += len(m_items)
                for i in m_items:
                    wl = i
                    op_old = True if m_op_num == "old" else False
                    if op_old:
                        op_num = wl
                    else:
                        op_num = int(m_op_num)
                    if m_op == "*":
                        wl *= op_num
                    elif m_op == "+":
                        wl += op_num
                    else:
                        print("This is not a valid op type!!!!!!!!!!!")
                    wl = wl % gcd
                    divisible = True if wl % m_div_num == 0 else False
                    if divisible:
                        monkes[m_true_to].add_item(wl)
                    else:
                        monkes[m_false_to].add_item(wl)
                x = len(m_items)
                for i in range(x):
                    monkes[mid].remove_item()

            print(f"After {r+1} -th round: ------------------")
            for m in monkes:
                mid, m_items = m.id, m.items
                print(f"Monkey {mid}: {m_items} ")

            print(f"--------------------------------------")
            sd = []
            for mid in inspect_dic:
                print(f"{mid}: {inspect_dic[mid]}")
                sd.append(inspect_dic[mid])
            sd = sorted(sd)
            print(f"{sd[-1] * sd[-2]}\n")
p1()