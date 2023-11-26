array = [34,7,19,4,21,8]
def program(n):
    even = 0
    for i in n:
        if i%2 == 0:
            even += i      
    return even

print(program(array))