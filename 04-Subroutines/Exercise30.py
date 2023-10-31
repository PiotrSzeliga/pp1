def sum_of_even_or_odd_digits(n,m):
    n = str(n)
    sum = 0
    if m == True:
        for i in n:
            if int(i) % 2 == 0:
                sum += int(i)
    else:
        for i in n:
            if int(i) % 2 != 0:
                sum += int(i)
    return sum


if __name__ == "__main__":
    print(sum_of_even_or_odd_digits(20576,False))
