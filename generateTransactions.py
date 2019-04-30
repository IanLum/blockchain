import string
import random

def generateTransactions(minAmount, maxAmount, minSize, maxSize):
    t = []
    for i in range(random.randint(minAmount,maxAmount)): # generate transactions
        t.append(''.join([random.choice(string.ascii_letters + string.digits) for n in range(random.randint(minSize,maxSize))]))
    return t