def coins(a):
    counter = 0
    counter += a//5 + a%5//2 + a%5%2
    return counter