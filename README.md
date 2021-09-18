# **raventool**

Tools for working with ravencoin core wallet json rpc.

Initial exploitation began with a blog post:
https://nessy.info/?p=1543

## Requirements
 * python3
 * virtualenv

## Install

```
$ virtualenv -p python3 venv/
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python setup.py develop
```

## Test

```
$ python setup.py test
test_get_transaction_fail (tests.test_main.MainTestCase) ... ok
test_get_transaction_success (tests.test_main.MainTestCase) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.041s

OK
```

## Usage

```
>>> from raventool.main import *
```

**get_transaction**

```
>>> transaction = get_transaction('af73af5e9c1cb6abbf1085e2220be742e707902a40781245eb5ceebf2b59cc72')

>>> transaction['result']['txid']
'af73af5e9c1cb6abbf1085e2220be742e707902a40781245eb5ceebf2b59cc72'

>>> transaction['result']['confirmations']
954

>>> transaction['result']['vout'][3]['scriptPubKey']['asset']['name']
'NESSY#Erik_Wolfeye'

>>> transaction['result']['vout'][3]['scriptPubKey']['asset']['ipfs_hash']
'Qmc2wkKd3TieWMENaBtPhADxvr42t8pMia1Kx461LS74Vr'
```

You can use cloudflare's ipfs gateway to view the asset:

https://cloudflare-ipfs.com/ipfs/Qmc2wkKd3TieWMENaBtPhADxvr42t8pMia1Kx461LS74Vr/

**get_wallet_info**

```
>>> get_wallet_info()
{'result': {'walletname': 'wallet.dat',
  'walletversion': 10500,
  'balance': ???,
  'unconfirmed_balance': 0.0,
  'immature_balance': 0.0,
  'txcount': 45,
  'keypoololdest': 1630722883,
  'keypoolsize': 1000,
  'keypoolsize_hd_internal': 999,
  'paytxfee': 0.0,
  'hdseedid': '???',
  'hdmasterkeyid': '???'},
 'error': None,
 'id': 0}
```

**list_my_assets**

```
>>> list_my_assets()
{'result': {
  'NESSY': 999820,
  'NESSY!': 1,
  'NESSY#Erik_Wolfeye': 1},
 'error': None,
 'id': 0}
```

**list_accounts**

```
>>> list_accounts()
{'result': {'': ???, 'private': 0.0}, 'error': None, 'id': 0}
```

**list_received_by_address**

```
In [20]: list_received_by_address()
Out[20]:
{'result': [
  {'address': '???',
   'account': '',
   'amount': 0.0,
   'confirmations': 1141,
   'label': '',
   'txids': ['???', '???']}],
 'error': None,
 'id': 0}
```

**sendtoaddress**

```
>>> sendtoaddress('????', 0.05)
{'result': '????',
 'error': None,
 'id': 0}
```
