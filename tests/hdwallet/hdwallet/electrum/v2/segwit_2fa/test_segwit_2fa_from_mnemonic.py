#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
#             2024, Eyoel Tadesse <eyoel_tadesse@proton.me>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from hdwallet import HDWallet
from hdwallet.cryptocurrencies import CRYPTOCURRENCIES
from hdwallet.derivations import DERIVATIONS
from hdwallet.mnemonics import ElectrumV2Mnemonic
from hdwallet.hds import HDS


def test_segiwt_2fa_from_mnemonic(data):

    cryptocurrency = CRYPTOCURRENCIES.cryptocurrency(
        data["hdwallet"]["Electrum-V2"]["segwit-2fa"]["cryptocurrency"]
    )
    hdwallet: HDWallet = HDWallet(
        cryptocurrency=cryptocurrency,
        hd=HDS.hd(
            data["hdwallet"]["Electrum-V2"]["segwit-2fa"]["hd"]
        ),
        network=data["hdwallet"]["Electrum-V2"]["segwit-2fa"]["network"],
        language=data["hdwallet"]["Electrum-V2"]["segwit-2fa"]["language"].lower(),
        mnemonic_type=data["hdwallet"]["Electrum-V2"]["segwit-2fa"]["mnemonic_type"],
        mode=data["hdwallet"]["Electrum-V2"]["segwit-2fa"]["mode"],
        public_key_type=data["hdwallet"]["Electrum-V2"]["segwit-2fa"]["public_key_type"]
    ).from_mnemonic(
        mnemonic=ElectrumV2Mnemonic(
            mnemonic=data["hdwallet"]["Electrum-V2"]["segwit-2fa"]["mnemonic"],
            mnemonic_type=data["hdwallet"]["Electrum-V2"]["segwit-2fa"]["mnemonic_type"]
        )
    ).from_derivation(
        derivation=DERIVATIONS.derivation(data["hdwallet"]["Electrum-V1"]["derivation"]["name"])(
            **data["hdwallet"]["Electrum-V1"]["derivation"]["args"]
        )
    )

    assert hdwallet.cryptocurrency() == data["hdwallet"]["Electrum-V2"]["segwit-2fa"]["cryptocurrency"]
    assert hdwallet.symbol() == data["hdwallet"]["Electrum-V2"]["segwit-2fa"]["symbol"]
    assert hdwallet.network() == data["hdwallet"]["Electrum-V2"]["segwit-2fa"]["network"]
    assert hdwallet.coin_type() == data["hdwallet"]["Electrum-V2"]["segwit-2fa"]["coin_type"]
    assert hdwallet.entropy() == data["hdwallet"]["Electrum-V2"]["segwit-2fa"]["entropy"]
    assert hdwallet.strength() == data["hdwallet"]["Electrum-V2"]["segwit-2fa"]["strength"]
    assert hdwallet.mnemonic() == data["hdwallet"]["Electrum-V2"]["segwit-2fa"]["mnemonic"]
    assert hdwallet.language() == data["hdwallet"]["Electrum-V2"]["segwit-2fa"]["language"]
    assert hdwallet.seed() ==  data["hdwallet"]["Electrum-V2"]["segwit-2fa"]["seed"]
    assert hdwallet.ecc() == data["hdwallet"]["Electrum-V2"]["segwit-2fa"]["ecc"]
    assert hdwallet.hd() == data["hdwallet"]["Electrum-V2"]["segwit-2fa"]["hd"]
    assert hdwallet.master_private_key() == data["hdwallet"]["Electrum-V2"]["segwit-2fa"]["master_private_key"]
    assert hdwallet.master_wif() == data["hdwallet"]["Electrum-V2"]["segwit-2fa"]["master_wif"]
    assert hdwallet.master_public_key() == data["hdwallet"]["Electrum-V2"]["segwit-2fa"]["master_public_key"]
    assert hdwallet.public_key_type() == data["hdwallet"]["Electrum-V2"]["segwit-2fa"]["public_key_type"]
    assert hdwallet.wif_type() == data["hdwallet"]["Electrum-V2"]["segwit-2fa"]["wif_type"]

    assert hdwallet.private_key() == data["hdwallet"]["Electrum-V2"]["segwit-2fa"]["derivations"][-1]["private_key"]
    assert hdwallet.wif() == data["hdwallet"]["Electrum-V2"]["segwit-2fa"]["derivations"][-1]["wif"]
    assert hdwallet.public_key() == data["hdwallet"]["Electrum-V2"]["segwit-2fa"]["derivations"][-1]["public_key"]
    assert hdwallet.uncompressed() == data["hdwallet"]["Electrum-V2"]["segwit-2fa"]["derivations"][-1]["uncompressed"]
    assert hdwallet.compressed() == data["hdwallet"]["Electrum-V2"]["segwit-2fa"]["derivations"][-1]["compressed"]

    assert hdwallet.address() == data["hdwallet"]["Electrum-V2"]["segwit-2fa"]["derivations"][-1]["address"]
    assert hdwallet.dumps() == data["hdwallet"]["Electrum-V2"]["segwit-2fa"]

    dump = data["hdwallet"]["Electrum-V2"]["segwit-2fa"].copy()
    del dump["derivations"]
    dump["derivation"] = data["hdwallet"]["Electrum-V2"]["segwit-2fa"]["derivations"][-1].copy()
    assert hdwallet.dump() == dump
