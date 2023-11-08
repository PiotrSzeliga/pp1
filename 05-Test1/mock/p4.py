def f(card_number):
    masked = card_number[0:2]+10*"*"+card_number[-4:]
    return masked
