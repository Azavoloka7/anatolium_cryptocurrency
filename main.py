from blockchain.blockchain import Blockchain
from node.node import Node
from wallet.wallet import Wallet
import logging

# Importing hash_utils module
from utils.hash_utils import hash_block, generate_proof_of_work

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def initialize_blockchain():
    """
    Initialize a new blockchain.
    """
    try:
        blockchain = Blockchain()
        return blockchain
    except Exception as e:
        logger.error("Error occurred while initializing blockchain: %s", str(e))

def create_wallets():
    """
    Create sender and recipient wallets.
    """
    try:
        sender_wallet = Wallet()
        recipient_wallet = Wallet()
        return sender_wallet, recipient_wallet
    except Exception as e:
        logger.error("Error occurred while creating wallets: %s", str(e))

def create_nodes(blockchain):
    """
    Create nodes and assign them the provided blockchain.
    """
    try:
        node1 = Node(blockchain)
        node2 = Node(blockchain)
        return node1, node2
    except Exception as e:
        logger.error("Error occurred while creating nodes: %s", str(e))

def mine_blocks(node1, node2):
    """
    Mine blocks on nodes.
    """
    try:
        node1.mine()
        node2.mine()
    except Exception as e:
        logger.error("Error occurred while mining blocks: %s", str(e))

def print_blockchain(blockchain):
    """
    Print the current blockchain.
    """
    try:
        print("Blockchain:")
        for block in blockchain.chain:
            print(block)
    except Exception as e:
        logger.error("Error occurred while printing blockchain: %s", str(e))

def create_new_transaction(blockchain, sender_wallet, recipient_wallet, amount):
    """
    Create a new transaction and save it to sender's and recipient's wallets.
    """
    try:
        transaction_data = {
            'sender': sender_wallet.generate_address(),
            'recipient': recipient_wallet.generate_address(),
            'amount': amount
        }
        blockchain.new_transaction(**transaction_data)

        if blockchain.current_transactions:
            sender_wallet.save_transaction(blockchain.current_transactions[-1])
            recipient_wallet.save_transaction(blockchain.current_transactions[-1])
        else:
            print("No transactions found in the current block.")
    except Exception as e:
        logger.error("Error occurred while creating new transaction: %s", str(e))

def display_transaction_history(wallet, wallet_type):
    """
    Display transaction history for a wallet.
    """
    try:
        print(f"\n{wallet_type} Wallet Transaction History:")
        wallet.display_transaction_history()
    except Exception as e:
        logger.error("Error occurred while displaying transaction history: %s", str(e))

def resolve_conflicts(node):
    """
    Resolve conflicts on a node.
    """
    try:
        node.resolve_conflicts()
    except Exception as e:
        logger.error("Error occurred while resolving conflicts: %s", str(e))

if __name__ == "__main__":
    blockchain = initialize_blockchain()
    sender_wallet, recipient_wallet = create_wallets()
    node1, node2 = create_nodes(blockchain)

    mine_blocks(node1, node2)
    print_blockchain(blockchain)

    create_new_transaction(blockchain, sender_wallet, recipient_wallet, 100)

    display_transaction_history(sender_wallet, "Sender")
    display_transaction_history(recipient_wallet, "Recipient")

    # Placeholder for resolving conflicts
    resolve_conflicts(node1)

    print("\nUpdated Blockchain:")
    print_blockchain(blockchain)
