keypad = 7
while keypad > 0:
    if keypad%3 != 0:
        print(keypad,end=" " )
        keypad += 1
    else:
        print(keypad)
        keypad -= 5