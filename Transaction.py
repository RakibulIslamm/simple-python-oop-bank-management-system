from datetime import datetime

class Transaction:
    def __init__(self, name, account_no, type, amount) -> None:
        self.customar_name = name
        self.account_no = account_no
        self.type = type
        self.amount = amount
        self.date = datetime.now()

    def __repr__(self) -> str:
        return f"Account No:{self.account_no}, Type: {self.type}, Amount: {self.amount} Date: {self.date.strftime('%m/%d/%y %H:%M')}"