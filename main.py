import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(f"{self.index}{self.previous_hash}{self.data}{self.timestamp}".encode())
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block", time.time())

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), latest_block.hash, data, time.time())
        self.chain.append(new_block)

blockchain = Blockchain()
blockchain.add_block("Transação 1")
blockchain.add_block("Transação 2")

for block in blockchain.chain:
    print(vars(block))


