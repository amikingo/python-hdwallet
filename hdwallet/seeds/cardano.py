#!/usr/bin/env python3

# Copyright © 2020-2023, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from typing import Literal

import cbor2

from ..utils import get_bytes, bytes_to_string
from ..crypto import blake2b_256
from ..mnemonics.bip39 import BIP39Mnemonic
from .iseed import ISeed


class CardanoSeed(ISeed):

    @classmethod
    def generate(cls, mnemonic: str, seed_type: Literal["byron-legacy", "icarus"] = "icarus", **kwargs) -> str:

        if seed_type == "byron-legacy":
            return cls.generate_byron_legacy(mnemonic=mnemonic)
        elif seed_type == "icarus":
            return cls.generate_icarus(mnemonic=mnemonic)
        else:
            expected: tuple = ("byron-legacy", "icarus")
            raise ValueError(f"Invalid seed type (expected: {expected}, got: {seed_type!r})")

    @classmethod
    def generate_byron_legacy(cls, mnemonic: str) -> str:

        if not BIP39Mnemonic.is_valid(mnemonic=mnemonic):
            ValueError("Invalid BIP39 mnemonic words")

        return bytes_to_string(blake2b_256(
            cbor2.dumps(get_bytes(BIP39Mnemonic.decode(mnemonic=mnemonic)))
        ))

    @classmethod
    def generate_icarus(cls, mnemonic: str) -> str:

        if not BIP39Mnemonic.is_valid(mnemonic=mnemonic):
            ValueError("Invalid BIP39 mnemonic words")

        return BIP39Mnemonic.decode(mnemonic=mnemonic)
