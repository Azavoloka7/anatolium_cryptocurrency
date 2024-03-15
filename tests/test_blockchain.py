import unittest
from blockchain.blockchain import Blockchain

class TestBlockchain(unittest.TestCase):
    def test_new_block(self):
        blockchain = Blockchain()
        self.assertEqual(len(blockchain.chain), 1)
        blockchain.new_block(100, '1')
        self.assertEqual(len(blockchain.chain), 2)

    def test_new_transaction(self):
        blockchain = Blockchain()
        blockchain.new_transaction("sender", "recipient", 10)
        self.assertEqual(len(blockchain.current_transactions), 1)

    def test_hash(self):
        blockchain = Blockchain()
        block = blockchain.last_block
        self.assertEqual(blockchain.hash(block), blockchain.hash(block))


