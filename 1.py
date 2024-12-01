import pandas as pd

def read_input_txt(path: str):
    with open(path, 'r') as f:
        return f.read().splitlines()

def solve(l1, l2) -> int:
    assert len(l1) == len(l2), Exception("Assumption broken. Code expects equal list lengths l1 and l2")
    dists = []
    while len(l1) > 0 and len(l2) > 0:
        print(len(l1), len(l2))
        a, b = min(l1), min(l2)
        # d_a = l1.index(a)
        # d_b = l2.index(b)
        # dist = abs(d_a - d_b)
        dist = abs(a - b)
        dists.append(dist)
        l1.remove(a)
        l2.remove(b)
    return sum(dists)

if __name__ == "__main__":
    input_txt = read_input_txt("1.txt")
    l1, l2 = [], []
    for line in input_txt:
        a, b = line.split("   ")
        l1.append(int(a))
        l2.append(int(b))

    answer = solve(l1, l2)
    print(answer)