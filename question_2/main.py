from inventory import (
    load_goods, save_goods, add_book, list_books, update_stock, remove_book
)
inventory = load_goods()

while True:
    print("\n--- Bookstore Inventory ---")
    print("1. List all books")
    print("2. Add new book")
    print("3. Update book stock")
    print("4. Remove a book")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        list_books(inventory)
    elif choice == "2":
        title = input("Title: ")
        author = input("Author: ")
        price = input("Price: ")
        stock = input("Stock: ")
        add_book(inventory, title, author, price, stock)
    elif choice == "3":
        list_books(inventory)
        item = int(input("Book number to update: ")) - 1
        new_stock = input("New stock: ")
        update_stock(inventory, item, new_stock)
    elif choice == "4":
        list_books(inventory)
        item = int(input("Book number to remove: ")) - 1
        remove_book(inventory, item)
    elif choice == "5":
        save_goods(inventory)
        print("Bye!")
        break
    else:
        print("Invalid option.")
