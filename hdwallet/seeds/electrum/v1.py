#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from typing import Union

from ...crypto import sha256
from ...exceptions import MnemonicError
from ...mnemonics import (
    IMnemonic, ElectrumV1Mnemonic
)
from ...utils import bytes_to_string, encode
from ..iseed import ISeed


class ElectrumV1Seed(ISeed):

    hash_iteration_number: int = 10 ** 5

    @classmethod
    def name(cls) -> str:
        return "Electrum-V1"

    @classmethod
    def from_mnemonic(cls, mnemonic: Union[str, IMnemonic], **kwargs) -> str:
        mnemonic = (
            mnemonic.mnemonic() if isinstance(mnemonic, IMnemonic) else mnemonic
        )
        if not ElectrumV1Mnemonic.is_valid(mnemonic=mnemonic):
            raise MnemonicError(f"Invalid {cls.name()} mnemonic words")

        entropy: str = ElectrumV1Mnemonic.decode(mnemonic)
        entropy_hash: bytes = encode(entropy)
        for _ in range(cls.hash_iteration_number):
            entropy_hash = sha256(entropy_hash + encode(entropy))

        return bytes_to_string(entropy_hash)
