from brownie import FundMe, accounts
from scripts.helpful import get_account, deploy_mocks,LOCAL_BLOCKCHAIN_ENVIRONMENTS

def fund():
    fund_me_obj=FundMe[-1]
    account= get_account()
    entrance_fee= fund_me_obj.getEntranceFee()
    print(entrance_fee)
    fund_me_obj.fund({"from":account,"value":entrance_fee})

def withdraw():
    fund_me_obj=FundMe[-1]
    account= get_account()
    fund_me_obj.withdraw({"from": account})


def main():
    fund()

