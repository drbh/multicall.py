from enum import IntEnum


class Network(IntEnum):
    Mainnet = 1
    Kovan = 42
    Rinkeby = 4
    Görli = 5
    xDai = 100
    Bsc = 56
    Fantom = 250
    Polygon = 137


MULTICALL_ADDRESSES = {
    Network.Mainnet: '0xeefBa1e63905eF1D7ACbA5a8513c70307C1cE441',
    Network.Kovan: '0x2cc8688C5f75E365aaEEb4ea8D6a480405A48D2A',
    Network.Rinkeby: '0x42Ad527de7d4e9d9d011aC45B31D8551f8Fe9821',
    Network.Görli: '0x77dCa2C955b15e9dE4dbBCf1246B4B85b651e50e',
    Network.xDai: '0xb5b692a88BDFc81ca69dcB1d924f59f0413A602a',
    Network.Bsc: '0x1ee38d535d541c55c9dae27b12edf090c608e6fb',
    Network.Fantom: '0xb828c456600857abd4ed6c32facc607bd0464f4f',
    Network.Polygon: '0x95028e5b8a734bb7e2071f96de89babe75be9c8e',
}
