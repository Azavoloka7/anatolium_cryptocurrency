from wallet.wallet import Wallet

class TransactionBuilder:
    def __init__(self):
        self.wallet = Wallet()

    def build_transaction(self, recipient, amount):
        sender = self.wallet.generate_address()
        return {
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        }
