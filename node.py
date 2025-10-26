# Flask HTTP API for a blockchain node
from flask import Flask, jsonify, request
from uuid import uuid4
from blockchain import Blockchain
from wallet import verify_transaction_signature
import os

app = Flask(__name__)

# Instantiate the Blockchain
blockchain = Blockchain()

# Generate a globally unique address for this node (if not provided)
nod...