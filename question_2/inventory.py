import json
import math
from books import Book

BOOKS_FILE = "books.json"

def load_goods():
    try:
        with open(BOOKS_FILE, "r") as f:
            data = json.load(f)
            inventory = []
            for book_data in data:
                book_object = Book.from_dict(book_data)
                inventory.append(book_object)
        return inventory
    except FileNotFoundError:
        return []

def save_goods(inventory):
    with open(BOOKS_FILE, "w") as f:
        book_list = []
        for book in inventory:
            book_dict = book.to_dict()
            book_list.append(book_dict)
        json.dump(book_list, f, indent=2)

def add_book(inventory, title, author, price, stock):
    price = math.ceil(float(price) * 100) / 100
    new_book = Book(title, author, price, stock)
    inventory.append(new_book)
    save_goods(inventory)
    print(f'Added "{title}" by "{author}".')

def list_books(inventory):
    if not inventory:
        print("No bookd in inventory.")
        return
    for item, book in enumerate(inventory, 1):
        print(f"{item}. {book.title} by {book.author} - ${book.price:2f} ({book.stock} in stock)")

def update_stock(inventory, book_index, new_stock):
    if book_index >= 0 and book_index < len(inventory):
        selected_book = inventory[book_index]
        selected_book.stock = int(new_stock)
        save_goods(inventory)

        print("Stock updated.")

    else:
        print("Book not found.")

def remove_book(inventory, book_index):
    if book_index >= 0 and book_index < len(inventory):
        book = inventory.pop(book_index)
        save_goods(inventory)
        print(f'Removed "{book.title}"')
    else:
        print("Book not found.")
