# Simple wallet utilities: key generation, sign, verify (ECDSA)
from ecdsa import SigningKey, VerifyingKey, SECP256k1, BadSignatureError
import binascii
import json
import hashlib

def generate_private_key_hex() -> str:
    sk = SigningKey.generate(curve=SECP256k1)
    return binascii.hexlify(sk.to_string()).decode()

def private_key_to_public_key_hex(privkey_hex: str) -> str:
    sk = SigningKey.from_string(binascii.unhexlify(privkey_hex), curve=SECP256k1)
    vk = sk.verifying_key
    return binascii.hexlify(vk.to_string()).decode()

def sign_transaction(privkey_hex: str, transaction: dict) -> str:
    # transaction should be a dict containing sender, recipient, amount
    tx_copy = transaction.copy()
    tx_copy.pop('signature', None)
    message = json.dumps(tx_copy, sort_keys=True).encode()
    sk = SigningKey.from_string(binascii.unhexlify(privkey_hex), curve=SECP256k1)
    signature = sk.sign(message)
    return binascii.hexlify(signature).decode()

def verify_transaction_signature(pubkey_hex: str, signature_hex: str, transaction: dict) -> bool:
    tx_copy = transaction.copy()
    tx_copy.pop('signature', None)
    message = json.dumps(tx_copy, sort_keys=True).encode()
    try:
        vk = VerifyingKey.from_string(binascii.unhexlify(pubkey_hex), curve=SECP256k1)
        vk.verify(binascii.unhexlify(signature_hex), message)
        return True
    except (binascii.Error, BadSignatureError, Exception):
        return False
