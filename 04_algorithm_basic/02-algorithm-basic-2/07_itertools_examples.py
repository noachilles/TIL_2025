import itertools
arr = [1, 2, 3]

print(tuple(itertools.permutations(arr)))  # 순열
# ((1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1))

print(tuple(itertools.combinations(arr, 2)))  # 조합
# ((1, 2), (1, 3), (2, 3))

print(tuple(itertools.product(arr, repeat=2)))  # 중복순열
# ((1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3))

print(tuple(itertools.combinations_with_replacement(arr, 2)))  # 중복조합
# ((1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3))
