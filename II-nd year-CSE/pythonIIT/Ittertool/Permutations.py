import itertools
def print_string_permutations(s):
    perms = itertools.permutations(s)

    print(f"All permutations of the string '{s}':")
    for perm in perms:
        print("".join(perm))
print_string_permutations('123')
