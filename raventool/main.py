#!/usr/bin/env python3

import json

import requests

# base config
rpc_user = 'ravenUser'
rpc_pass = 'ravenPassword'
url = 'http://%s:%s@127.0.0.1:8766' % (rpc_user, rpc_pass)


def get_transaction(txid):
    """
    Get transaction by txid
    """

    body = {
        "id": 0,
        "method": "getrawtransaction",
        "params": {'txid': txid, 'verbose': True},
        "jsonrpc": "2.0"
    }

    # make post request
    res = requests.post(url, data=json.dumps(body))
    res.raise_for_status()

    return res.json()


def get_wallet_info():
    """
    Get wallet info
    """

    body = {
        "id": 0,
        "method": "getwalletinfo",
        "jsonrpc": "2.0"
    }

    # make post request
    res = requests.post(url, data=json.dumps(body))
    res.raise_for_status()

    return res.json()


def list_my_assets():
    """
    List my assets
    """

    body = {
        "id": 0,
        "method": "listmyassets",
        "jsonrpc": "2.0"
    }

    # make post request
    res = requests.post(url, data=json.dumps(body))
    res.raise_for_status()

    return res.json()


def list_accounts():
    """
    List accounts
    """

    body = {
        "id": 0,
        "method": "listaccounts",
        "jsonrpc": "2.0"
    }

    # make post request
    res = requests.post(url, data=json.dumps(body))
    res.raise_for_status()

    return res.json()


def list_received_by_address():
    """
    List accounts
    """

    body = {
        "id": 0,
        "method": "listreceivedbyaddress",
        "params": [6, True, True],
        "jsonrpc": "2.0"
    }

    # make post request
    res = requests.post(url, data=json.dumps(body))
    res.raise_for_status()

    return res.json()


def sendtoaddress(address, amount):
    """
    Send to address
    """

    body = {
        "id": 0,
        "method": "sendtoaddress",
        "params": [address, amount],
        "jsonrpc": "2.0"
    }

    # make post request
    res = requests.post(url, data=json.dumps(body))
    res.raise_for_status()

    return res.json()


if __name__ == '__main__':
    pass
