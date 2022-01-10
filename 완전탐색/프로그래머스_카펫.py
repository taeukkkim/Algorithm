def solution(brown, yellow):
    '''
    yellow = (x - 2) * (y - 2) = xy -2x -2y +4
    brown = 2x + 2y - 4
    yellow + brown = xy
    '''
    total = yellow + brown
    for y in range(3, total+1):
        if total % y == 0:
            x = total / y
            if x + y - 2 == brown / 2:
                break
    return [x,y]