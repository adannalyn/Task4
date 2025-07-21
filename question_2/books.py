"""
Task 2: Bookstore Inventory System (Using Git Branches)
Goal: Build an app to manage books in a store.
Features:
- Book class: title, author, price, stock
- Use inventory.py for inventory logic
- Save inventory in books.json
- Use math module for rounding prices
- Use Git: Create and merge feature branches
 * git checkout -b feature-search
 * git merge feature-search
 """
class Book:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "price": self.price,
            "stock": self.stock
        }

    @staticmethod
    def from_dict(data):
        return Book (
            data["title"], data["author"], data["price"], data["stock"]
        )
