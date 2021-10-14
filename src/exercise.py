from src.book import Book

def main():
    #write your code below this line
    books = []
    while True:
        title = input("Title:")
        if not title:
            break
        pages = input("Pages:")
        year = input("Publication Year:")
        input_book = Book(title, pages, year)
        books.append(input_book)
    
    print_query = input("What information will be printed?")
    if (print_query == "everything"):
        for i in books:
            print(i)
    elif (print_query == "name"):
        for j in books:
            print(j.get_title())

if __name__ == '__main__':
    main()
