# Import dependencies
import subprocess
import json
import os
from dotenv import load_dotenv
from eth_account import Account

# Load and set environment variables
load_dotenv("mnemonic.env")
mnemonic=os.getenv("mnemonic")

# Import constants.py and necessary functions from bit and web3
from constants import *
 
 
# Create a function called `derive_wallets`
def derive_wallets (mnemonic, coin, numderive): # YOUR CODE HERE
    command = f'php hd-wallet-derive/hd-wallet-derive.php -g --mnemonic="{mnemonic}" --cols=path,address,privkey,pubkey --coin={coin} --numderive={numderive} --format=json'
    p = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    return json.loads(output)

# Create a dictionary object called coins to store the output from `derive_wallets`.
coins = {ETH:derive_wallets (mnemonic, ETH, 3),
        BTCTEST:derive_wallets (mnemonic, BTCTEST, 3)}

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account(coin,priv_key):
    if coin == ETH: 
        return Account.privateKeyToAccount(priv_key)
    if coin == BTCTEST:
         return PrivateKeyTestnet(priv_key)
        
# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx(# YOUR CODE HERE):
    # YOUR CODE HERE

# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx(# YOUR CODE HERE):
    # YOUR CODE HERE

