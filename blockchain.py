import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

    @staticmethod
    def calculate_hash(index, previous_hash, timestamp, data):
        value = str(index) + previous_hash + str(timestamp) + data
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    @staticmethod
    def create_genesis_block():
        return Block(0, "0", int(time.time()), "Genesis Block", Block.calculate_hash(0, "0", int(time.time()), "Genesis Block"))

    @staticmethod
    def create_new_block(previous_block, data):
        index = previous_block.index + 1
        timestamp = int(time.time())
        previous_hash = previous_block.hash
        hash = Block.calculate_hash(index, previous_hash, timestamp, data)
        return Block(index, previous_hash, timestamp, data, hash)

class Blockchain:
    def __init__(self):
        self.chain = [Block.create_genesis_block()]

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        self.chain.append(new_block)

def main():
    my_blockchain = Blockchain()

    # Adding blocks to the blockchain
    my_blockchain.add_block(Block.create_new_block(my_blockchain.get_latest_block(), "Block 1 Data"))
    my_blockchain.add_block(Block.create_new_block(my_blockchain.get_latest_block(), "Block 2 Data"))
    my_blockchain.add_block(Block.create_new_block(my_blockchain.get_latest_block(), "Block 3 Data"))

    # Display the blockchain
    for block in my_blockchain.chain:
        print(f"Index: {block.index}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Hash: {block.hash}")
        print("\n")

if __name__ == "__main__":
    main()
