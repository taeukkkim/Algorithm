from itertools import product

def solution(numbers, target):
    num_list = [(n,-n) for n in numbers]
    ans_list = list(map(sum,product(*num_list)))
    return ans_list.count(target)