def month_from_number(n):
    list = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    return list[n-1]

def letter_in_text(l):
    text = input("Input text: ")
    return f"The number of letter {l}: {text.count(l)}"

def number_in_range(x,y,z):
    if z in range(x,y+1):
        return True
    else:
        return False
    
def credit_card(card_number):
    card_number2 = card_number[0:2]+"************"+card_number[-2:]
    return card_number2

