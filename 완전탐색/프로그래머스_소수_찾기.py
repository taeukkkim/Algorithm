from itertools import permutations

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    per_list = []
    
    for i in range(1, len(numbers)+1):
        per_list.extend(permutations(numbers,i))
    per_list = [int(''.join(per)) for per in per_list]
    per_list = set(per_list)
    
    for num in per_list:
        if num >= 2:
            flag = True
            for i in range(2,int(num**0.5) + 1):
                if num % i == 0:
                    flag = False
                    break
                    
            if flag:
                answer += 1
                    
    return answer