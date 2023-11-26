def wordsNumber(n):
    l = n.split()
    counter = 0
    for i in l:
        counter += 1
    return counter

def lenOrder(n):
    l = n.split()
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0,len(l)-1):
            if len(l[i])>len(l[i+1]):
                sorted = False
                l[i], l[i+1] = l[i+1], l[i]
    return l

def lenOrder2(n):
    l = n.split()
    n = sorted(l,key=len)
    return n

def alphOrder(n):
    l = n.split()
    n = sorted(l)
    return n


