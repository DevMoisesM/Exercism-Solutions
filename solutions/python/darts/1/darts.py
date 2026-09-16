def score(x, y):
    origin_x = 0
    origin_y = 0

    radius_outer_circle = 10
    radius_middle_circle = 5
    radius_inner_circle = 1

    squared_distance = (x - origin_x) ** 2 + (y - origin_y) ** 2
    
    if squared_distance <= radius_inner_circle ** 2:
        return 10
    if squared_distance <= radius_middle_circle ** 2:
        return 5
    if squared_distance <= radius_outer_circle ** 2:
        return 1
    return 0