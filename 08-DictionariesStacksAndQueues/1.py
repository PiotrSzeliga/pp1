def f(n):   
    g = [0,1]
    while g[-1] < n:
        g.append(g[-1]+g[-2])
    if g.count(n) == 1:
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(f(1000))
    print(f(2584))
    print(f(4181))