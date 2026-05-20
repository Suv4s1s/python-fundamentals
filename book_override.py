class Book:
    def __init__(self, author,title):
        self.author = author
        self.title= title
    
    def book_info(self):
        print(f"{self.title} is authorized by {self.author}")

class Fiction(Book):
    def __init__(self, author, title, publisher):
        super().__init__(author, titles)
        self.publisher = publisher
    
    def book_info(self):
        print(f"{self.title} is authored by {self.author} ")

    def invoke(self):
        super().book_info()

def main():
    print("Derived Class")
    silver_book = Fiction("Daniel silver", "prince of fire")
    silver_book.book_info()
    silver_book.invoke()

    print("-"*20)

    print("Base class")
    reacher_book = Book("Lee Child", "One Shot")
    reacher_book.book_info()

if __name__ == "__main__":
    main()