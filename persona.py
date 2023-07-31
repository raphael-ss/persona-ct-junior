def calc_median(iterable:list):
    iterable.sort()
    size = len(iterable)
    index = size // 2
    if size % 2 == 0:
        return (iterable[index] + iterable[index+1]) / 2
    else:
        return iterable[index]



