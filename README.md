# Basham-blockchain (Minimal Operational Chain)

This repository contains a minimal operational blockchain implementation (Python + Flask).
It supports:
- creating accounts (ECDSA keys)
- creating and signing transactions
- basic proof-of-work mining
- running multiple nodes and resolving forks by consensus

Files:
- blockchain.py - core chain logic
- node.py - Flask HTTP API for a node
- wallet.py - simple key/sign/verify helpers
- requirements.txt - Python deps

Quick start (local):

1. Create a Python virtualenv and install dependencies:
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

2. Start a node:
   PORT=5000 python node.py

3. Start more nodes (in separate shells):
   PORT=5001 python node.py
   PORT=5002 python node.py

4. Register nodes with each other:
   curl -X POST -H "Content-Type: application/json" -d '{"nodes":["http://127.0.0.1:5001","http://127.0.0.1:5002"]}' http://127.0.0.1:5000/nodes/register

5. Create wallets/keys (example python snippet):
   from wallet import generate_private_key_hex, private_key_to_public_key_hex
   priv = generate_private_key_hex()
   pub = private_key_to_public_key_hex(priv)

6. Create and sign a transaction:
   tx = {"sender": "<pubkey>", "recipient": "<recipient_pubkey>", "amount": 1}
   signature = sign_transaction(priv, tx)
   tx['signature'] = signature
   curl -X POST -H "Content-Type: application/json" -d '{"sender":"<pubkey>","recipient":"<recipient_pubkey>","amount":1,"signature":"<signature>"}' http://127.0.0.1:5000/transactions/new

7. Mine a block:
   curl http://127.0.0.1:5000/mine

8. Check chain:
   curl http://127.0.0.1:5000/chain

Docker (optional):
- There is a Dockerfile and docker-compose.yml (provided) to run multiple nodes locally.
- Build images and bring up the compose stack:
  docker-compose up --build

Security and improvements:
- This is a learning/minimal implementation. For production:
  - Use TLS on endpoints.
  - Harden and persist data (use a DB).
  - Add transaction replay protection, nonces, fee model, and account-balance checks.
  - Improve consensus (PoS, PBFT) or layer 2, and implement persistent peer discovery.
