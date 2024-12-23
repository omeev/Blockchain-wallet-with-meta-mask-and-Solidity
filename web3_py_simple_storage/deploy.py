from solcx import compile_standard
import json

#Enter the correct path of SimpleStorage.sol file#
with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
    #print(simple_storage_file)
# Compile our Solidity
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file }},
        "settings": {
            "outputSelection": {
                "*" : { "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    sole_version="0.8.10",
)
with open ("compiled_code.json","w") as file:
    json.dump(compiled_sol, file)
