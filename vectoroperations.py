import math

def get_magnitude(vec):
    return math.sqrt((vec[0] * vec[0])+(vec[1] * vec[1]))


def get_normalized(vec):
    if get_magnitude(vec) <= 0:
        return (0, 0)
    return (vec[0] / get_magnitude(vec), vec[1]
            / get_magnitude(vec))


def get_dist(vec1, vec2):
    return (vec2[0] - vec1[0], vec2[1] - vec1[1])
