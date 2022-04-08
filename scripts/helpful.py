from brownie import accounts, config ,network, MockV3Aggregator
import time


DECIMALS =8
STARTING_PRICE=200000000000

FORKED_LOCAL_ENVIRONMENT =["mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS =["development", "ganache-local"]

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENT:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    print(f"active network is {network.show_active()}")
    if(len(MockV3Aggregator)<=0):
           print ("Deploying Mocks...")
           MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE ,{"from": get_account()})
           time.sleep(1)
           print("mocks deployed")