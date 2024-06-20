#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from typing import (
    List, Union
)

import os

from ..exceptions import EntropyError
from ..utils import (
    get_bytes, bytes_to_string, bytes_to_integer
)


class IEntropy:

    _entropy: str
    _strength: int

    strengths: List[int]

    def __init__(self, entropy: Union[bytes, str]) -> None:
        try:
            strength: int = len(get_bytes(entropy))
            if self.name() == "Electrum-V2":
                if not self.are_entropy_bits_enough(get_bytes(entropy)):
                    raise EntropyError("Entropy bits are not enough")
                self._strength = bytes_to_integer(get_bytes(entropy)).bit_length()
            else:
                if not self.is_valid_bytes_strength(strength):
                    raise EntropyError("Unsupported entropy strength")
                self._strength = strength * 8
            self._entropy = bytes_to_string(entropy)
        except ValueError:
            raise EntropyError("Invalid entropy data")

    @classmethod
    def name(cls) -> str:
        pass

    def entropy(self) -> str:
        return self._entropy

    def strength(self) -> int:
        return self._strength

    @classmethod
    def generate(cls, strength: int) -> str:
        return bytes_to_string(
            os.urandom(strength // 8)
        )

    @classmethod
    def is_valid_strength(cls, strength: int) -> bool:
        return strength in cls.strengths

    @classmethod
    def is_valid_bytes_strength(cls, bytes_strength: int) -> bool:
        return cls.is_valid_strength(bytes_strength * 8)

    def are_entropy_bits_enough(self, entropy: Union[bytes, int]) -> bool:
        pass
