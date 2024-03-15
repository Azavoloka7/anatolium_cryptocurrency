import logging
import requests

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Node:
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def mine(self):
        """
        Mine a new block
        """
        try:
            last_block = self.blockchain.last_block
            last_proof = last_block['proof']
            proof = self.blockchain.proof_of_work(last_proof)

            # We receive a reward for finding the proof
            self.blockchain.new_transaction(
                sender="0",
                recipient="Anatolii",  # For simplicity, the recipient is the miner
                amount=1,
            )

            # Forge the new block by adding it to the chain
            previous_hash = self.blockchain.hash(last_block)
            block = self.blockchain.new_block(proof, previous_hash)

            return block
        except Exception as e:
            logger.error("Error occurred while mining a block: %s", str(e))

    def register_node(self, address):
        """
        Add a new node to the list of nodes
        """
        try:
            pass  # Placeholder for now
        except Exception as e:
            logger.error("Error occurred while registering a node: %s", str(e))

    def resolve_conflicts(self):
        """
        This is our Consensus Algorithm, it resolves conflicts
        by replacing our chain with the longest one in the network.
        """
        try:
            pass  # Placeholder for now
        except Exception as e:
            logger.error("Error occurred while resolving conflicts: %s", str(e))
