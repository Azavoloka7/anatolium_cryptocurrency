import rsa
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Wallet:
    def __init__(self):
        try:
            # Generate public and private keys
            self.public_key, self.private_key = rsa.newkeys(512)
            self.transaction_history = []
        except Exception as e:
            logger.error("Error occurred while initializing the wallet: %s", str(e))

    def save_transaction(self, transaction):
        """
        Save a transaction to the wallet's transaction history
        """
        try:
            self.transaction_history.append(transaction)
        except Exception as e:
            logger.error("Error occurred while saving transaction to wallet's history: %s", str(e))

    def get_transaction_history(self):
        """
        Get the transaction history of the wallet
        """
        try:
            return self.transaction_history
        except Exception as e:
            logger.error("Error occurred while getting wallet's transaction history: %s", str(e))

    def display_transaction_history(self):
        """
        Display the transaction history of the wallet
        """
        try:
            for transaction in self.transaction_history:
                print(transaction)
        except Exception as e:
            logger.error("Error occurred while displaying wallet's transaction history: %s", str(e))

    def generate_address(self):
        """
        Generate an address from the public key
        """
        try:
            return rsa.PublicKey(self.public_key.n, self.public_key.e)
        except Exception as e:
            logger.error("Error occurred while generating address from public key: %s", str(e))
