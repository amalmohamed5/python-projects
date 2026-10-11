
class Book():
    def __init__(self,title,author,price,is_borrowed):
        self.title=title.strip().lower()
        self.author=author
        self.price=price
        self.is_borrowed=is_borrowed
    def __str__(self):
        return (f"Title: {self.title} , Author: {self.author} , Borrowed: {'yes' if self.is_borrowed else ' No'} ")
    def borrow_book(self):
        if self.is_borrowed==False :
            self.is_borrowed=True
            print("book is borrowed succesfully")
        else:
            print("Book has already been borrowed")
    def return_book(self):
        if self.is_borrowed==True:
            self.is_borrowed=False
            print("book has been returned")
        else:
            print("the book is avaliable on libirary")
class Library():
    def __init__(self):
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
        print("Book added succesfully")
    def show_books(self):
        if not self.books :
            print("No books in library")
            return
    
        for book in self.books:
                 print(book) 
    def search_books(self,title):
       
        if not self.books :
             print("No books in library")
             return
        for book in self.books:
            if( title==book.title):
                print(f"book {title} is found")
                break
        else :
                print("book not found")
    def borrow_book(self, title):
         for book in self.books:
              if( title==book.title):
                   book.borrow_book()
                   break
         else:
              print("book not found")
    def return_book(self,title):
          for book in self.books:
             if( title==book.title):
                  book.return_book()
                  break
          else:
               print("book not found")
    def remove_book(self,title):
         if not self.books :
              print("No books in library")
              return
         for book in self.books:
              if( title==book.title):
                 self.books.remove(book)
                 print("Book removed")
                 break
         else:
           print("book not found")
         
         


library=Library()

def main_menu():
     print("=====Library-System=====")
     print("1-Add Book")
     print("2-show books")
     print("3-search book")
     print("4-borrow book")
     print("5-return book")
     print("6-remove book")
     print("7-Exit")
while True:
     main_menu()
     choice=input('choose an option (1-7) : ')
     if choice=='1':
        title=input("enter book title: ").strip().lower()
        author=input("enter book author: ")
        try:
          price=int(input("enter book price : "))
          book=Book(title,author,price,is_borrowed=False)
          library.add_book(book)
        except ValueError:
          print("Enter a valid integer number!")
         
     elif choice=='2':
          library.show_books()
     elif choice=='3':
          title=input("Enter book title : ").strip().lower()
          library.search_books(title)
     elif choice=='4':
          title=input("Enter book title : ").strip().lower()
          library.borrow_book(title)
     elif choice=='5':  
        title=input("Enter book title : ").strip().lower()
        library.return_book(title)
     elif choice=='6':
          title=input("Enter book title : ").strip().lower()
          library.remove_book(title)
     elif choice=='7':
        print("FINISHED")
        break
     else:
          print("Enter valid number !")
