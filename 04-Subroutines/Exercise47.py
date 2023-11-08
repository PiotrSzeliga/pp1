def f(text):
    text2 = []
    for i in text:
        text2.append(i)
    text3 = "-".join(text2)    
    return text3
if __name__ == "__main__":
    print(f("Univesity"))