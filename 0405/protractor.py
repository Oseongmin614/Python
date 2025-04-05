def solution(angle):
    conditions = (
        (angle < 90, 1),
        (angle == 90, 2),
        (angle < 180, 3),
        (angle == 180, 4),
    )

    for condition, result in conditions:
        if condition:
            return result