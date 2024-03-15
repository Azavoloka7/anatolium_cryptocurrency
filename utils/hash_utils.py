import hashlib
import json

def hash_string_256(string):
    """
    Hashes a string using SHA-256 algorithm.
    
    Args:
    - string: The string to be hashed.
    
    Returns:
    - The hashed string in hexadecimal format.
    """
    return hashlib.sha256(string).hexdigest()

def hash_block(block):
    """
    Hashes a block using SHA-256 algorithm.
    
    Args:
    - block: The block to be hashed.
    
    Returns:
    - The hashed block in hexadecimal format.
    """
    # Convert the block to a JSON string to ensure consistency
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()

def generate_proof_of_work(previous_proof):
    """
    Simple proof of work algorithm:
    - Find a number p' such that hash(pp') contains 4 leading zeroes, where p is the previous proof
    - p is the previous proof, and p' is the new proof
    
    Args:
    - previous_proof: The previous proof
    
    Returns:
    - The new proof that satisfies the criteria
    """
    new_proof = 1
    while not is_valid_proof(previous_proof, new_proof):
        new_proof += 1
    return new_proof

def is_valid_proof(previous_proof, proof):
    """
    Validates the proof of work.
    
    Args:
    - previous_proof: The previous proof
    - proof: The current proof to be validated
    
    Returns:
    - True if the proof is valid, False otherwise
    """
    guess = f'{previous_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:4] == "0000"
