import numpy as np
with open("input") as f:
    lines = f.readlines()
    elf = []
    sum = 0
    for i, line in enumerate(lines):
        if line.strip() == "":
            elf.append(sum)
            sum = 0
            continue
        energy = int(line)
        sum += energy
    elf_np = np.asarray(elf)
    elf_sort = np.sort(elf_np)
    print(f"1st problem: {np.max(elf_np)}")
    print(f"second problem: {elf_sort[-1]+elf_sort[-2]+elf_sort[-3]}")
