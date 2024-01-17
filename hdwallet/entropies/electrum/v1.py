#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from typing import List

from ..ientropy import IEntropy


class ELECTRUM_V1_ENTROPY_STRENGTHS:

    ONE_HUNDRED_TWENTY_EIGHT: int = 128


class ElectrumV1Entropy(IEntropy):

    _name = "Electrum-V1"

    strengths = [
        ELECTRUM_V1_ENTROPY_STRENGTHS.ONE_HUNDRED_TWENTY_EIGHT
    ]