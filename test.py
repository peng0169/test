import web3

# Define your node URL (in this case, it should be http://localhost:8545)

w3 = web3.Web3(web3.HTTPProvider('http://localhost:8545'))

from web3 import Web3
import json

# Load ABI from file (assuming it is named 'YourContract.json')
with open('YourContract.json') as f:
    abi = json.load(f)

# Define the address of deployed smart contract on Ganache network.
contract_address = "0x7EF2e0048f5bAeDe046f6BF797943daF4ED8CB47"

your_contract = w3.eth.contract(address=Web3.to_checksum_address(contract_address), abi=abi)

# Call a function on the smart contract
tx_hash = your_contract.functions.mint('0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2', 1).transact()

print(tx_hash)