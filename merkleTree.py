import hashlib
import random
import string
from generateTransactions import generateTransactions

def nextLayer(transactions):
    new = []
    for i in range(0,len(transactions)-1,2):
        new.append(hashlib.sha256((transactions[i]+transactions[i+1]).encode('UTF-8')).hexdigest())
    if len(transactions)%2 == 1:
        l = len(transactions)-1
        new.append(hashlib.sha256((transactions[l]+transactions[l]).encode('UTF-8')).hexdigest())
    return new

# t = generateTransactions(4,30,4,50)
t = ['1']*3

def merk(transactions):
    merkleTree = [transactions]
    transactions = list(map(lambda x: hashlib.sha256(x.encode('UTF-8')).hexdigest(),transactions))
    merkleTree.append(transactions)
    while len(transactions) > 1: # create merkle tree
        transactions = nextLayer(transactions)
        merkleTree.append(transactions)
    return merkleTree

# merkleTree = merk(t)
# for i in range(len(merkleTree)): # print
#     print('---')
#     print('layer', i, merkleTree[i])