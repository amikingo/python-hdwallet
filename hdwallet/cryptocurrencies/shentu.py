#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from ..ecc import SLIP10Secp256k1ECC
from ..const import (
    Info, Entropies, Mnemonics, Seeds, HDs, Addresses, Networks, XPrivateKeyVersions, XPublicKeyVersions
)
from .icryptocurrency import (
    ICryptocurrency, INetwork
)


class Mainnet(INetwork):

    HRP = "certik"
    XPRIVATE_KEY_VERSIONS = XPrivateKeyVersions({
        "P2PKH": 0x488ade4
    })
    XPUBLIC_KEY_VERSIONS = XPublicKeyVersions({
        "P2PKH": 0x488b21e
    })
    WIF_PREFIX = 0x80


class Shentu(ICryptocurrency):

    NAME = "Shentu"  # Certik old name
    SYMBOL = "CTK"
    INFO = Info({
        "SOURCE_CODE": "https://github.com/ShentuChain",
        "WHITEPAPER": "https://www.shentu.technology/whitepaper",
        "WEBSITES": [
            "https://www.shentu.technology"
        ]
    })
    ECC = SLIP10Secp256k1ECC
    COIN_TYPE = 118  # Cosmos coin type
    NETWORKS = Networks({
        "MAINNET": Mainnet
    })
    DEFAULT_NETWORK = NETWORKS.MAINNET
    ENTROPIES = Entropies({
        "BIP39"
    })
    MNEMONICS = Mnemonics({
        "BIP39"
    })
    SEEDS = Seeds({
        "BIP39"
    })
    HDS = HDs({
        "BIP32", "BIP44"
    })
    DEFAULT_HD = HDS.BIP44
    ADDRESSES = Addresses({
        "COSMOS": "Cosmos"
    })
    DEFAULT_ADDRESS = ADDRESSES.COSMOS