class book:
    def __init__(self, title):
        self.title = title

class library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append(book(title))          
        print("book been placed") 

    def show(self):
        if len(self.books) == 0:
            print("no book left")

        else:
            print("there are books left")
            for book in self.books:
                print(book.title)

library = library()

while True:
    print("\n1. add book")
    print("2. show book")
    print("2. exit")

    choice = input("enter ur choices :")

    if choice == "1":
        title = input("enter book title")
        library.add_book(title)
        

