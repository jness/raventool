import unittest

import requests

from raventool.main import *


class MainTestCase(unittest.TestCase):

    def test_get_transaction_success(self):
        txid = 'af73af5e9c1cb6abbf1085e2220be742e707902a40781245eb5ceebf2b59cc72'
        res = get_transaction(txid)
        self.assertEqual(res['result']['txid'], txid)

    def test_get_transaction_fail(self):
        txid = '0x'
        self.assertRaises(requests.exceptions.HTTPError, get_transaction, txid)

    def test_get_wallet_info(self):
        res = get_wallet_info()
        self.assertEqual(res['result']['walletname'], 'wallet.dat')

    def test_list_my_assets(self):
        res = list_my_assets()
        self.assertTrue('NESSY' in res['result'])

    def test_list_accounts(self):
        res = list_accounts()
        self.assertTrue(res['result'])

    def test_list_received_by_address(self):
        res = list_received_by_address()
        self.assertTrue(len(res['result']) > 1)
