def is_triangle(func):
    def wrap_func(sides):
        return 0 not in sides and max(sides) <= sum(sides) - max(sides) and func(sides)
    return wrap_func


@is_triangle
def equilateral(sides):
    return len(set(sides)) == 1


@is_triangle
def isosceles(sides):
    return 1 <= len(set(sides)) <= 2


@is_triangle
def scalene(sides):
    return len(set(sides)) == 3
