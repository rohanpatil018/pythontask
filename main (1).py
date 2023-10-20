# keys=input("enter keys seperated by space: ").split()
# num_lists=int(input("enter the number of values lists: "))
# result_dict={}
# for i in range(num_lists):
#     values=input(f"enter values sepearted by space for {keys[1]}: ").split()
#     result_dict[keys[i]]=values
# print("/ncreated dictionary:")
# print(result_dict)





book_dict = {}

# Function to add a book
def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    year = input("Enter the publication year: ")
    genre = input("Enter the genre: ")
    book_dict[title] = {'Author': author, 'Year': year, 'Genre': genre}
    print(f"Book '{title}' added successfully!")

# Function to search for a book
def search_book():
    title = input("Enter the book title to search: ")
    if title in book_dict:
        print(f"Book details for '{title}':")
        book_info = book_dict[title]
        for key, value in book_info.items():
            print(f"{key}: {value}")
    else:
        print(f"Book '{title}' not found in the dictionary.")

# Function to display all books
def display_books():
    if book_dict:
        print("List of all books in the dictionary:")
        for title, book_info in book_dict.items():
            print(f"Title: {title}")
            for key, value in book_info.items():
                print(f"{key}: {value}")
            print()
    else:
        print("The dictionary is empty. No books to display.")

# Function to delete a book
def delete_book():
    title = input("Enter the book title to delete: ")
    if title in book_dict:
        del book_dict[title]
        print(f"Book '{title}' has been deleted.")
    else:
        print(f"Book '{title}' not found in the dictionary.")

# Function to update book details
def update_book():
    title = input("Enter the book title to update: ")
    if title in book_dict:
        author = input("Enter the new author's name: ")
        year = input("Enter the new publication year: ")
        genre = input("Enter the new genre: ")
        book_dict[title] = {'Author': author, 'Year': year, 'Genre': genre}
        print(f"Book '{title}' updated successfully!")
    else:
        print(f"Book '{title}' not found in the dictionary.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Display All Books")
    print("4. Delete Book")
    print("5. Update Book")
    print("6. Exit")
    choice = input("Enter your choice (1/2/3/4/5/6): ")
    
    if choice == '1':
        add_book()
    elif choice == '2':
        search_book()
    elif choice == '3':
        display_books()
    elif choice == '4':
        delete_book()
    elif choice == '5':
        update_book()
    elif choice == '6':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice")