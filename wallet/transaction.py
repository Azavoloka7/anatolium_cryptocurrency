class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def __str__(self):
        return f"Transaction(sender={self.sender}, recipient={self.recipient}, amount={self.amount})"
