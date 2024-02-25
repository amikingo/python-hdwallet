#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from typing import (
    Any, Union
)

from ..libs.base58 import ensure_string
from ..libs.segwit_bech32 import (
    segwit_encode, segwit_decode
)
from ..const import PUBLIC_KEY_TYPES
from ..ecc import (
    IPublicKey, SLIP10Secp256k1PublicKey, validate_and_get_public_key
)
from ..crypto import hash160
from ..utils import bytes_to_string
from .iaddress import IAddress


class P2WPKHAddress(IAddress):
    
    hrp: str = "bc"
    witness_version: int = 0

    @staticmethod
    def name() -> str:
        return "P2WPKH"

    @classmethod
    def encode(cls, public_key: Union[bytes, str, IPublicKey], **kwargs: Any) -> str:

        public_key: IPublicKey = validate_and_get_public_key(
            public_key=public_key, public_key_cls=SLIP10Secp256k1PublicKey
        )
        public_key_hash: bytes = hash160(
            public_key.raw_compressed()
            if kwargs.get("public_key_type", PUBLIC_KEY_TYPES.COMPRESSED) == PUBLIC_KEY_TYPES.COMPRESSED else
            public_key.raw_uncompressed()
        )
        return ensure_string(segwit_encode(
            kwargs.get("hrp", cls.hrp),
            kwargs.get("witness_version", cls.witness_version),
            public_key_hash
        ))

    @classmethod
    def decode(cls, address: str, **kwargs: Any) -> str:

        witness_version, address_decode = segwit_decode(
            kwargs.get("hrp", cls.hrp), address
        )
        return bytes_to_string(address_decode)