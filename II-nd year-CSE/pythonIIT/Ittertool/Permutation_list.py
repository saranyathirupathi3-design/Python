import itertools

def generate_permutations(input_list):
    perms_iterator = itertools.permutations(input_list)
    perms_list = list(perms_iterator)
    return perms_list
my_list = ['X', 'Y', 'Z']
all_permutations = generate_permutations(my_list)
print(f"Original list: {my_list}")
print("All permutations using itertools.permutations():")
for perm in all_permutations:
    print(perm)
