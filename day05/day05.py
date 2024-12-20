
from functools import cmp_to_key

print("Day05")

def parse_input(fn):
    rules_dict = {}
    pages = []
    with open(f"day05/{fn}.txt") as f:
        rules = True
        for line in f.readlines():
            if not line.strip():
                if not rules:
                    break
                rules = False
                continue
            if rules:
                key, val = line.strip().split("|")[:2]
                rules_dict.setdefault(key, []).append(val)
            else:
                pages.append(tuple(line.strip().split(",")))
    return rules_dict, pages

rules_dict, jobs = parse_input("input")
total = 0
fixed_total = 0
for job in jobs:
    filtered_rules = dict(((k, v) for k, v in rules_dict.items() if k in job and set(v)|set(job)))

    # we need to sort the job by all the rules that apply.
    # this means:
    #  * if a page is a key in filtered_rules, it comes before all the pages that are values of that key.
    #  * if a page is a value in filtered_rules, the key comes before
    def orderfunc(left, right):
        if left in filtered_rules and right in filtered_rules[left]:
            return -1
        if right in filtered_rules and left in filtered_rules[right]:
            return 1
        return 0

    sorted_job = tuple(sorted(job, key=cmp_to_key(orderfunc)))
    middle_idx = len(sorted_job)//2
    if sorted_job == job:
        middle_idx = len(sorted_job)//2
        total += int(sorted_job[middle_idx])
    else:
        fixed_total += int(sorted_job[middle_idx])
print(total)
print(fixed_total)
