#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from ..ecc import SLIP10Secp256k1ECC
from ..const import (
    Info, WitnessVersions, Entropies, Mnemonics, Seeds, HDs, Addresses, Networks, XPrivateKeyVersions, XPublicKeyVersions
)
from .icryptocurrency import (
    ICryptocurrency, INetwork
)


class Mainnet(INetwork):

    PUBLIC_KEY_ADDRESS_PREFIX = 0x38
    SCRIPT_ADDRESS_PREFIX = 0x3c
    HRP = "pw"
    WITNESS_VERSIONS = WitnessVersions({
        "P2WPKH": 0x00,
        "P2WSH": 0x00
    })
    XPRIVATE_KEY_VERSIONS = XPrivateKeyVersions({
        "P2PKH": 0x8f1daeb8,
        "P2SH": 0x8f1daeb8
    })
    XPUBLIC_KEY_VERSIONS = XPublicKeyVersions({
        "P2PKH": 0x696e82d1,
        "P2SH": 0x696e82d1
    })
    MESSAGE_PREFIX = "\x18Bitcoin Signed Message:\n"
    WIF_PREFIX = 0x6c


class Particl(ICryptocurrency):

    NAME = "Particl"
    SYMBOL = "PART"
    INFO = Info({
        "SOURCE_CODE": "https://github.com/particl/particl-core",
        "WHITEPAPER": "https://github.com/particl/whitepaper/blob/master/Particl%20Whitepaper%20Draft%20v0.3.pdf",
        "WEBSITES": [
            "http://particl.io",
            "https://particl.store"
        ]
    })
    ECC = SLIP10Secp256k1ECC
    COIN_TYPE = 44
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
        "P2PKH", "P2SH"
    })
    DEFAULT_ADDRESS = ADDRESSES.P2PKH