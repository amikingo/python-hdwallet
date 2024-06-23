#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
#             2024, Eyoel Tadesse <eyoel_tadesse@proton.me>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

import json
import os
import pytest

from hdwallet.addresses.p2pkh import P2PKHAddress
from hdwallet.addresses.p2sh import P2SHAddress
from hdwallet.addresses.p2wpkh import P2WPKHAddress
from hdwallet.addresses.p2wpkh_in_p2sh import P2WPKHInP2SHAddress
from hdwallet.addresses.p2wsh import P2WSHAddress
from hdwallet.addresses.p2wsh_in_p2sh import P2WSHInP2SHAddress
from hdwallet.addresses.p2tr import P2TRAddress
from hdwallet.addresses.ethereum import EthereumAddress
from hdwallet.addresses.xinfin import XinFinAddress
from hdwallet.addresses.tron import TronAddress
from hdwallet.addresses.ripple import RippleAddress
from hdwallet.addresses.filecoin import FilecoinAddress
from hdwallet.addresses.cosmos import CosmosAddress
from hdwallet.addresses.avalanche import AvalancheAddress
from hdwallet.addresses.eos import EOSAddress
from hdwallet.addresses.ergo import ErgoAddress
from hdwallet.addresses.icon import IconAddress
from hdwallet.addresses.okt_chain import OKTChainAddress
from hdwallet.addresses.harmony import HarmonyAddress
from hdwallet.addresses.zilliqa import ZilliqaAddress
from hdwallet.addresses.injective import InjectiveAddress

# Test Values
base_path: str = os.path.dirname(__file__)
file_path: str = os.path.abspath(os.path.join(base_path, "../../data/addresses.json"))
values = open(file_path, "r", encoding="utf-8")
_: dict = json.loads(values.read())
values.close()


def test_p2pkh_address():

    assert P2PKHAddress.name() == _["SLIP10-Secp256k1"]["addresses"]["P2PKH"]["name"]

    assert P2PKHAddress.encode(
        public_key= _["SLIP10-Secp256k1"]["compressed-public-key"],
        public_key_address_prefix=int(_["SLIP10-Secp256k1"]["addresses"]["P2PKH"]["compressed"]["args"]["public_key_address_prefix"], base=16),
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["P2PKH"]["compressed"]["args"]["public_key_type"]
    ) == _["SLIP10-Secp256k1"]["addresses"]["P2PKH"]["compressed"]["encode"]

    assert P2PKHAddress.decode(
        address=_["SLIP10-Secp256k1"]["addresses"]["P2PKH"]["compressed"]["encode"],
        public_key_address_prefix=int(_["SLIP10-Secp256k1"]["addresses"]["P2PKH"]["compressed"]["args"]["public_key_address_prefix"], base=16),
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["P2PKH"]["compressed"]["args"]["public_key_type"]
    ) ==  _["SLIP10-Secp256k1"]["addresses"]["P2PKH"]["compressed"]["decode"]


    assert P2PKHAddress.encode(
        public_key= _["SLIP10-Secp256k1"]["uncompressed-public-key"],
        public_key_address_prefix=int(_["SLIP10-Secp256k1"]["addresses"]["P2PKH"]["uncompressed"]["args"]["public_key_address_prefix"], base=16),
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["P2PKH"]["uncompressed"]["args"]["public_key_type"]
    ) == _["SLIP10-Secp256k1"]["addresses"]["P2PKH"]["uncompressed"]["encode"]

    assert P2PKHAddress.decode(
        address=_["SLIP10-Secp256k1"]["addresses"]["P2PKH"]["uncompressed"]["encode"],
        public_key_address_prefix=int(_["SLIP10-Secp256k1"]["addresses"]["P2PKH"]["uncompressed"]["args"]["public_key_address_prefix"], base=16),
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["P2PKH"]["uncompressed"]["args"]["public_key_type"]
    ) ==  _["SLIP10-Secp256k1"]["addresses"]["P2PKH"]["uncompressed"]["decode"]


def test_p2sh_address():

    assert P2SHAddress.name() == _["SLIP10-Secp256k1"]["addresses"]["P2SH"]["name"]

    assert P2SHAddress.encode(
        public_key= _["SLIP10-Secp256k1"]["compressed-public-key"],
        script_address_prefix=int(_["SLIP10-Secp256k1"]["addresses"]["P2SH"]["compressed"]["args"]["script_address_prefix"], base=16),
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["P2SH"]["compressed"]["args"]["public_key_type"]
    ) == _["SLIP10-Secp256k1"]["addresses"]["P2SH"]["compressed"]["encode"]

    assert P2SHAddress.decode(
        address=_["SLIP10-Secp256k1"]["addresses"]["P2SH"]["compressed"]["encode"],
        script_address_prefix=int(_["SLIP10-Secp256k1"]["addresses"]["P2SH"]["compressed"]["args"]["script_address_prefix"], base=16),
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["P2SH"]["compressed"]["args"]["public_key_type"]
    ) ==  _["SLIP10-Secp256k1"]["addresses"]["P2SH"]["compressed"]["decode"]


    assert P2SHAddress.encode(
        public_key= _["SLIP10-Secp256k1"]["uncompressed-public-key"],
        script_address_prefix=int(_["SLIP10-Secp256k1"]["addresses"]["P2SH"]["uncompressed"]["args"]["script_address_prefix"], base=16),
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["P2SH"]["uncompressed"]["args"]["public_key_type"]
    ) == _["SLIP10-Secp256k1"]["addresses"]["P2SH"]["uncompressed"]["encode"]

    assert P2SHAddress.decode(
        address=_["SLIP10-Secp256k1"]["addresses"]["P2SH"]["uncompressed"]["encode"],
        script_address_prefix=int(_["SLIP10-Secp256k1"]["addresses"]["P2SH"]["uncompressed"]["args"]["script_address_prefix"], base=16),
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["P2SH"]["uncompressed"]["args"]["public_key_type"]
    ) ==  _["SLIP10-Secp256k1"]["addresses"]["P2SH"]["uncompressed"]["decode"]


def test_p2wpkh_address():

    assert P2WPKHAddress.name() == _["SLIP10-Secp256k1"]["addresses"]["P2WPKH"]["name"]

    assert P2WPKHAddress.encode(
        public_key= _["SLIP10-Secp256k1"]["compressed-public-key"],
        hrp=_["SLIP10-Secp256k1"]["addresses"]["P2WPKH"]["compressed"]["args"]["hrp"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["P2WPKH"]["compressed"]["args"]["public_key_type"]
    ) == _["SLIP10-Secp256k1"]["addresses"]["P2WPKH"]["compressed"]["encode"]

    assert P2WPKHAddress.decode(
        address=_["SLIP10-Secp256k1"]["addresses"]["P2WPKH"]["compressed"]["encode"],
        hrp=_["SLIP10-Secp256k1"]["addresses"]["P2WPKH"]["compressed"]["args"]["hrp"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["P2WPKH"]["compressed"]["args"]["public_key_type"]
    ) ==  _["SLIP10-Secp256k1"]["addresses"]["P2WPKH"]["compressed"]["decode"]


    assert P2WPKHAddress.encode(
        public_key= _["SLIP10-Secp256k1"]["uncompressed-public-key"],
        hrp=_["SLIP10-Secp256k1"]["addresses"]["P2WPKH"]["uncompressed"]["args"]["hrp"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["P2WPKH"]["uncompressed"]["args"]["public_key_type"]
    ) == _["SLIP10-Secp256k1"]["addresses"]["P2WPKH"]["uncompressed"]["encode"]

    assert P2WPKHAddress.decode(
        address=_["SLIP10-Secp256k1"]["addresses"]["P2WPKH"]["uncompressed"]["encode"],
        hrp=_["SLIP10-Secp256k1"]["addresses"]["P2WPKH"]["uncompressed"]["args"]["hrp"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["P2WPKH"]["uncompressed"]["args"]["public_key_type"]
    ) ==  _["SLIP10-Secp256k1"]["addresses"]["P2WPKH"]["uncompressed"]["decode"]


def test_p2pkh_in_p2sh_address():

    assert P2WPKHInP2SHAddress.name() == _["SLIP10-Secp256k1"]["addresses"]["P2WPKH-In-P2SH"]["name"]

    assert P2WPKHInP2SHAddress.encode(
        public_key= _["SLIP10-Secp256k1"]["compressed-public-key"],
        script_address_prefix=int(_["SLIP10-Secp256k1"]["addresses"]["P2WPKH-In-P2SH"]["compressed"]["args"]["script_address_prefix"], base=16),
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["P2WPKH-In-P2SH"]["compressed"]["args"]["public_key_type"]
    ) == _["SLIP10-Secp256k1"]["addresses"]["P2WPKH-In-P2SH"]["compressed"]["encode"]

    assert P2WPKHInP2SHAddress.decode(
        address=_["SLIP10-Secp256k1"]["addresses"]["P2WPKH-In-P2SH"]["compressed"]["encode"],
        script_address_prefix=int(_["SLIP10-Secp256k1"]["addresses"]["P2WPKH-In-P2SH"]["compressed"]["args"]["script_address_prefix"], base=16),
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["P2WPKH-In-P2SH"]["compressed"]["args"]["public_key_type"]
    ) ==  _["SLIP10-Secp256k1"]["addresses"]["P2WPKH-In-P2SH"]["compressed"]["decode"]


    assert P2WPKHInP2SHAddress.encode(
        public_key= _["SLIP10-Secp256k1"]["uncompressed-public-key"],
        script_address_prefix=int(_["SLIP10-Secp256k1"]["addresses"]["P2WPKH-In-P2SH"]["uncompressed"]["args"]["script_address_prefix"], base=16),
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["P2WPKH-In-P2SH"]["uncompressed"]["args"]["public_key_type"]
    ) == _["SLIP10-Secp256k1"]["addresses"]["P2WPKH-In-P2SH"]["uncompressed"]["encode"]

    assert P2WPKHInP2SHAddress.decode(
        address=_["SLIP10-Secp256k1"]["addresses"]["P2WPKH-In-P2SH"]["uncompressed"]["encode"],
        script_address_prefix=int(_["SLIP10-Secp256k1"]["addresses"]["P2WPKH-In-P2SH"]["uncompressed"]["args"]["script_address_prefix"], base=16),
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["P2WPKH-In-P2SH"]["uncompressed"]["args"]["public_key_type"]
    ) ==  _["SLIP10-Secp256k1"]["addresses"]["P2WPKH-In-P2SH"]["uncompressed"]["decode"]


def test_p2tr_address():

    assert P2TRAddress.name() == _["SLIP10-Secp256k1"]["addresses"]["P2TR"]["name"]

    assert P2TRAddress.encode(
        public_key= _["SLIP10-Secp256k1"]["compressed-public-key"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["P2TR"]["compressed"]["args"]["public_key_type"]
    ) == _["SLIP10-Secp256k1"]["addresses"]["P2TR"]["compressed"]["encode"]

    assert P2TRAddress.decode(
        address=_["SLIP10-Secp256k1"]["addresses"]["P2TR"]["compressed"]["encode"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["P2TR"]["compressed"]["args"]["public_key_type"]
    ) ==  _["SLIP10-Secp256k1"]["addresses"]["P2TR"]["compressed"]["decode"]


    assert P2TRAddress.encode(
        public_key= _["SLIP10-Secp256k1"]["uncompressed-public-key"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["P2TR"]["uncompressed"]["args"]["public_key_type"]
    ) == _["SLIP10-Secp256k1"]["addresses"]["P2TR"]["uncompressed"]["encode"]

    assert P2TRAddress.decode(
        address=_["SLIP10-Secp256k1"]["addresses"]["P2TR"]["uncompressed"]["encode"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["P2TR"]["uncompressed"]["args"]["public_key_type"]
    ) ==  _["SLIP10-Secp256k1"]["addresses"]["P2TR"]["uncompressed"]["decode"]


def test_ethereum_address():

    assert EthereumAddress.name() == _["SLIP10-Secp256k1"]["addresses"]["Ethereum"]["name"]

    assert EthereumAddress.encode(
        public_key= _["SLIP10-Secp256k1"]["compressed-public-key"],
        skip_checksum_encode=_["SLIP10-Secp256k1"]["addresses"]["Ethereum"]["compressed"]["args"]["skip_checksum_encode"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["Ethereum"]["compressed"]["args"]["public_key_type"]
    ) == _["SLIP10-Secp256k1"]["addresses"]["Ethereum"]["compressed"]["encode"]

    assert EthereumAddress.decode(
        address=_["SLIP10-Secp256k1"]["addresses"]["Ethereum"]["compressed"]["encode"],
        skip_checksum_encode=_["SLIP10-Secp256k1"]["addresses"]["Ethereum"]["compressed"]["args"]["skip_checksum_encode"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["Ethereum"]["compressed"]["args"]["public_key_type"]
    ) ==  _["SLIP10-Secp256k1"]["addresses"]["Ethereum"]["compressed"]["decode"]


def test_xinfin_address():

    assert XinFinAddress.name() == _["SLIP10-Secp256k1"]["addresses"]["XinFin"]["name"]

    assert XinFinAddress.encode(
        public_key= _["SLIP10-Secp256k1"]["compressed-public-key"],
        skip_checksum_encode=_["SLIP10-Secp256k1"]["addresses"]["XinFin"]["compressed"]["args"]["skip_checksum_encode"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["XinFin"]["compressed"]["args"]["public_key_type"]
    ) == _["SLIP10-Secp256k1"]["addresses"]["XinFin"]["compressed"]["encode"]

    assert XinFinAddress.decode(
        address=_["SLIP10-Secp256k1"]["addresses"]["XinFin"]["compressed"]["encode"],
        skip_checksum_encode=_["SLIP10-Secp256k1"]["addresses"]["XinFin"]["compressed"]["args"]["skip_checksum_encode"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["XinFin"]["compressed"]["args"]["public_key_type"]
    ) ==  _["SLIP10-Secp256k1"]["addresses"]["XinFin"]["compressed"]["decode"]


def test_tron_address():

    assert TronAddress.name() == _["SLIP10-Secp256k1"]["addresses"]["Tron"]["name"]

    assert TronAddress.encode(
        public_key= _["SLIP10-Secp256k1"]["compressed-public-key"],
        skip_checksum_encode=_["SLIP10-Secp256k1"]["addresses"]["Tron"]["compressed"]["args"]["skip_checksum_encode"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["Tron"]["compressed"]["args"]["public_key_type"]
    ) == _["SLIP10-Secp256k1"]["addresses"]["Tron"]["compressed"]["encode"]

    assert TronAddress.decode(
        address=_["SLIP10-Secp256k1"]["addresses"]["Tron"]["compressed"]["encode"],
        skip_checksum_encode=_["SLIP10-Secp256k1"]["addresses"]["Tron"]["compressed"]["args"]["skip_checksum_encode"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["Tron"]["compressed"]["args"]["public_key_type"]
    ) ==  _["SLIP10-Secp256k1"]["addresses"]["Tron"]["compressed"]["decode"]


def test_ripple_address():

    assert RippleAddress.name() == _["SLIP10-Secp256k1"]["addresses"]["Ripple"]["name"]

    assert RippleAddress.encode(
        public_key= _["SLIP10-Secp256k1"]["compressed-public-key"],
        public_key_address_prefix=int(_["SLIP10-Secp256k1"]["addresses"]["Ripple"]["compressed"]["args"]["public_key_address_prefix"], base=16),
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["Ripple"]["compressed"]["args"]["public_key_type"]
    ) == _["SLIP10-Secp256k1"]["addresses"]["Ripple"]["compressed"]["encode"]

    assert RippleAddress.decode(
        address=_["SLIP10-Secp256k1"]["addresses"]["Ripple"]["compressed"]["encode"],
        public_key_address_prefix=int(_["SLIP10-Secp256k1"]["addresses"]["Ripple"]["compressed"]["args"]["public_key_address_prefix"], base=16),
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["Ripple"]["compressed"]["args"]["public_key_type"]
    ) ==  _["SLIP10-Secp256k1"]["addresses"]["Ripple"]["compressed"]["decode"]


    assert RippleAddress.encode(
        public_key= _["SLIP10-Secp256k1"]["uncompressed-public-key"],
        public_key_address_prefix=int(_["SLIP10-Secp256k1"]["addresses"]["Ripple"]["uncompressed"]["args"]["public_key_address_prefix"], base=16),
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["Ripple"]["uncompressed"]["args"]["public_key_type"]
    ) == _["SLIP10-Secp256k1"]["addresses"]["Ripple"]["uncompressed"]["encode"]

    assert RippleAddress.decode(
        address=_["SLIP10-Secp256k1"]["addresses"]["Ripple"]["uncompressed"]["encode"],
        public_key_address_prefix=int(_["SLIP10-Secp256k1"]["addresses"]["Ripple"]["uncompressed"]["args"]["public_key_address_prefix"], base=16),
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["Ripple"]["uncompressed"]["args"]["public_key_type"]
    ) ==  _["SLIP10-Secp256k1"]["addresses"]["Ripple"]["uncompressed"]["decode"]


def test_filecoin_address():

    assert FilecoinAddress.name() == _["SLIP10-Secp256k1"]["addresses"]["Filecoin"]["name"]

    assert FilecoinAddress.encode(
        public_key= _["SLIP10-Secp256k1"]["compressed-public-key"],
        address_type=_["SLIP10-Secp256k1"]["addresses"]["Filecoin"]["compressed"]["args"]["address_type"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["Filecoin"]["compressed"]["args"]["public_key_type"]
    ) == _["SLIP10-Secp256k1"]["addresses"]["Filecoin"]["compressed"]["encode"]

    assert FilecoinAddress.decode(
        address=_["SLIP10-Secp256k1"]["addresses"]["Filecoin"]["compressed"]["encode"],
        address_type=_["SLIP10-Secp256k1"]["addresses"]["Filecoin"]["compressed"]["args"]["address_type"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["Filecoin"]["compressed"]["args"]["public_key_type"]
    ) ==  _["SLIP10-Secp256k1"]["addresses"]["Filecoin"]["compressed"]["decode"]


    assert FilecoinAddress.encode(
        public_key= _["SLIP10-Secp256k1"]["uncompressed-public-key"],
        address_type=_["SLIP10-Secp256k1"]["addresses"]["Filecoin"]["uncompressed"]["args"]["address_type"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["Filecoin"]["uncompressed"]["args"]["public_key_type"]
    ) == _["SLIP10-Secp256k1"]["addresses"]["Filecoin"]["uncompressed"]["encode"]

    assert FilecoinAddress.decode(
        address=_["SLIP10-Secp256k1"]["addresses"]["Filecoin"]["uncompressed"]["encode"],
        address_type=_["SLIP10-Secp256k1"]["addresses"]["Filecoin"]["uncompressed"]["args"]["address_type"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["Filecoin"]["uncompressed"]["args"]["public_key_type"]
    ) ==  _["SLIP10-Secp256k1"]["addresses"]["Filecoin"]["uncompressed"]["decode"]


def test_cosmos_address():

    assert CosmosAddress.name() == _["SLIP10-Secp256k1"]["addresses"]["Cosmos"]["name"]

    assert CosmosAddress.encode(
        public_key= _["SLIP10-Secp256k1"]["compressed-public-key"],
        hrp=_["SLIP10-Secp256k1"]["addresses"]["Cosmos"]["compressed"]["args"]["hrp"],
        address_type=_["SLIP10-Secp256k1"]["addresses"]["Cosmos"]["compressed"]["args"]["public_key_type"]
    ) == _["SLIP10-Secp256k1"]["addresses"]["Cosmos"]["compressed"]["encode"]

    assert CosmosAddress.decode(
        address=_["SLIP10-Secp256k1"]["addresses"]["Cosmos"]["compressed"]["encode"],
        hrp=_["SLIP10-Secp256k1"]["addresses"]["Cosmos"]["compressed"]["args"]["hrp"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["Cosmos"]["compressed"]["args"]["public_key_type"]
    ) ==  _["SLIP10-Secp256k1"]["addresses"]["Cosmos"]["compressed"]["decode"]


    assert CosmosAddress.encode(
        public_key= _["SLIP10-Secp256k1"]["uncompressed-public-key"],
        hrp=_["SLIP10-Secp256k1"]["addresses"]["Cosmos"]["uncompressed"]["args"]["hrp"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["Cosmos"]["uncompressed"]["args"]["public_key_type"]
    ) == _["SLIP10-Secp256k1"]["addresses"]["Cosmos"]["uncompressed"]["encode"]

    assert CosmosAddress.decode(
        address=_["SLIP10-Secp256k1"]["addresses"]["Cosmos"]["uncompressed"]["encode"],
        hrp=_["SLIP10-Secp256k1"]["addresses"]["Cosmos"]["uncompressed"]["args"]["hrp"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["Cosmos"]["uncompressed"]["args"]["public_key_type"]
    ) ==  _["SLIP10-Secp256k1"]["addresses"]["Cosmos"]["uncompressed"]["decode"]


def test_avalanche_address():

    assert AvalancheAddress.name() == _["SLIP10-Secp256k1"]["addresses"]["Avalanche"]["name"]

    assert AvalancheAddress.encode(
        public_key= _["SLIP10-Secp256k1"]["compressed-public-key"],
        address_type=_["SLIP10-Secp256k1"]["addresses"]["Avalanche"]["compressed"]["args"]["address_type"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["Avalanche"]["compressed"]["args"]["public_key_type"]
    ) == _["SLIP10-Secp256k1"]["addresses"]["Avalanche"]["compressed"]["encode"]

    assert AvalancheAddress.decode(
        address=_["SLIP10-Secp256k1"]["addresses"]["Avalanche"]["compressed"]["encode"],
        address_type=_["SLIP10-Secp256k1"]["addresses"]["Avalanche"]["compressed"]["args"]["address_type"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["Avalanche"]["compressed"]["args"]["public_key_type"]
    ) ==  _["SLIP10-Secp256k1"]["addresses"]["Avalanche"]["compressed"]["decode"]


    assert AvalancheAddress.encode(
        public_key= _["SLIP10-Secp256k1"]["uncompressed-public-key"],
        address_type=_["SLIP10-Secp256k1"]["addresses"]["Avalanche"]["uncompressed"]["args"]["address_type"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["Avalanche"]["uncompressed"]["args"]["public_key_type"]
    ) == _["SLIP10-Secp256k1"]["addresses"]["Avalanche"]["uncompressed"]["encode"]

    assert AvalancheAddress.decode(
        address=_["SLIP10-Secp256k1"]["addresses"]["Avalanche"]["uncompressed"]["encode"],
        address_type=_["SLIP10-Secp256k1"]["addresses"]["Avalanche"]["uncompressed"]["args"]["address_type"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["Avalanche"]["uncompressed"]["args"]["public_key_type"]
    ) ==  _["SLIP10-Secp256k1"]["addresses"]["Avalanche"]["uncompressed"]["decode"]


def test_eos_address():

    assert EOSAddress.name() == _["SLIP10-Secp256k1"]["addresses"]["EOS"]["name"]

    assert EOSAddress.encode(
        public_key= _["SLIP10-Secp256k1"]["compressed-public-key"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["EOS"]["compressed"]["args"]["public_key_type"]
    ) == _["SLIP10-Secp256k1"]["addresses"]["EOS"]["compressed"]["encode"]

    assert EOSAddress.decode(
        address=_["SLIP10-Secp256k1"]["addresses"]["EOS"]["compressed"]["encode"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["EOS"]["compressed"]["args"]["public_key_type"]
    ) ==  _["SLIP10-Secp256k1"]["addresses"]["EOS"]["compressed"]["decode"]


    assert EOSAddress.encode(
        public_key= _["SLIP10-Secp256k1"]["uncompressed-public-key"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["EOS"]["uncompressed"]["args"]["public_key_type"]
    ) == _["SLIP10-Secp256k1"]["addresses"]["EOS"]["uncompressed"]["encode"]

    assert EOSAddress.decode(
        address=_["SLIP10-Secp256k1"]["addresses"]["EOS"]["uncompressed"]["encode"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["EOS"]["uncompressed"]["args"]["public_key_type"]
    ) ==  _["SLIP10-Secp256k1"]["addresses"]["EOS"]["uncompressed"]["decode"]

def test_ergo_address():

    assert ErgoAddress.name() == _["SLIP10-Secp256k1"]["addresses"]["Ergo"]["name"]

    assert ErgoAddress.encode(
        public_key= _["SLIP10-Secp256k1"]["compressed-public-key"],
        address_type=_["SLIP10-Secp256k1"]["addresses"]["Ergo"]["compressed"]["args"]["address_type"],
        network_type=_["SLIP10-Secp256k1"]["addresses"]["Ergo"]["compressed"]["args"]["network_type"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["Ergo"]["compressed"]["args"]["public_key_type"]
    ) == _["SLIP10-Secp256k1"]["addresses"]["Ergo"]["compressed"]["encode"]

    assert ErgoAddress.decode(
        address=_["SLIP10-Secp256k1"]["addresses"]["Ergo"]["compressed"]["encode"],
        address_type=_["SLIP10-Secp256k1"]["addresses"]["Ergo"]["compressed"]["args"]["address_type"],
        network_type=_["SLIP10-Secp256k1"]["addresses"]["Ergo"]["compressed"]["args"]["network_type"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["Ergo"]["compressed"]["args"]["public_key_type"]
    ) ==  _["SLIP10-Secp256k1"]["addresses"]["Ergo"]["compressed"]["decode"]


    assert ErgoAddress.encode(
        public_key= _["SLIP10-Secp256k1"]["uncompressed-public-key"],
        address_type=_["SLIP10-Secp256k1"]["addresses"]["Ergo"]["uncompressed"]["args"]["address_type"],
        network_type=_["SLIP10-Secp256k1"]["addresses"]["Ergo"]["uncompressed"]["args"]["network_type"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["Ergo"]["uncompressed"]["args"]["public_key_type"]
    ) == _["SLIP10-Secp256k1"]["addresses"]["Ergo"]["uncompressed"]["encode"]

    assert ErgoAddress.decode(
        address=_["SLIP10-Secp256k1"]["addresses"]["Ergo"]["uncompressed"]["encode"],
        address_type=_["SLIP10-Secp256k1"]["addresses"]["Ergo"]["uncompressed"]["args"]["address_type"],
        network_type=_["SLIP10-Secp256k1"]["addresses"]["Ergo"]["uncompressed"]["args"]["network_type"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["Ergo"]["uncompressed"]["args"]["public_key_type"]
    ) ==  _["SLIP10-Secp256k1"]["addresses"]["Ergo"]["uncompressed"]["decode"]


def test_okt_chain_address():

    assert OKTChainAddress.name() == _["SLIP10-Secp256k1"]["addresses"]["OKT-Chain"]["name"]

    assert OKTChainAddress.encode(
        public_key= _["SLIP10-Secp256k1"]["compressed-public-key"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["OKT-Chain"]["compressed"]["args"]["public_key_type"]
    ) == _["SLIP10-Secp256k1"]["addresses"]["OKT-Chain"]["compressed"]["encode"]

    assert OKTChainAddress.decode(
        address=_["SLIP10-Secp256k1"]["addresses"]["OKT-Chain"]["compressed"]["encode"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["OKT-Chain"]["compressed"]["args"]["public_key_type"]
    ) ==  _["SLIP10-Secp256k1"]["addresses"]["OKT-Chain"]["compressed"]["decode"]


    assert OKTChainAddress.encode(
        public_key= _["SLIP10-Secp256k1"]["uncompressed-public-key"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["OKT-Chain"]["uncompressed"]["args"]["public_key_type"]
    ) == _["SLIP10-Secp256k1"]["addresses"]["OKT-Chain"]["uncompressed"]["encode"]

    assert OKTChainAddress.decode(
        address=_["SLIP10-Secp256k1"]["addresses"]["OKT-Chain"]["uncompressed"]["encode"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["OKT-Chain"]["uncompressed"]["args"]["public_key_type"]
    ) ==  _["SLIP10-Secp256k1"]["addresses"]["OKT-Chain"]["uncompressed"]["decode"]


def test_harmony_address():

    assert HarmonyAddress.name() == _["SLIP10-Secp256k1"]["addresses"]["Harmony"]["name"]

    assert HarmonyAddress.encode(
        public_key= _["SLIP10-Secp256k1"]["compressed-public-key"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["Harmony"]["compressed"]["args"]["public_key_type"]
    ) == _["SLIP10-Secp256k1"]["addresses"]["Harmony"]["compressed"]["encode"]

    assert HarmonyAddress.decode(
        address=_["SLIP10-Secp256k1"]["addresses"]["Harmony"]["compressed"]["encode"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["Harmony"]["compressed"]["args"]["public_key_type"]
    ) ==  _["SLIP10-Secp256k1"]["addresses"]["Harmony"]["compressed"]["decode"]


    assert HarmonyAddress.encode(
        public_key= _["SLIP10-Secp256k1"]["uncompressed-public-key"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["Harmony"]["uncompressed"]["args"]["public_key_type"]
    ) == _["SLIP10-Secp256k1"]["addresses"]["Harmony"]["uncompressed"]["encode"]

    assert HarmonyAddress.decode(
        address=_["SLIP10-Secp256k1"]["addresses"]["Harmony"]["uncompressed"]["encode"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["Harmony"]["uncompressed"]["args"]["public_key_type"]
    ) ==  _["SLIP10-Secp256k1"]["addresses"]["Harmony"]["uncompressed"]["decode"]


def test_zilliqa_address():

    assert ZilliqaAddress.name() == _["SLIP10-Secp256k1"]["addresses"]["Zilliqa"]["name"]

    assert ZilliqaAddress.encode(
        public_key= _["SLIP10-Secp256k1"]["compressed-public-key"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["Zilliqa"]["compressed"]["args"]["public_key_type"]
    ) == _["SLIP10-Secp256k1"]["addresses"]["Zilliqa"]["compressed"]["encode"]

    assert ZilliqaAddress.decode(
        address=_["SLIP10-Secp256k1"]["addresses"]["Zilliqa"]["compressed"]["encode"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["Zilliqa"]["compressed"]["args"]["public_key_type"]
    ) ==  _["SLIP10-Secp256k1"]["addresses"]["Zilliqa"]["compressed"]["decode"]


    assert ZilliqaAddress.encode(
        public_key= _["SLIP10-Secp256k1"]["uncompressed-public-key"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["Zilliqa"]["uncompressed"]["args"]["public_key_type"]
    ) == _["SLIP10-Secp256k1"]["addresses"]["Zilliqa"]["uncompressed"]["encode"]

    assert ZilliqaAddress.decode(
        address=_["SLIP10-Secp256k1"]["addresses"]["Zilliqa"]["uncompressed"]["encode"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["Zilliqa"]["uncompressed"]["args"]["public_key_type"]
    ) ==  _["SLIP10-Secp256k1"]["addresses"]["Zilliqa"]["uncompressed"]["decode"]


def test_injective_address():

    assert InjectiveAddress.name() == _["SLIP10-Secp256k1"]["addresses"]["Injective"]["name"]

    assert InjectiveAddress.encode(
        public_key= _["SLIP10-Secp256k1"]["compressed-public-key"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["Injective"]["compressed"]["args"]["public_key_type"]
    ) == _["SLIP10-Secp256k1"]["addresses"]["Injective"]["compressed"]["encode"]

    assert InjectiveAddress.decode(
        address=_["SLIP10-Secp256k1"]["addresses"]["Injective"]["compressed"]["encode"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["Injective"]["compressed"]["args"]["public_key_type"]
    ) ==  _["SLIP10-Secp256k1"]["addresses"]["Injective"]["compressed"]["decode"]


    assert InjectiveAddress.encode(
        public_key= _["SLIP10-Secp256k1"]["uncompressed-public-key"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["Injective"]["uncompressed"]["args"]["public_key_type"]
    ) == _["SLIP10-Secp256k1"]["addresses"]["Injective"]["uncompressed"]["encode"]

    assert InjectiveAddress.decode(
        address=_["SLIP10-Secp256k1"]["addresses"]["Injective"]["uncompressed"]["encode"],
        public_key_type=_["SLIP10-Secp256k1"]["addresses"]["Injective"]["uncompressed"]["args"]["public_key_type"]
    ) ==  _["SLIP10-Secp256k1"]["addresses"]["Injective"]["uncompressed"]["decode"]
