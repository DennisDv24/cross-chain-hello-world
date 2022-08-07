from brownie import EncodingTest
from brownie import accounts
import pytest

def test_encoding():
    DEV = '0xDFA0B3fCf7B9E6e1BFB8ef536Aa33B5aF6Fd7F47'
    c = EncodingTest.deploy({'from': accounts[0]})
    assert c.testEncoding(DEV) == DEV
