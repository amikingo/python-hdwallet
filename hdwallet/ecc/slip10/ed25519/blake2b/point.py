#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from ..point import SLIP10Ed25519Point


class SLIP10Ed25519Blake2bPoint(SLIP10Ed25519Point):

    @staticmethod
    def name() -> str:
        return "SLIP10-Ed25519-Blake2b"
