import json
import random
import string
from pathlib import Path

class Bank:

    database = "data.json"
    data = []

    # Load existing data
    if Path(database).exists():
        try:
            with open(database, "r") as f:
                data = json.load(f)
        except:
            data = []

    @classmethod
    def update(cls):
        with open(cls.database, "w") as f:
            json.dump(cls.data, f, indent=4)

    @classmethod
    def generate_account(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        sp = random.choices("!@#$%", k=1)

        acc = alpha + num + sp
        random.shuffle(acc)

        return "".join(acc)

    def create_account(self, name, age, email, pin):

        if age < 18:
            return "Age must be above 18"

        if len(str(pin)) != 4:
            return "Pin must be 4 digits"

        info = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "account_no": Bank.generate_account(),
            "balance": 0
        }

        Bank.data.append(info)
        Bank.update()

        return info

    def find_user(self, account_no, pin):

        for user in Bank.data:
            if user["account_no"] == account_no and user["pin"] == pin:
                return user
        return None

    def deposit(self, account_no, pin, amount):

        user = self.find_user(account_no, pin)

        if not user:
            return "Account not found"

        if amount <= 0:
            return "Invalid amount"

        user["balance"] += amount
        Bank.update()

        return "Deposit successful"

    def withdraw(self, account_no, pin, amount):

        user = self.find_user(account_no, pin)

        if not user:
            return "Account not found"

        if amount > user["balance"]:
            return "Insufficient balance"

        user["balance"] -= amount
        Bank.update()

        return "Withdrawal successful"

    def get_details(self, account_no, pin):

        user = self.find_user(account_no, pin)

        if not user:
            return None

        return user

    def update_details(self, account_no, pin, field, value):

        user = self.find_user(account_no, pin)

        if not user:
            return "Account not found"

        user[field] = value
        Bank.update()

        return "Updated successfully"

    def delete_account(self, account_no, pin):

        user = self.find_user(account_no, pin)

        if not user:
            return "Account not found"

        Bank.data.remove(user)
        Bank.update()

        return "Account deleted"