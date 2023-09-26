#!/usr/bin/env python3

from typing import (
    Any, Union
)

from ..libs.base32 import (
    encode_no_padding, decode
)
from ..ecc import (
    IPublicKey, SLIP10Ed25519PublicKey
)
from ..crypto import sha512_256
from ..utils import (
    get_bytes, bytes_to_string
)
from . import (
    IAddress, validate_and_get_public_key
)


class AlgorandAddress(IAddress):

    checksum_length: int = 4

    @staticmethod
    def compute_checksum(public_key: bytes) -> bytes:
        return sha512_256(public_key)[-1 * 4:]

    @classmethod
    def encode(cls, public_key: Union[bytes, str, IPublicKey], **kwargs: Any) -> str:

        public_key: SLIP10Ed25519PublicKey = validate_and_get_public_key(
            public_key=public_key, public_key_cls=SLIP10Ed25519PublicKey
        )
        return encode_no_padding(bytes_to_string(
            public_key.raw_compressed()[1:] + cls.compute_checksum(public_key.raw_compressed()[1:])
        ))

    @classmethod
    def decode(cls, address: str, **kwargs: Any) -> str:

        address_decode: bytes = get_bytes(decode(address))

        expected_length: int = (
            SLIP10Ed25519PublicKey.compressed_length() + cls.checksum_length - 1
        )
        if len(address_decode) != expected_length:
            raise ValueError(f"Invalid length (expected: {expected_length}, got: {len(address_decode)})")

        checksum: bytes = address_decode[-1 * cls.checksum_length:]
        public_key: bytes = address_decode[:-1 * cls.checksum_length]

        checksum_got: bytes = cls.compute_checksum(public_key)
        if checksum != checksum_got:
            raise ValueError(f"Invalid checksum (expected: {checksum.hex()}, got: {checksum_got.hex()})")

        if not SLIP10Ed25519PublicKey.is_valid_bytes(public_key):
            raise ValueError(f"Invalid {SLIP10Ed25519PublicKey.curve_type()} public key {public_key.hex()}")

        return bytes_to_string(public_key)
