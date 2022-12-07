class Node:
    def __init__(self, type, name, size=-1, parent=None):
        self.type = type
        self.name = name
        self.children = []
        self.size = size
        self.parent = parent

    def insert_child(self, type, name, size):
        self.children.append(Node(type, name, size, self))

    def is_leaf(self):
        return len(self.children) == 0

    def get_parent(self):
        return self.parent

    def get_children(self):
        return self.children

    def get_type(self):
        return self.type

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size


def traverse_recursive(root):
    if root.get_type() == "file":
        return root.get_size()
    children = root.get_children()
    size = 0
    for c in children:
        if c.get_type() == "file":
            size += c.get_size()
        else:
            size += traverse_recursive(c)
    root.set_size(size)
    return size


def traverse_recursive_result(root, threshold):
    result = 0
    if root.get_type() == "dir":
        if root.get_size() <= threshold:
            result += root.get_size()
        children = root.get_children()
        for c in children:
            result += traverse_recursive_result(c, threshold)
    return result


def traverse_recursive_p2(root):
    dir_size = []
    if root.get_type() == "dir":
        dir_size.append(root.get_size())
        children = root.get_children()
        for c in children:
            result = traverse_recursive_p2(c)
            dir_size = dir_size + result
    return dir_size


def p1():
    with open("input") as f:
        lines = f.readlines()
        for lidx, line in enumerate(lines):
            if line[0] == "$":
                if line[2:4] == "ls":
                    pass
                    # print(lidx, "ls")
                elif line[2:4] == "cd":
                    if ".." in line[4:]:
                        # print(lidx, "cd ..")
                        current = current.get_parent()
                    elif "/" in line[4:]:
                        # print(lidx, "cd /")
                        root = Node("dir", "/", -1)
                        current = root
                    else:
                        dest = line[4:].strip()
                        children = current.get_children()
                        for c in children:
                            if c.get_type() == "dir" and c.get_name() == dest:
                                current = c
                                break
                        # print(lidx, "cd: ",  dest)
            elif line[0:3] == "dir":
                current.insert_child("dir", line[3:].strip(), -1)
            else:
                file_size, name = line.strip().split(" ")
                current.insert_child("file", name, int(file_size))
                # print(name, file_size)

    traverse_recursive(root)

    results = traverse_recursive_result(root, 100000)
    print(f"p1: {results}")

    # --------- p2 ------------
    used_mem = root.get_size()
    free_mem = 70000000 - used_mem
    need_mem = 30000000 - free_mem
    # sort dir size and find the first that is bigger than need_mem
    dir_size = traverse_recursive_p2(root)
    dir_size.sort()
    for ds in dir_size:
        if ds > need_mem:
            print(f"p2: {ds}")
            break

p1()