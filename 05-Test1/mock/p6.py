def f(number, even):
    sum = 0
    if even == True:
        for i in str(number):
            if int(i)%2 == 0:
                sum+=int(i)
    elif even == False:
        for i in str(number):
            if int(i)%2 != 0:
                sum+=int(i)
    return sum
