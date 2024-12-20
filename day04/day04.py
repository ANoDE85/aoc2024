import re
import pprint


print("Day04")


def load_matrix(fn):
    with open(f"day04/{fn}") as f:
        data = [
            [c for c in line.strip()] for line in f.readlines()
        ]
    return data


from collections import defaultdict
def groups(data, func):
    grouping = defaultdict(list)
    for y in range(len(data)):
        for x in range(len(data[y])):
            grouping[func(x, y)].append(data[y][x])
    return list(map(grouping.get, sorted(grouping)))

def count_all(fn):
    test = load_matrix(fn)

    cols = groups(test, lambda x, y: x)
    rows = groups(test, lambda x, y: y)
    fdiag = groups(test, lambda x, y: x + y)
    bdiag = groups(test, lambda x, y: x - y)

    xmas_pat = re.compile("XMAS")
    samx_pat = re.compile("SAMX")

    count = 0
    for group in [cols, rows, fdiag, bdiag]:
        for line in group:
            count += len(xmas_pat.findall("".join(line))) + len(samx_pat.findall("".join(line)))
    print(count)

count_all("test_input.txt")
count_all("input.txt")

#Part 2
def count_diagonally(fn):
    count = 0
    data = load_matrix(fn)
    for row_idx, row in enumerate(data):
        for col_idx, c in enumerate(row):
            if c in ("M", "S"):
                try:
                    matrix = [
                        [data[row_idx][col_idx],   ".",                        data[row_idx][col_idx + 2]],
                        [".",                      data[row_idx+1][col_idx+1], "."],
                        [data[row_idx+2][col_idx], ".",                        data[row_idx+2][col_idx + 2]]
                    ]
                except IndexError:
                    break
                fdiag = "".join([diag for diag in groups(matrix, lambda x, y: x + y) if len(diag) == 3][0])
                bdiag = "".join([diag for diag in groups(matrix, lambda x, y: x - y) if len(diag) == 3][0])
                if fdiag in ("MAS", "SAM") and bdiag in ("MAS", "SAM"):
                    count += 1
    print(count)


count_diagonally("part2_test.txt")
count_diagonally("input.txt")