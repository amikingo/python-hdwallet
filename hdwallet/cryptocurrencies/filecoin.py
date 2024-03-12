#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from ..ecc import SLIP10Secp256k1ECC
from ..const import (
    Info, Entropies, Mnemonics, Seeds, HDs, Addresses, AddressTypes, Networks, Params, XPrivateKeyVersions, XPublicKeyVersions
)
from .icryptocurrency import (
    ICryptocurrency, INetwork
)


class Mainnet(INetwork):

    XPRIVATE_KEY_VERSIONS = XPrivateKeyVersions({
        "P2PKH": 0x488ade4
    })
    XPUBLIC_KEY_VERSIONS = XPublicKeyVersions({
        "P2PKH": 0x488b21e
    })
    WIF_PREFIX = 0x80


class Filecoin(ICryptocurrency):

    NAME = "Filecoin"
    SYMBOL = "FIL"
    INFO = Info({
        "SOURCE_CODE": "https://github.com/filecoin-project",
        "WHITEPAPER": "https://docs.filecoin.io",
        "WEBSITES": [
            "https://filecoin.io"
        ]
    })
    ECC = SLIP10Secp256k1ECC
    COIN_TYPE = 461
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
        "FILECOIN": "Filecoin"
    })
    DEFAULT_ADDRESS = ADDRESSES.FILECOIN
    ADDRESS_TYPES = AddressTypes({
        "SECP256K1": "secp256k1",
        "BLS": "bls"
    })
    DEFAULT_ADDRESS_TYPE = ADDRESS_TYPES.SECP256K1
    PARAMS = Params({
        "ALPHABET": "abcdefghijklmnopqrstuvwxyz234567",
        "ADDRESS_PREFIX": "f",
        "ADDRESS_TYPES": {
            "SECP256K1": 1,  # A SECP256K1 public key address.
            "BLS": 3  # A BLS public key address.
        }
    })