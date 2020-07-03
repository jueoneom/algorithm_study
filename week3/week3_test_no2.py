from math import ceil
def solution(l, v):

    v = sorted(v)
    boundary_max = max(v[0], l - v[-1])
    max_distance = 0

    for i in range(len(v) - 1):
        distance = v[i + 1] - v[i]
        if  distance > max_distance:
            max_distance = distance

    max_distance = ceil(max_distance / 2)     

    if max_distance > boundary_max:    
        return ceil(max_distance)
    else:
        return boundary_max