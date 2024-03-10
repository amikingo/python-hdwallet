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

    PUBLIC_KEY_ADDRESS_PREFIX = 0x49
    SCRIPT_ADDRESS_PREFIX = 0x53
    XPRIVATE_KEY_VERSIONS = XPrivateKeyVersions({
        "P2PKH": 0x221312b,
        "P2SH": 0x221312b
    })
    XPUBLIC_KEY_VERSIONS = XPublicKeyVersions({
        "P2PKH": 0x22d2533,
        "P2SH": 0x22d2533
    })
    MESSAGE_PREFIX = None
    WIF_PREFIX = 0x42


class Testnet(INetwork):

    PUBLIC_KEY_ADDRESS_PREFIX = 0x4c
    SCRIPT_ADDRESS_PREFIX = 0x89
    XPRIVATE_KEY_VERSIONS = XPrivateKeyVersions({
        "P2PKH": 0x3a805837,
        "P2SH": 0x3a805837
    })
    XPUBLIC_KEY_VERSIONS = XPublicKeyVersions({
        "P2PKH": 0x3a8061a0,
        "P2SH": 0x3a8061a0
    })

    MESSAGE_PREFIX = None
    WIF_PREFIX = 0xed


class TWINS(ICryptocurrency):

    NAME = "TWINS"
    SYMBOL = "TWINS"
    INFO = Info({
        "SOURCE_CODE": "https://github.com/NewCapital/TWINS-Core",
        "WEBSITES": [
            "https://win.win"
        ]
    })
    ECC = SLIP10Secp256k1ECC
    COIN_TYPE = 970
    NETWORKS = Networks({
        "MAINNET": Mainnet, "TESTNET": Testnet
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
