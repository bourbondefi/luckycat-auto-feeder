from web3 import Web3
from time import sleep
import time

class LuckyCatFeeder():
    def __init__(self):
        # Connect to the BSC Web3 provider
        self.web3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))

        with open('luckycat.abi', 'r') as f:
            lucky_abi = f.read()
        lucky_addr = '0xb50e74A6b82F59c4058b5D798E3D9C9D9B8c6e16'
        self.lucky_contract = self.web3.eth.contract(address=lucky_addr, abi=lucky_abi)
    

    def feed_cats(self):
        self.referral_address = '0xdF0833C041db53856380CF1e64CD6428A9e41D3d'
        self.sender_address= 'WALLET ADDRESS HERE'
        self.nonce = self.web3.eth.get_transaction_count(self.sender_address)
        self.feed_cats = self.lucky_contract.functions.hatchEggs(self.referral_address).buildTransaction({'from': self.sender_address,'value': self.web3.toWei(0,'ether'),'gas': 300000, 'gasPrice': self.web3.toWei('5','gwei'),'nonce': self.nonce,})
        self.signed_txn = self.web3.eth.account.sign_transaction(self.feed_cats, private_key='PRIVATE KEY HERE')
        self.tx_token = self.web3.eth.send_raw_transaction(self.signed_txn.rawTransaction)
        del self.feed_cats

if __name__ == "__main__":

    lc = LuckyCatFeeder()


    while(True):

        lc.feed_cats()
        print('Cats Fed')
        sleep(86400)