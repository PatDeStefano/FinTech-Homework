import subprocess
import json
import os
from dotenv import load_dotenv
from pathlib import Path

from constants import *
from web3 import Web3
from eth_account import Account

from web3.middleware import geth_poa_middleware
from bit import PrivateKeyTestnet
from bit.network import NetworkAPI

mnemonic = os.getenv('MNEMONIC', 'lunch quantum worth heavy measure ramp label ring auction jelly warm laugh')

coins_in_wallet = {BTC, ETH, BTCTEST}

def derive_wallets(mnemonic, coin, numderive):
    command = './derive -g --mnemonic="' + mnemonic + '" --cols=path,address,privkey,pubkey --coin="' + coin + '" --numderive="' + str(numderive) + '" --format=json'

    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()

    keys = json.loads(output)
    return keys

def coins():
    coin_dict = {}
    for i in coins_in_wallet:
        coin_dict[i] = derive_wallets(mnemonic, i, 3)
        
    return coin_dict

def priv_key_to_account(coin, priv_key):
    if coin == ETH:
        private_key = Account.privateKeyToAccount(priv_key)
    elif coin == BTCTEST:
        private_key = PrivateKeyTestnet(priv_key)
    return private_key

def create_tx(coin, account, to, amount):
    if coin=='eth':
        gasEstimate = w3.eth.estimateGas({"from": account.address, "to": to, "value": amount})
        return { "from": account.address,"to": to,"value": amount,"gas": gasEstimate, "gasPrice": w3.eth.gasPrice,"nonce": w3.eth.getTransactionCount(account.address)}
    elif coin=='btc-test':
        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])

def send_tx(coin, account, to, amount):
    tx = create_tx(coin, account, to, amount)
    signed_tx = account.sign_transaction(tx)
    if coin=='eth':
        result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return result.hex()
    elif coin=='btc-test':
        return NetworkAPI.broadcast_tx_testnet(signed_tx) 