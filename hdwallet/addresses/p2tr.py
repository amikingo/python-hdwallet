#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from typing import (
    Any, Union
)

from ..libs.segwit_bech32 import (
    segwit_encode, segwit_decode
)
from ..ecc import (
    IPoint, IPublicKey, SLIP10Secp256k1ECC, SLIP10Secp256k1Point, SLIP10Secp256k1PublicKey, validate_and_get_public_key
)
from ..crypto import sha256
from ..utils import (
    get_bytes, integer_to_bytes, bytes_to_integer, bytes_to_string
)
from .iaddress import IAddress


class P2TRAddress(IAddress):
    
    hrp: str = "bc"
    field_size: int = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
    tap_tweak_sha256: bytes = get_bytes(
        "e80fe1639c9ca050e3af1b39c143c63e429cbceb15d940fbb5c5a1f4af57c5e9"
    )
    witness_version: int = 1

    @staticmethod
    def name() -> str:
        return "P2TR"

    @classmethod
    def tagged_hash(cls, tag: Union[bytes, str], data_bytes: bytes) -> bytes:
        tag_hash = sha256(tag) if isinstance(tag, str) else tag
        return sha256(tag_hash + tag_hash + data_bytes)

    @classmethod
    def hash_tap_tweak(cls, pub_key: IPublicKey) -> bytes:
        return cls.tagged_hash(cls.tap_tweak_sha256, integer_to_bytes(pub_key.point().x()))

    @classmethod
    def lift_x(cls, pub_key: IPublicKey) -> IPoint:
        p = cls.field_size
        x = pub_key.point().x()
        if x >= p:
            raise ValueError("Unable to compute LiftX point")
        c = (pow(x, 3, p) + 7) % p
        y = pow(c, (p + 1) // 4, p)
        if c != pow(y, 2, p):
            raise ValueError("Unable to compute LiftX point")
        return SLIP10Secp256k1Point.from_coordinates(
            x, y if y % 2 == 0 else p - y
        )

    @classmethod
    def tweak_public_key(cls, pub_key: IPublicKey) -> bytes:
        h = cls.hash_tap_tweak(pub_key)
        out_point = cls.lift_x(pub_key) + (bytes_to_integer(h) * SLIP10Secp256k1ECC.GENERATOR)
        return integer_to_bytes(out_point.x())

    @classmethod
    def encode(cls, public_key: Union[bytes, str, IPublicKey], **kwargs: Any) -> str:

        public_key: IPublicKey = validate_and_get_public_key(
            public_key=public_key, public_key_cls=SLIP10Secp256k1PublicKey
        )
        return segwit_encode(
            kwargs.get("hrp", cls.hrp),
            kwargs.get("witness_version", cls.witness_version),
            cls.tweak_public_key(public_key)
        )

    @classmethod
    def decode(cls, address: str, **kwargs: Any) -> str:

        witness_version, address_decode = segwit_decode(
            kwargs.get("hrp", cls.hrp), address
        )

        expected_length: int = SLIP10Secp256k1PublicKey.compressed_length() - 1
        if len(address_decode) != expected_length:
            raise ValueError(f"Invalid length (expected: {expected_length}, got: {len(address_decode)})")
        if witness_version != cls.witness_version:
            raise ValueError(f"Invalid witness version (expected: {cls.witness_version}, got: {witness_version})")

        return bytes_to_string(address_decode)