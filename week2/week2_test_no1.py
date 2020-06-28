def solution(seat):
    seat_set = set()
    for s in seat:
        seat_set.add(tuple(s))

    return len(seat_set)