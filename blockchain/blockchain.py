import hashlib
import json
import logging
from time import time

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # Create the genesis block
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        Create a new block in the blockchain
        """
        try:
            block = {
                'index': len(self.chain) + 1,
                'timestamp': time(),
                'transactions': self.current_transactions,
                'proof': proof,
                'previous_hash': previous_hash or self.hash(self.chain[-1]),
            }

            # Reset the current list of transactions
            self.current_transactions = []

            self.chain.append(block)
            return block
        except Exception as e:
            logger.error("Error occurred while creating a new block: %s", str(e))

    def new_transaction(self, sender, recipient, amount):
        """
        Create a new transaction to go into the next mined block
        """
        try:
            self.current_transactions.append({
                'sender': sender,
                'recipient': recipient,
                'amount': amount,
            })

            return self.last_block['index'] + 1
        except Exception as e:
            logger.error("Error occurred while creating a new transaction: %s", str(e))

    @property
    def last_block(self):
        """
        Returns the last block in the blockchain
        """
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """
        Create a SHA-256 hash of a block
        """
        try:
            # We must make sure that the dictionary is ordered, or we'll have inconsistent hashes
            block_string = json.dumps(block, sort_keys=True).encode()
            return hashlib.sha256(block_string).hexdigest()
        except Exception as e:
            logger.error("Error occurred while hashing block: %s", str(e))

    def proof_of_work(self, last_proof):
        """
        Simple Proof of Work Algorithm:
         - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
         - p is the previous proof, and p' is the new proof
        """
        try:
            proof = 0
            while self.valid_proof(last_proof, proof) is False:
                proof += 1

            return proof
        except Exception as e:
            logger.error("Error occurred while performing proof of work: %s", str(e))

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?
        """
        try:
            guess = f'{last_proof}{proof}'.encode()
            guess_hash = hashlib.sha256(guess).hexdigest()
            return guess_hash[:4] == "0000"
        except Exception as e:
            logger.error("Error occurred while validating proof: %s", str(e))
