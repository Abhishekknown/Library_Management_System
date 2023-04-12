from tkinter import *
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb+srv://abhishekmanjhi21:mnOHVwPlSjSbJcTc@cluster0.dk30bwj.mongodb.net/library_db?retryWrites=true&w=majority")

db = client["library_db"]
books_coll = db["books"]


# Add a book to the database
def add_book():
    title = title_entry.get()
    author = author_entry.get()
    book_num = book_num_entry.get()
    if title and author and book_num:
        books_coll.insert_one({"book_num": book_num, "title": title, "author": author})
        status_label.config(text="Book added successfully.")
        clear_entries()
        show_books()
    else:
        status_label.config(text="Please enter all fields.")


# Delete a book from the database
def delete_book():
    book_num = book_num_entry.get()
    result = books_coll.delete_one({"book_num": book_num})
    if result.deleted_count > 0:
        status_label.config(text="Book deleted successfully.")
        clear_entries()
        show_books()
    else:
        status_label.config(text="Book not found.")


# Clear the entry fields
def clear_entries():
    title_entry.delete(0, END)
    author_entry.delete(0, END)
    book_num_entry.delete(0, END)


# Show all books in the database
def show_books():
    book_list.delete(0, END)
    for book in books_coll.find():
        if 'book_num' in book:
            book_list.insert(END, f"{book['book_num']} - {book['title']} by {book['author']}")


# Create Tkinter window
root = Tk()
root.title("Library Management System")

# Entry fields for adding a new book
book_num_label = Label(root, text="Book Number:")
book_num_label.grid(row=0, column=0, padx=5, pady=5)
book_num_entry = Entry(root)
book_num_entry.grid(row=0, column=1, padx=5, pady=5)

title_label = Label(root, text="Title:")
title_label.grid(row=1, column=0, padx=5, pady=5)
title_entry = Entry(root)
title_entry.grid(row=1, column=1, padx=5, pady=5)

author_label = Label(root, text="Author:")
author_label.grid(row=2, column=0, padx=5, pady=5)
author_entry = Entry(root)
author_entry.grid(row=2, column=1, padx=5, pady=5)

# Buttons to add and delete books
add_button = Button(root, text="Add Book", command=add_book)
add_button.grid(row=3, column=0, padx=5, pady=5)

delete_button = Button(root, text="Delete Book", command=delete_book)
delete_button.grid(row=3, column=1, padx=5, pady=5)

# Listbox to show all books in the database
book_list = Listbox(root)
book_list.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Button to show all books
show_button = Button(root, text="Show Books", command=show_books)
show_button.grid(row=5, column=1, padx=5, pady=5)

# Status label to show success/failure messages
status_label = Label(root, text="Welcome to Library Management System!", bd=1, relief=SUNKEN, anchor=W)
status_label.grid(row=6, column=0, columnspan=2, sticky=W+E, padx=5, pady=5)
root.mainloop()



