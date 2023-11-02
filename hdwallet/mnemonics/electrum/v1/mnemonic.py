#!/usr/bin/env python3

# Copyright © 2020-2023, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from typing import (
    Dict, List, Union, Optional
)

import unicodedata

from ....utils import (
    get_bytes, integer_to_bytes, bytes_to_integer, bytes_to_string
)
from ....entropys.electrum.v1 import (
    ElectrumV1Entropy, ELECTRUM_V1_ENTROPY_LENGTHS
)
from ...imnemonic import IMnemonic


class ELECTRUM_V1_MNEMONIC_WORDS:

    TWELVE: int = 12


class ELECTRUM_V1_MNEMONIC_LANGUAGES:

    ENGLISH: str = "english"


class ElectrumV1Mnemonic(IMnemonic):

    words: List[int] = [
        ELECTRUM_V1_MNEMONIC_WORDS.TWELVE
    ]
    words_to_entropy_length: Dict[int, int] = {
        ELECTRUM_V1_MNEMONIC_WORDS.TWELVE: ELECTRUM_V1_ENTROPY_LENGTHS.ONE_HUNDRED_TWENTY_EIGHT
    }
    languages: List[str] = [
        ELECTRUM_V1_MNEMONIC_LANGUAGES.ENGLISH
    ]
    wordlist_path: Dict[str, str] = {
        ELECTRUM_V1_MNEMONIC_LANGUAGES.ENGLISH: "electrum/v1/wordlist/english.txt"
    }
    words_list_number: int = 1626

    @classmethod
    def from_words(cls, words: int, language: str) -> str:
        if words not in cls.words:
            raise ValueError(f"Invalid words number for mnemonic (expected {cls.words}, got {words})")

        return cls.from_entropy(
            entropy=ElectrumV1Entropy.generate(cls.words_to_entropy_length[words]), language=language
        )

    @classmethod
    def from_entropy(cls, entropy: Union[str, bytes], language: str) -> str:
        return cls.encode(entropy=entropy, language=language)

    @classmethod
    def encode(cls, entropy: Union[str, bytes], language: str) -> str:
        # Check entropy length
        entropy: bytes = get_bytes(entropy)
        if not ElectrumV1Entropy.is_valid_bytes_length(len(entropy)):
            raise ValueError(f"Wrong entropy length (expected {ElectrumV1Entropy.lengths}, got {len(entropy) * 8})")

        mnemonic: List[str] = []
        words_list: List[str] = cls.get_words_list_by_language(language=language)
        for index in range(len(entropy) // 4):

            chunk: int = bytes_to_integer(
                entropy[index * 4:(index * 4) + 4], endianness="big"
            )
            word_1_index: int = chunk % len(words_list)
            word_2_index: int = (
                ((chunk // len(words_list)) + word_1_index) % len(words_list)
            )
            word_3_index: int = (
                ((chunk // len(words_list) // len(words_list)) + word_2_index) % len(words_list)
            )
            mnemonic += [
                words_list[word_index] for word_index in (word_1_index, word_2_index, word_3_index)
            ]

        return " ".join(cls.normalize(mnemonic))

    @classmethod
    def decode(cls, mnemonic: str, words_list: Optional[List[str]] = None, words_list_with_index: Optional[dict] = None) -> str:

        # Check mnemonic length
        words: list = cls.normalize(mnemonic)
        if len(words) not in cls.words:
            raise ValueError(f"Invalid mnemonic words count (expected {cls.words}, got {len(words)})")

        if not words_list or not words_list_with_index:
            # Detect language if it was not specified at construction
            words_list, language = cls.find_language(mnemonic=words)
            words_list_with_index: dict = {
                words_list[i]: i for i in range(len(words_list))
            }

        # Consider 3 words at a time, 3 words represent 4 bytes
        entropy: bytes = b""
        for index in range(len(words) // 3):
            word_1, word_2, word_3 = words[index * 3:(index * 3) + 3]

            # Get the word indexes
            word_1_index: int = words_list_with_index[word_1]
            word_2_index: int = words_list_with_index[word_2] % len(words_list)
            word_3_index: int = words_list_with_index[word_3] % len(words_list)

            # Get back the bytes chunk
            chunk: int = (
                word_1_index +
                (len(words_list) * ((word_2_index - word_1_index) % len(words_list))) +
                (len(words_list) * len(words_list) * ((word_3_index - word_2_index) % len(words_list)))
            )
            entropy += integer_to_bytes(chunk, bytes_num=4, endianness="big")

        return bytes_to_string(entropy)

    @classmethod
    def is_valid(
        cls, mnemonic: Union[str, List[str]], words_list: Optional[List[str]] = None, words_list_with_index: Optional[dict] = None
    ) -> bool:
        try:
            cls.decode(mnemonic=mnemonic, words_list=words_list, words_list_with_index=words_list_with_index)
            return True
        except (ValueError, KeyError):
            return False

    @classmethod
    def normalize(cls, mnemonic: Union[str, List[str]]) -> List[str]:
        mnemonic: list = mnemonic.split() if isinstance(mnemonic, str) else mnemonic
        return list(map(lambda _: unicodedata.normalize("NFKD", _.lower()), mnemonic))
