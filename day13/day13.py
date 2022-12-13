class Node:
    def __init__(self):
        self.child_list = []
        self.parent = None

    def add_item(self, item):
        self.child_list.append(item)

    def set_parent(self, parent):
        self.parent = parent

    def in_boundary(self, idx):
        return idx < len(self.child_list)

    def is_node(self, idx):
        return isinstance(self.child_list[idx], Node)

    def is_empty(self):
        return len(self.child_list) == 0


def create_tree(p):
    root = Node()
    current = root
    i = 0
    num_list = [str(i) for i in range(10)]
    while i < len(p):
        if p[i] == "[":
            node = Node()
            node.set_parent(current)
            current.add_item(node)
            current = node
            i += 1
        elif p[i] in num_list:
            num_end = i
            for j in range(i+1, len(p)):
                if p[j] in num_list:
                    num_end += 1
                else:
                    break
            number = int(p[i: num_end+1])
            current.add_item(number)
            i = num_end + 1
        elif p[i] == "]":
            current = current.parent
            i += 1
        else:
            i += 1
    return root


def compare(ptr1, ptr2):
    idx = 0
    while ptr1.in_boundary(idx) and ptr2.in_boundary(idx):
        is_node1, is_node2 = ptr1.is_node(idx), ptr2.is_node(idx)
        v1, v2 = ptr1.child_list[idx], ptr2.child_list[idx]
        if not is_node1 and not is_node2:  # both integers
            if v1 > v2:
                return False
            elif v1 < v2:
                return True
        elif is_node1 and is_node2:  # both lists
            if not compare(v1, v2):
                return False
        elif not is_node1:  # left is integer, right is list
            node = Node()
            node.add_item(v1)
            if not compare(node, v2):
                return False
        elif not is_node2:  # left is list, right is integer
            node = Node()
            node.add_item(v2)
            if not compare(v1, node):
                return False
        idx += 1
    if ptr1.in_boundary(idx) and not ptr2.in_boundary(idx):
        return False
    return True


def is_right_order(f1, f2):
    p1_tree = create_tree(f1)
    p2_tree = create_tree(f2)
    return compare(p1_tree, p2_tree)


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
            if is_right_order(p1, p2):
                num_right += 1
                right_order += count
                print(f">> {count} -th pair is the right order")
            else:
                print(f"{count} -th pair is not the right order")
        print(f"results: {right_order}")
        print(f"num of right order: {num_right}")
p1()