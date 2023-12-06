class Phone():
    def __init__(self,model,aparat,załadowany):
        self.model = model
        self.aparat = aparat
        self.załadowany = załadowany
        self.działanie = False
    def załącz(self):
        if self.działanie:
            print("Telefon już jest włączony")
        else:
            print("Załączam")
    def wyłącz(self):
        if self.działanie:
            print("Wyłączam")
        else:
            print("Telefon już jest wyłączony")
    def zadzwoń(self,osoba):
        print(f"Dzwonię do {osoba}")

telefon = Phone("Samsung A20e",True,True,)
print(telefon.model)
print(telefon.aparat)
print(telefon.załadowany)
telefon.załącz()
telefon.wyłącz()
telefon.zadzwoń("Doktor")