import json
import os

from datetime import datetime

class Transaction:
    def __init__(self, category, amount, date=None):
        self.category = category
        self.amount = float(amount)
        self.date = date if date else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    def to_dict(self):
        return {
            "category": self.category,
            "amount": self.amount,
            "date": self.date
        }
    @staticmethod
    def from_dict(data):
        return Transaction(data["category"], data["amount"], data["amount"])

class Budget:
    def __init__(self, filename="transaction.json"):
        self.filename = filename
        self.transactions = self.load_tranactions()

    def load_tranactions(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as f:
            data = json.load(f)
            transactions = []
            for tran in data:
                transaction_object = Transaction.from_dict(tran)
                transactions.append(transaction_object)
            return transactions

    def save_transactions(self):
        with open(self.filename, "w") as f:
            transaction_dicts = [t.to_dict() for t in self.transactions]
            json.dump(transaction_dicts, f, indent=2)

    def add_transaction(self, category, amount, date=None):
        tran = Transaction(category, amount, date)
        self.transactions.append(tran)
        self.save_transactions()

    def list_transactions(self):
        for tran in self.transactions:
            print(f"{tran.date} | {tran.category} | ${tran.amount:2f}")
