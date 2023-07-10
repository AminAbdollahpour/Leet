def array_diff(a, b):
    for item in b:
        if item in a:
            for i in range(a.count(item)):
                a.remove(item)
    return a


# def array_diff(a, b):
#     return [x for x in a if x not in b]