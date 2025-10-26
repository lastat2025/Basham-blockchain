# Minimal blockchain core for Basham-blockchain
# Simple proof-of-work, transaction pool, basic validation

import hashlib
import json
import time
from typing import List, Dict, Any
from urllib.parse import urlparse
import requests

class Blockchain:
    def __init__(self):
        self.chain: List[Dict[str, Any]] = []
        self.current_transactions: List[Dict[str, Any]] = []
        self.nodes = set()
        # Create genesis block
        self.new_block(previous_hash='1', proof=100)

    def register_node(self, address: str):
        parsed = urlparse(address)
        if parsed.netloc:
            self.nodes.add(parsed.netloc)
        elif parsed.path:
            # Accept without scheme
            self.nodes.add(parsed.path)

    def valid_chain(self, chain: List[Dict[str, Any]]) -> bool:
        last_block = chain[0]
        current_index = 1
        while current_index < len(chain):
            block = chain[current_index]
            # Check that the hash of the block is correct
            if block['previous_hash'] != self.hash(last_block):
                return False
            # Check that the proof of work is correct
            if not self.valid_proof(last_block['proof'], block['proof'], self.hash(last_block)):
                return False
            last_block = block
            current_index += 1
        return True

    def resolve_conflicts(self) -> bool:
        neighbours = self.nodes
        new_chain = None
        max_length = len(self.chain)
        for node in neighbours:
            try:
                response = requests.get(f'http://{node}/chain', timeout=3)
                if response.status_code == 200:
                    length = response.json()['length']
                    chain = response.json()['chain']
                    if length > max_length and self.valid_chain(chain):
                        max_length = length
                        new_chain = chain
            except requests.RequestException:
                continue
        if new_chain:
            self.chain = new_chain
            return True
        return False

    def new_block(self, proof: int, previous_hash: str = None) -> Dict[str, Any]:
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender: str, recipient: str, amount: float, signature: str = None) -> int:
        tx = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
            'signature': signature
        }
        self.current_transactions.append(tx)
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block: Dict[str, Any]) -> str:
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self) -> Dict[str, Any]:
        return self.chain[-1]

    def proof_of_work(self, last_proof: int) -> int:
        proof = 0
        last_hash = self.hash(self.last_block)
        while not self.valid_proof(last_proof, proof, last_hash):
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof: int, proof: int, last_hash: str) -> bool:
        guess = f'{last_proof}{proof}{last_hash}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        # Difficulty: leading 4 zeros (adjust as desired)
        return guess_hash[:4] == "0000"