import itertools

def permutations_without_repetition(digits):
    return list(itertools.permutations(digits))

def permutations_with_repetition(digits, r):
    return list(itertools.product(digits, repeat=r))

digits = [1, 2, 3]

print("Without repetition:")
print(permutations_without_repetition(digits))

print("\nWith repetition (length 3):")
print(permutations_with_repetition(digits, 3))
