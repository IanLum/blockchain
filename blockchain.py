import hashlib
import random
from generateTransactions import generateTransactions
from merkleTree import merk
import time

class Block():

    def __init__(self, prevID, d, index, id=''):
        self.index = index
        self.previousBlockID = prevID
        self.nonce = ''
        self.id = id
        self.merkleRoot = merk(generateTransactions(4,20,4,20))[-1][0]
        self.difficulty = d

class Blockchain():
    
    def __init__(self):
        self.chain = [Block('',4,0,id='0'*64)] # create chain with genesis block
    
    def addBlock(self, block):
        self.chain.append(block)

    def newBlock(self):
        newblock =  Block(self.chain[-1].id, 4, self.chain[-1].index+1)

        nonce = 0
        mined = False
        while not mined:
            blockHash = hashlib.sha256((newblock.merkleRoot+newblock.previousBlockID+str(nonce)).encode('UTF-8')).hexdigest()
            if blockHash[:newblock.difficulty] == '0'*newblock.difficulty:
                mined = True
            else:
                nonce += 1
        newblock.nonce = nonce
        newblock.id = blockHash

        self.addBlock(newblock)

chain0 = Blockchain()
chainFile = open('chain.txt','w')


for i in range(15):
# while True:
    chainFile.write(str(vars(chain0.chain[-1])) + '\n')
    print(vars(chain0.chain[-1]))
    # input()
    chain0.newBlock()