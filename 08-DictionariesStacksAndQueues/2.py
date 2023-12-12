def f(array):
    x = set()
    for i in array:
        x.add(i)
    for b in x:
        if array.count(b)%2 == 0:
            pass
        else:
            return b
        
if __name__ == "__main__":
    print(f([7,7,7,7,4,4,4,5,5]))