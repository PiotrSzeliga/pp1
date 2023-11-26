array = [12,6,4,9,10]
def start(n):
    list = []
    for i in array:
        list.append(f"{i:>2}: {i*"*"}")
    return "\n".join(list)

print(start(array))