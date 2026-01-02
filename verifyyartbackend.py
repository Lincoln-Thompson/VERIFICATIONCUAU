from web3 import Web3
from cryptography.fernet import Fernet
import sys
import time
def decrypt(key):
    key=key.encode('utf-8')
    with open(r'C:\Users\lbolt\OneDrive\Desktop\STABLECu\ECONOMICS\docfororacle.txt','rb') as doc:
        encrypted_message=doc.read()

    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message

w3 = Web3(Web3.HTTPProvider('https://ethereum-sepolia-rpc.publicnode.com'))
pkey=decrypt(input('Enter key to start program:'))
account = w3.eth.account.from_key(pkey)
senderaddress=account.address

abi=[{"type":"event","name":"TagCreated","inputs":[{"name":"manu_id","type":"uint256","components":None,"internalType":None,"indexed":False},{"name":"product","type":"string","components":None,"internalType":None,"indexed":False}],"anonymous":False},{"type":"event","name":"TagVerified","inputs":[{"name":"tag_id","type":"bytes32","components":None,"internalType":None,"indexed":True},{"name":"scanner","type":"address","components":None,"internalType":None,"indexed":True}],"anonymous":False},{"type":"function","name":"createTag","stateMutability":"nonpayable","inputs":[{"name":"tag_id","type":"bytes32","components":None,"internalType":None},{"name":"manu_id","type":"uint256","components":None,"internalType":None},{"name":"product","type":"string","components":None,"internalType":None}],"outputs":[]},{"type":"function","name":"verify","stateMutability":"nonpayable","inputs":[{"name":"tag_id","type":"bytes32","components":None,"internalType":None}],"outputs":[{"name":"","type":"bool","components":None,"internalType":None}]},{"type":"function","name":"getTag","stateMutability":"view","inputs":[{"name":"tag_id","type":"bytes32","components":None,"internalType":None}],"outputs":[{"name":"","type":"uint256","components":None,"internalType":None},{"name":"","type":"string","components":None,"internalType":None},{"name":"","type":"bool","components":None,"internalType":None},{"name":"","type":"bool","components":None,"internalType":None}]},{"type":"function","name":"name","stateMutability":"view","inputs":[],"outputs":[{"name":"","type":"string","components":None,"internalType":None}]},{"type":"function","name":"symbol","stateMutability":"view","inputs":[],"outputs":[{"name":"","type":"string","components":None,"internalType":None}]},{"type":"function","name":"owner","stateMutability":"view","inputs":[],"outputs":[{"name":"","type":"address","components":None,"internalType":None}]},{"type":"constructor","stateMutability":"nonpayable","inputs":[{"name":"_name","type":"string","components":None,"internalType":None},{"name":"_symbol","type":"string","components":None,"internalType":None}]}]


tokencontract = w3.eth.contract(address='0x495553f755Ba61E0f4D2Ca5623befFE0dd06054d', abi=abi)



def verifytag(stringtobeverified):
   
    b32 = Web3.to_bytes(text=stringtobeverified).ljust(32, b'\0')
    print(b32)
    result0=tokencontract.functions.getTag(b32).call()
    txn = tokencontract.functions.verify(b32).build_transaction({
    'from': senderaddress,
    'nonce': w3.eth.get_transaction_count(senderaddress),
    'gas': 200000,  # adjust if needed
    #'gasPrice': w3.to_wei('1.5', 'gwei'),  # adjust for network
    "maxFeePerGas": w3.to_wei(200, "gwei"),         
    "maxPriorityFeePerGas": w3.to_wei(10, "gwei"),
    'chainId': 11155111,  # ← IMPORTANT: match your network (e.g., 1=ETH, 8453=Base)
    })
    signed_txn = w3.eth.account.sign_transaction(txn, private_key=pkey)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)  # ← snake_case!
    print("Transaction sent! Hash:", w3.to_hex(tx_hash))
    time.sleep(15)
    result=tokencontract.functions.getTag(b32).call()
    result.append(result0)
    return result
