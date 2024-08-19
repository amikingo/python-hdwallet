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

    PUBLIC_KEY_ADDRESS_PREFIX = 0x1e
    SCRIPT_ADDRESS_PREFIX = 0x16
    HRP = "dogecoin"
    WITNESS_VERSIONS = WitnessVersions({
        "P2WPKH": 0x00,
        "P2WSH": 0x00
    })    
    XPRIVATE_KEY_VERSIONS = XPrivateKeyVersions({
        "P2PKH": 0x02fac398,
        "P2SH": 0x02fac398,
        "P2WPKH": 0x04b2430c,
        "P2WPKH_IN_P2SH": 0x049d7878
    })
    XPUBLIC_KEY_VERSIONS = XPublicKeyVersions({
        "P2PKH": 0x02facafd,
        "P2SH": 0x02facafd,
        "P2WPKH": 0x04b24746,
        "P2WPKH_IN_P2SH": 0x049d7cb2
    })
    MESSAGE_PREFIX = "\x19Dogecoin Signed Message:\n"
    WIF_PREFIX = 0xf1


class Testnet(INetwork):

    PUBLIC_KEY_ADDRESS_PREFIX = 0x71
    SCRIPT_ADDRESS_PREFIX = 0xc4
    HRP = "dogecointestnet"
    WITNESS_VERSIONS = WitnessVersions({
        "P2WPKH": 0x00,
        "P2WSH": 0x00
    })
    XPRIVATE_KEY_VERSIONS = XPrivateKeyVersions({
        "P2PKH": 0x04358394,
        "P2SH": 0x04358394,
        "P2WPKH": 0x04358394,
        "P2WPKH_IN_P2SH": 0x04358394
    })
    XPUBLIC_KEY_VERSIONS = XPublicKeyVersions({
        "P2PKH": 0x043587cf,
        "P2SH": 0x043587cf,
        "P2WPKH": 0x043587cf,
        "P2WPKH_IN_P2SH": 0x043587cf
    })
    MESSAGE_PREFIX = "\x19Dogecoin Signed Message:\n"
    WIF_PREFIX = 0xf1


class Dogecoin(ICryptocurrency):

    NAME = "Dogecoin"
    SYMBOL = "DOGE"
    INFO = Info({
        "SOURCE_CODE": "https://github.com/dogecoin/dogecoin",
        "WHITEPAPER": "https://github.com/dogecoin/dogecoin/blob/master/README.md",
        "WEBSITES": [
            "http://dogecoin.com"
        ]
    })
    ECC = SLIP10Secp256k1ECC
    COIN_TYPE = 3
    SUPPORT_BIP38 = True
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
    ADDRESSES = Addresses((
        "P2PKH", "P2SH", "P2WPKH", {"P2WPKH_IN_P2SH": "P2WPKH-In-P2SH"}
    ))
    DEFAULT_ADDRESS = ADDRESSES.P2PKH
