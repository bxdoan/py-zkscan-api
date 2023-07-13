from py_zkscan_api import Explorers


if __name__ == '__main__':
    explorer = Explorers()
    data_block = explorer.get_last_block()
    print(f"Last block: {data_block['number']}, time: {data_block['timestamp']}, hash: {data_block['hash']}")
    data = explorer.get_block_by_number(data_block['number'])
    print(f"Block by number: {data}")
