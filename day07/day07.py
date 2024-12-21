import pprint
import itertools

def load_equations(fn):
    equations = []
    with open(f"day07/{fn}.txt") as f:
        for line in f.readlines():
            a = line.strip().split(':')
            equations.append(
                (int(a[0].strip()), [int(b.strip()) for b in a[1].split(' ') if b != ''])
            )
    return equations


class add:
    def __call__(self, a, b):
        return a + b
    def __repr__(self):
        return ' + '

class mul:
    def __call__(self, a, b):
        return a * b
    def __repr__(self):
        return ' * '

def fmt_equation(operands, operators, result):
    return f"{result} = {''.join([str(x) for t in itertools.zip_longest(operands, operators, fillvalue='') for x in t])}"

def check_equation(equation):
    result, operands = equation
    a = add()
    m = mul()
    ops = [a, m]
    num_operators = len(operands) - 1
    possible_combinations = list(reversed(tuple(itertools.product(ops, repeat=num_operators))))
    # print(possible_combinations)
    for combo in possible_combinations:
        check_result = operands[0]
        for op, v in zip(combo, operands[1:]):
            check_result = op(check_result, v)
        if check_result == result:
            print(f"Found equation: {fmt_equation(operands, combo, result)}")
            return result
    return 0

class concat:
    def __call__(self, a, b):
        return int(str(a) + str(b))
    def __repr__(self):
        return ' || '

def check_with_merge(equation):
    result, operands = equation
    a = add()
    m = mul()
    c = concat()
    ops = [a, m, c]
    num_operators = len(operands) - 1
    possible_combinations = list(reversed([combo for combo in itertools.product(ops, repeat=num_operators) if c in combo]))
    for combo in possible_combinations:
        check_result = operands[0]
        for op, v in zip(combo, operands[1:]):
            check_result = op(check_result, v)
        if check_result == result:
            print(f"Found equation: {fmt_equation(operands, combo, result)}")
            return result
    return 0


def main():
    print("Day07")
    equations = load_equations("input")
    failed_equations = []
    total = 0
    for idx, eq in enumerate(equations):
        print(f"Checking equation {idx + 1} of {len(equations)}")
        res = check_equation(eq)
        if res == 0:
            failed_equations.append(eq)
        total += res
    total_part_one = total

    # Part 2
    # Check all the failed equations again with merging
    for idx, eq in enumerate(failed_equations):
        print(f"Checking equation {idx + 1} of {len(failed_equations)}")
        total += check_with_merge(eq)
    print(total_part_one)
    print(total)


if __name__ == "__main__":
    main()

