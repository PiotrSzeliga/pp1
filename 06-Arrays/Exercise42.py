def rand_elem(array):
    import random
    return array[random.randrange(len(array))]

array = [1,6,9,6536,537,34,897,"fah","6"," m349"]
print(rand_elem(array))