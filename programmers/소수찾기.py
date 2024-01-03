from itertools import permutations

def solution(numbers):
    new_numbers = set()
    for i in range(len(numbers)):
        permutations_lst = map(int, map("".join, list(permutations(list(numbers), i+1))))
        new_numbers |= set(permutations_lst)
        
    new_numbers -= set([0,1])
    lim = int(max(new_numbers) ** 0.5) + 1
    for i in range(2, lim):
        for j in range(i * 2, max(new_numbers) + 1, i):
            new_numbers -= set([j])

    return len(new_numbers)