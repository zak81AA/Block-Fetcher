import time

class BlockScanner:
    def __init__(self, rpc: RPCClient):
        self.rpc = rpc

    def latest_block(self):
        return int(self.rpc.call("eth_blockNumber"), 16)

    def get_block(self, block_num):
        return self.rpc.call(
            "eth_getBlockByNumber",
            [hex(block_num), True]
        )

    def stream(self, start_block):
        current = start_block

        while True:
            latest = self.latest_block()

            while current <= latest:
                block = self.get_block(current)
                yield block
                current += 1

            time.sleep(2)