def f(n):
    prime = []
    number = 2
    while len(prime) != n:
        for i in range(2,number):
            if number%i == 0:
                number += 1
                continue
            else:
                prime.append(number)
    return prime[n]

if __name__ == "__main__":
    print(f(5))