#Creating a library system (i'll be dividing the same into functions)
library_db = [] #a list containing each element in the library

def add_book():
    isbn = input("Enter the ISBN code: ")
    #put it inside the for loop to check whether the ISBN code firstly already exists in the
    for book in library_db:
        if (book["ISBN"] == isbn):
            print("The book with the ISBN already exists. ")
            return
        
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book : ")
    price = input("Enter the price of the book: ")
    genre = input("Enter the genre of the book: ")


        #now to declare the values according to the keys
    book = {
            "ISBN" : isbn,
            "Title" : title, 
            "Author" : author, 
            "Price" : price, 
            "Genre" : genre
    }

    library_db.append(book)
    print("Your book is added sucessfully!")
    print()

def display_books():
    print("The book details are as follows. ")
    print()
    if not library_db:
        print("Your library is empty..")
    else: 
        for book in library_db:
            print("ISBN: ", book["ISBN"])
            print("Title: ", book["Title"])
            print("Author: ",book["Author"])
            print("Price: ", book["Price"])
            print("Genre: ",book["Genre"])
            print()


def isbnsearch():
    isbn = input("Enter the ISBN number of the book you want to search: ")
    for book in library_db: 
        if book["ISBN"] == isbn: 
            print ("The book is found!")
            print("ISBN: ", book["ISBN"])
            print("Title: ", book["Title"])
            print("Author: ",book["Author"])
            print("Price: ", book["Price"])
            print("Genre: ",book["Genre"])
            print()
        else: 
            print("Your book is not found..")
            print()

def genresearch():
    genre = input("Enter the genre you are searching for: ")
    foundbooks = []
    for book in library_db:
        if book["Genre"] == genre:
             foundbooks.append(book)
    if not foundbooks: 
        print("No books are found gor the genre ",'"',genre,'"')   
        print()
    else: 
        for book in foundbooks:
                print("ISBN: ", book["ISBN"])
                print("Title: ", book["Title"])
                print("Author: ",book["Author"])
                print("Price: ", book["Price"])
                print("Genre: ",book["Genre"])
                print()
       
while True: 
    print("CHOOSE ONE OF THE OPTIONS GIVEN BELOW: ")
    print("1. Add a new book")
    print("2. Display all books")
    print("3. Search books by ISBN")
    print("4. Search books by genre")
    print("5. Exit")
    print()

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        add_book()
    elif choice == 2: 
        display_books()
    elif choice == 3: 
        isbnsearch()
    elif choice == 4: 
        genresearch()
    elif choice == 5: 
        print("Thank you for visitinG, SEE YOU AGAIN!")
        break

    else: 
        ("Error!!")