#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from ..ecc import SLIP10Ed25519ECC
from ..const import (
    NestedNamespace, CoinType, Entropies, Mnemonics, Seeds, HDs, Addresses, Networks, Params, XPrivateKeyVersions, XPublicKeyVersions
)
from .icryptocurrency import (
    ICryptocurrency, INetwork
)


class TezosAddressPrefixes(NestedNamespace):

    TZ1: str
    TZ2: str
    TZ3: str


TEZOS_ADDRESS_PREFIXES: TezosAddressPrefixes = TezosAddressPrefixes({
    "TZ1": "tz1",
    "TZ2": "tz2",
    "TZ3": "tz3"
})


class Mainnet(INetwork):

    XPRIVATE_KEY_VERSIONS = XPrivateKeyVersions({
        "P2PKH": 0x0488ade4
    })
    XPUBLIC_KEY_VERSIONS = XPublicKeyVersions({
        "P2PKH": 0x0488b21e
    })


class Tezos(ICryptocurrency):

    NAME = "Tezos"
    SYMBOL = "XTZ"
    SOURCE_CODE = "https://github.com/tezos/tezos"
    ECC = SLIP10Ed25519ECC
    COIN_TYPE = CoinType({
        "INDEX": 1729,
        "HARDENED": True
    })
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
        "TEZOS": "Tezos"
    })
    DEFAULT_ADDRESS = ADDRESSES.TEZOS
    PREFIXES = TEZOS_ADDRESS_PREFIXES
    PARAMS = Params({
        "ADDRESS_PREFIXES": {
            "TZ1": b"\x06\xa1\x9f",
            "TZ2": b"\x06\xa1\xa1",
            "TZ3": b"\x06\xa1\xa4"
        }
    })