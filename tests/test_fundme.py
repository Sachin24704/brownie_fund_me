from scripts.helpful import get_account, deploy_mocks,LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_fundme 
import pytest
from brownie import accounts, network , exceptions



def test_fund_withdraw():
    account=get_account()
    fundme_obj= deploy_fundme()
    entrance_fee=fundme_obj.getEntranceFee()+100
    tx=fundme_obj.fund({"from":account, "value" : entrance_fee})
    tx.wait(1)
    assert fundme_obj.addressToAmountFunded(account) == entrance_fee
    tx2= fundme_obj.withdraw({"from":account})
    tx2.wait(1)
    assert fundme_obj.addressToAmountFunded(account) ==0

def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing")

    fundme_obj=deploy_fundme()
    bad_actor=accounts.add()
    with pytest.raises(AttributeError):
        tx=fundme_obj.withdraw({"from":bad_actor})
        tx.wait(1)
