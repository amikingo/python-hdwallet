#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from typing import (
    Union, Dict, List
)

import unicodedata

from ...utils import (
    get_bytes, bytes_to_string, bytes_to_integer
)
from ...crypto import crc32
from ...entropies import (
    IEntropy, MoneroEntropy, MONERO_ENTROPY_STRENGTHS
)
from ...utils import bytes_chunk_to_words, words_to_bytes_chunk
from ..imnemonic import IMnemonic


class MONERO_MNEMONIC_WORDS:

    TWELVE: int = 12
    THIRTEEN: int = 13
    TWENTY_FOUR: int = 24
    TWENTY_FIVE: int = 25


class MONERO_MNEMONIC_LANGUAGES:

    CHINESE_SIMPLIFIED: str = "chinese-simplified"
    DUTCH: str = "dutch"
    ENGLISH: str = "english"
    FRENCH: str = "french"
    GERMAN: str = "german"
    ITALIAN: str = "italian"
    JAPANESE: str = "japanese"
    PORTUGUESE: str = "portuguese"
    RUSSIAN: str = "russian"
    SPANISH: str = "spanish"


class MoneroMnemonic(IMnemonic):

    word_bit_length: int = 11
    words_list_number: int = 1626
    words: List[int] = [
        MONERO_MNEMONIC_WORDS.TWELVE,
        MONERO_MNEMONIC_WORDS.THIRTEEN,
        MONERO_MNEMONIC_WORDS.TWENTY_FOUR,
        MONERO_MNEMONIC_WORDS.TWENTY_FIVE
    ]
    words_checksum: List[int] = [
        MONERO_MNEMONIC_WORDS.THIRTEEN,
        MONERO_MNEMONIC_WORDS.TWENTY_FIVE
    ]
    words_to_entropy_strength: Dict[int, int] = {
        MONERO_MNEMONIC_WORDS.TWELVE: MONERO_ENTROPY_STRENGTHS.ONE_HUNDRED_TWENTY_EIGHT,
        MONERO_MNEMONIC_WORDS.THIRTEEN: MONERO_ENTROPY_STRENGTHS.ONE_HUNDRED_TWENTY_EIGHT,
        MONERO_MNEMONIC_WORDS.TWENTY_FOUR: MONERO_ENTROPY_STRENGTHS.TWO_HUNDRED_FIFTY_SIX,
        MONERO_MNEMONIC_WORDS.TWENTY_FIVE: MONERO_ENTROPY_STRENGTHS.TWO_HUNDRED_FIFTY_SIX
    }
    languages: List[str] = [
        MONERO_MNEMONIC_LANGUAGES.CHINESE_SIMPLIFIED,
        MONERO_MNEMONIC_LANGUAGES.DUTCH,
        MONERO_MNEMONIC_LANGUAGES.ENGLISH,
        MONERO_MNEMONIC_LANGUAGES.FRENCH,
        MONERO_MNEMONIC_LANGUAGES.GERMAN,
        MONERO_MNEMONIC_LANGUAGES.ITALIAN,
        MONERO_MNEMONIC_LANGUAGES.JAPANESE,
        MONERO_MNEMONIC_LANGUAGES.PORTUGUESE,
        MONERO_MNEMONIC_LANGUAGES.RUSSIAN,
        MONERO_MNEMONIC_LANGUAGES.SPANISH
    ]
    language_unique_prefix_lengths: Dict[str, int] = {
        MONERO_MNEMONIC_LANGUAGES.CHINESE_SIMPLIFIED: 1,
        MONERO_MNEMONIC_LANGUAGES.DUTCH: 4,
        MONERO_MNEMONIC_LANGUAGES.ENGLISH: 3,
        MONERO_MNEMONIC_LANGUAGES.FRENCH: 4,
        MONERO_MNEMONIC_LANGUAGES.GERMAN: 4,
        MONERO_MNEMONIC_LANGUAGES.ITALIAN: 4,
        MONERO_MNEMONIC_LANGUAGES.JAPANESE: 4,
        MONERO_MNEMONIC_LANGUAGES.PORTUGUESE: 4,
        MONERO_MNEMONIC_LANGUAGES.SPANISH: 4,
        MONERO_MNEMONIC_LANGUAGES.RUSSIAN: 4
    }
    wordlist_path: Dict[str, str] = {
        MONERO_MNEMONIC_LANGUAGES.CHINESE_SIMPLIFIED: "monero/wordlist/chinese_simplified.txt",
        MONERO_MNEMONIC_LANGUAGES.DUTCH: "monero/wordlist/dutch.txt",
        MONERO_MNEMONIC_LANGUAGES.ENGLISH: "monero/wordlist/english.txt",
        MONERO_MNEMONIC_LANGUAGES.FRENCH: "monero/wordlist/french.txt",
        MONERO_MNEMONIC_LANGUAGES.GERMAN: "monero/wordlist/german.txt",
        MONERO_MNEMONIC_LANGUAGES.ITALIAN: "monero/wordlist/italian.txt",
        MONERO_MNEMONIC_LANGUAGES.JAPANESE: "monero/wordlist/japanese.txt",
        MONERO_MNEMONIC_LANGUAGES.PORTUGUESE: "monero/wordlist/portuguese.txt",
        MONERO_MNEMONIC_LANGUAGES.RUSSIAN: "monero/wordlist/russian.txt",
        MONERO_MNEMONIC_LANGUAGES.SPANISH: "monero/wordlist/spanish.txt"
    }

    @classmethod
    def name(cls) -> str:
        return "Monero"

    @classmethod
    def from_words(cls, words: int, language: str, **kwargs) -> str:
        if words not in cls.words:
            raise ValueError(f"Invalid words number for mnemonic (expected {cls.words}, got {words})")

        return cls.from_entropy(
            entropy=MoneroEntropy.generate(cls.words_to_entropy_strength[words]),
            language=language,
            checksum=(
                True if words in cls.words_checksum else False
            )
        )

    @classmethod
    def from_entropy(cls, entropy: Union[str, bytes, IEntropy], language: str, **kwargs) -> str:
        if isinstance(entropy, str) or isinstance(entropy, bytes):
            return cls.encode(
                entropy=entropy, language=language, checksum=kwargs.get("checksum", False)
            )
        elif isinstance(entropy, MoneroEntropy):
            return cls.encode(
                entropy=entropy.entropy(), language=language, checksum=kwargs.get("checksum", False)
            )
        raise Exception("Invalid entropy, only accept str, bytes, or Monero entropy class")

    @classmethod
    def encode(cls, entropy: Union[str, bytes], language: str, checksum: bool = False) -> str:

        entropy: bytes = get_bytes(entropy)
        if not MoneroEntropy.is_valid_bytes_strength(len(entropy)):
            raise ValueError(f"Wrong entropy length (expected {MoneroEntropy.strengths}, got {len(entropy) * 8})")

        mnemonic: List[str] = []
        words_list: List[str] = cls.get_words_list_by_language(language=language)
        if len(words_list) != cls.words_list_number:
            raise ValueError(f"Invalid number of loaded words list (expected {cls.words_list_number}, got {len(words_list)})")

        for index in range(len(get_bytes(entropy)) // 4):
            mnemonic += bytes_chunk_to_words(
                entropy[index * 4:(index * 4) + 4], words_list, "little"
            )

        if checksum:
            unique_prefix_length = cls.language_unique_prefix_lengths[language]
            prefixes = "".join(word[:unique_prefix_length] for word in mnemonic)
            checksum_word = mnemonic[
                bytes_to_integer(crc32(prefixes)) % len(mnemonic)
            ]
            mnemonic = mnemonic + [checksum_word]

        return " ".join(cls.normalize(mnemonic))

    @classmethod
    def decode(cls, mnemonic: str) -> str:
        words: list = cls.normalize(mnemonic)
        if len(words) not in cls.words:
            raise ValueError(f"Invalid mnemonic words count (expected {cls.words}, got {len(words)})")

        words_list, language = cls.find_language(mnemonic=words)
        if len(words_list) != cls.words_list_number:
            raise ValueError(f"Invalid number of loaded words list (expected {cls.words_list_number}, got {len(words_list)})")

        if len(words) in cls.words_checksum:
            mnemonic: list = words[:-1]
            unique_prefix_length = cls.language_unique_prefix_lengths[language]
            prefixes = "".join(word[:unique_prefix_length] for word in mnemonic)
            checksum_word = mnemonic[
                bytes_to_integer(crc32(prefixes)) % len(mnemonic)
            ]
            if words[-1] != checksum_word:
                raise ValueError(f"Invalid checksum (expected {checksum_word}, got {words[-1]})")

        entropy: bytes = b""
        for index in range(len(words) // 3):
            word_1, word_2, word_3 = words[index * 3:(index * 3) + 3]
            entropy += words_to_bytes_chunk(
                word_1, word_2, word_3, words_list, "little"
            )
        return bytes_to_string(entropy)

    @classmethod
    def normalize(cls, mnemonic: Union[str, List[str]]) -> List[str]:
        mnemonic: list = mnemonic.split() if isinstance(mnemonic, str) else mnemonic
        return list(map(lambda _: unicodedata.normalize("NFKD", _.lower()), mnemonic))
