def f(number1,number2,number3):
    m = [number1,number2,number3]
    return max(m)-min(m)

if __name__ == "__main__":
    print(f(2,12,8))