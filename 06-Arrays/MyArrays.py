def arrayMax(array):
    return max(array)

def arrayDifference(array):
    return max(array)-min(array)

def arrayMedian(array):
    import math
    m = (array[math.ceil((len(array)-1)/2)] + array[math.floor((len(array)-1)/2)])/2
    return m

def arrayMinMax(array):
    n = [min(array),max(array)]
    return n

def arraySep(array):
    g = "-".join(map(str,array))
    return g
