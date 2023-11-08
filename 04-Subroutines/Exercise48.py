def f(product_code):
     o = int(product_code[3])
     k = (int(product_code[0])+int(product_code[1])+int(product_code[2]))%7
     if o == k: 
        return True
     else:
        return False
    
if __name__ == "__main__":
    print(f("7071"))