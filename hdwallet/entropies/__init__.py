#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from typing import (
    List, Dict, Type
)

from .ientropy import IEntropy
from .algorand import (
    AlgorandEntropy, ALGORAND_ENTROPY_STRENGTHS
)
from .bip39 import (
    BIP39Entropy, BIP39_ENTROPY_STRENGTHS
)
from .electrum import (
    ElectrumV1Entropy, ELECTRUM_V1_ENTROPY_STRENGTHS,
    ElectrumV2Entropy, ELECTRUM_V2_ENTROPY_STRENGTHS
)
from .monero import (
    MoneroEntropy, MONERO_ENTROPY_STRENGTHS
)

ENTROPIES: Dict[str, Type[IEntropy]] = {
    AlgorandEntropy.name(): AlgorandEntropy,
    BIP39Entropy.name(): BIP39Entropy,
    ElectrumV1Entropy.name(): ElectrumV1Entropy,
    ElectrumV2Entropy.name(): ElectrumV2Entropy,
    MoneroEntropy.name(): MoneroEntropy
}

__all__: List[str] = [
    "IEntropy",
    "ALGORAND_ENTROPY_STRENGTHS",
    "BIP39_ENTROPY_STRENGTHS",
    "ELECTRUM_V1_ENTROPY_STRENGTHS",
    "ELECTRUM_V2_ENTROPY_STRENGTHS",
    "MONERO_ENTROPY_STRENGTHS",
    "ENTROPIES"
] + [
    entropy.__name__ for entropy in ENTROPIES.values()
]
