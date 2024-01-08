import book

book1 = book.eBook("Titleous","Tony Hawk",432,123)
book1.open()
book1.status()
for i in range(20):
    book1.next_page()
book1.status()
book1.previous_page()
book1.status()
book1.close()
book1.next_page()
book1.status()