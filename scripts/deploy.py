from scripts.helpful import get_account, deploy_mocks,LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import FundMe, network ,config, MockV3Aggregator
import time


def deploy_fundme() :
    account= get_account()
    if network.show_active() not in  LOCAL_BLOCKCHAIN_ENVIRONMENTS :
        price_feed_address =config["networks"][network.show_active()]["eth_usd_price_feed"]
    else :
        deploy_mocks()
        price_feed_address=MockV3Aggregator[-1].address
        
         
    fundme_obj=FundMe.deploy(price_feed_address,{"from": account},publish_source=config["networks"][network.show_active()].get("verify"))
    time.sleep(1)
    return fundme_obj

def main():
    deploy_fundme()
    
