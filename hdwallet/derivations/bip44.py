#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from typing import (
    Tuple, Union, Optional
)

from ..utils import (
    normalize_derivation, index_tuple_to_string
)
from .iderivation import IDerivation


class CHANGES:

    EXTERNAL_CHAIN: str = "external-chain"
    INTERNAL_CHAIN: str = "internal-chain"


class BIP44Derivation(IDerivation):  # https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki

    _purpose: Tuple[int, bool] = (44, True)
    _coin_type: Tuple[int, bool]
    _account: Union[Tuple[int, bool], Tuple[int, int, bool]]
    _change: Tuple[int, bool]
    _address: Union[Tuple[int, bool], Tuple[int, int, bool]]
    changes: dict = {
        "external-chain": 0, "internal-chain": 1
    }

    def __init__(
        self,
        coin_type: int = 0,
        account: Union[int, Tuple[int, int]] = 0,
        change: str = "external-chain",
        address: Union[int, Tuple[int, int]] = 0
    ) -> None:
        super(BIP44Derivation, self).__init__(indexes=[])

        self._coin_type = (coin_type, True)
        self._account = (*account, True) if isinstance(account, tuple) else (account, True)
        self._change = (self.changes[change], False)
        self._address = (*address, False) if isinstance(address, tuple) else (address, False)
        self._path, self._indexes, self._derivations = normalize_derivation(path=(
            f"m/{index_tuple_to_string(index=self._purpose)}/"
            f"{index_tuple_to_string(index=self._coin_type)}/"
            f"{index_tuple_to_string(index=self._account)}/"
            f"{index_tuple_to_string(index=self._change)}/"
            f"{index_tuple_to_string(index=self._address)}"
        ))

    @classmethod
    def name(cls) -> str:
        return "BIP44"

    def from_coin_type(self, coin_type: int) -> "BIP44Derivation":
        self._coin_type = (coin_type, True)
        self._path, self._indexes, self._derivations = normalize_derivation(path=(
            f"m/{index_tuple_to_string(index=self._purpose)}/"
            f"{index_tuple_to_string(index=self._coin_type)}/"
            f"{index_tuple_to_string(index=self._account)}/"
            f"{index_tuple_to_string(index=self._change)}/"
            f"{index_tuple_to_string(index=self._address)}"
        ))
        return self

    def from_account(self, account: Union[int, Tuple[int, int]]) -> "BIP44Derivation":
        self._account = (*account, True) if isinstance(account, tuple) else (account, True)
        self._path, self._indexes, self._derivations = normalize_derivation(path=(
            f"m/{index_tuple_to_string(index=self._purpose)}/"
            f"{index_tuple_to_string(index=self._coin_type)}/"
            f"{index_tuple_to_string(index=self._account)}/"
            f"{index_tuple_to_string(index=self._change)}/"
            f"{index_tuple_to_string(index=self._address)}"
        ))
        return self

    def from_change(self, change: str) -> "BIP44Derivation":
        self._change = (self.changes[change], False)
        self._path, self._indexes, self._derivations = normalize_derivation(path=(
            f"m/{index_tuple_to_string(index=self._purpose)}/"
            f"{index_tuple_to_string(index=self._coin_type)}/"
            f"{index_tuple_to_string(index=self._account)}/"
            f"{index_tuple_to_string(index=self._change)}/"
            f"{index_tuple_to_string(index=self._address)}"
        ))
        return self

    def from_address(self, address: Union[int, Tuple[int, int]]) -> "BIP44Derivation":
        self._address = (*address, False) if isinstance(address, tuple) else (address, False)
        self._path, self._indexes, self._derivations = normalize_derivation(path=(
            f"m/{index_tuple_to_string(index=self._purpose)}/"
            f"{index_tuple_to_string(index=self._coin_type)}/"
            f"{index_tuple_to_string(index=self._account)}/"
            f"{index_tuple_to_string(index=self._change)}/"
            f"{index_tuple_to_string(index=self._address)}"
        ))
        return self

    def clean(self) -> "BIP44Derivation":
        self._account = (0, True)
        self._change = (self.changes["external-chain"], False)
        self._address = (0, False)
        self._path, self._indexes, self._derivations = normalize_derivation(path=(
            f"m/{index_tuple_to_string(index=self._purpose)}/"
            f"{index_tuple_to_string(index=self._coin_type)}/"
            f"{index_tuple_to_string(index=self._account)}/"
            f"{index_tuple_to_string(index=self._change)}/"
            f"{index_tuple_to_string(index=self._address)}"
        ))
        return self

    def purpose(self) -> int:
        return self._purpose[0]

    def coin_type(self) -> int:
        return self._coin_type[0]

    def account(self) -> int:
        return (
            self._account[1] if len(self._account) == 3 else self._account[0]
        )

    def change(self) -> Optional[None]:
        _change: Optional[str] = None
        for key, value in self.changes.items():
            if value == self._change[0]:
                _change = key
                break
        return _change

    def address(self) -> int:
        return (
            self._address[1] if len(self._address) == 3 else self._address[0]
        )
