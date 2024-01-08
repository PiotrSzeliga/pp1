class eBook():
    def __init__(self,title,author,pages_number,current_page):
        self.title = title
        self.author = author
        self.pages_number = pages_number
        self.current_page = current_page
        self.opening = False

    def status(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nNumber of pages: {self.pages_number}\nCurrent page: {self.current_page}\n{self.opening}")
    
    def open(self):
        if self.opening == False:
            self.opening = True
        else:
            pass
    
    def close(self):
        if self.opening == True:
            self.opening = False
        else:
            pass

    def next_page(self):
        if self.opening == True:
            if self.current_page < self.pages_number:
                self.current_page += 1
            else:
                pass
        else:
            pass
    def previous_page(self):
        if self.opening == True:
            if self.current_page > 1:
                self.current_page -= 1
            else:
                pass
        else:
            pass
