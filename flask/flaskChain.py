from flask import Flask, render_template
import sys
sys.path.insert(0, '/Users/ianlum/Documents/Cryptocurrency/blockchain')
from blockchain import Block, Blockchain
app = Flask(__name__)

chain0 = Blockchain()
displayChain = [vars(chain0.chain[0])]
mining = False

@app.route('/')
def init():
    return render_template('b.html', chain=displayChain)

@app.route('/mineBlock')
def mineBlock():
    global mining
    if not mining:
        mining = True
        isMined = chain0.newBlock()
        displayChain.insert(0,vars(chain0.chain[-1]))
        print('new')
        mining = False
        return ''
        