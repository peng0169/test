import web3

# Define your node URL (in this case, it should be http://localhost:8545)

w3 = web3.Web3(web3.HTTPProvider('http://localhost:8545'))
print(w3.is_connected())

from web3 import Web3
import json

with open('/workspaces/test/my-smart-contract/artifacts/contracts/InvestmentToken.sol/InvestmentToken.json') as f:
    contract_data = json.load(f)
    abi = contract_data['abi']

# Define the address of deployed smart contract on Ganache network.
contract_address = "0x869c8a80b23d76374b8Fb3124a6a08BBCd108dCe"

your_contract = w3.eth.contract(address=Web3.to_checksum_address(contract_address), abi=abi)

# Call a function on the smart contract
tx_hash = your_contract.functions.mint('0x34828fF737EfA8DfF93ce6011eAacdd417FE014a', 1).transact()

print(tx_hash)