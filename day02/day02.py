with open("day02/data.txt", "r") as f:
    lines = [list(map(int, entry)) for entry in [l.strip().split(' ') for l in f.readlines()]]

def isvalid(entry: list[int]):
    pairs = list(zip(entry[0:],entry[1:]))
    if not all(item[0] > item[1] for item in pairs) and not all(item[0] < item[1] for item in pairs):
        return False
    return all(abs(item[0] - item[1]) >= 1 and abs(item[0] - item[1]) <= 3 for item in pairs)
print()
print(sum(1 for line in lines if isvalid(line)))


# part 2
def isvalid_lenient(entry: list[int]):
    if isvalid(entry):
        return True
    for idx in range(len(entry)):
        if isvalid(entry[0:idx] + entry[idx+1:]):
            return True
    return False
print()
print(sum(1 for line in lines if isvalid_lenient(line)))
