def f(number):
    sum = 0
    set(str(number))
    for i in str(number):
        if i in set:
            sum += i
        

if __name__ == "__main__":
    print(f(1027))