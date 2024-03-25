#!/usr/bin/env python3

from hdwallet.entropies.bip39 import (
    BIP39Entropy, BIP39_ENTROPY_STRENGTHS
)
from hdwallet.mnemonics.bip39 import (
    BIP39Mnemonic, BIP39_MNEMONIC_LANGUAGES
)
from hdwallet.seeds.bip39 import BIP39Seed
from hdwallet.cryptocurrencies import Bitcoin as Cryptocurrency
from hdwallet.derivations import CustomDerivation
from hdwallet.hds import BIP141HD


# Generate BIP39 entropy
# entropy: str = BIP39Entropy.generate(
#     strength=BIP39_ENTROPY_STRENGTHS.ONE_HUNDRED_TWENTY_EIGHT
# )
entropy: str = "36482302a3b8a1a9dfdd2911bc5eb4c2"
bip39_entropy: BIP39Entropy = BIP39Entropy(entropy=entropy)
print(f"BIP39 Entropy {bip39_entropy.entropy()}")
print(f"BIP39 Strength {bip39_entropy.strength()}")

# Get BIP39 mnemonic from entropy
mnemonic: str = BIP39Mnemonic.from_entropy(
    entropy=bip39_entropy, language=BIP39_MNEMONIC_LANGUAGES.JAPANESE
)
bip39_mnemonic: BIP39Mnemonic = BIP39Mnemonic(mnemonic=mnemonic)
print(f"BIP39 Mnemonic {bip39_mnemonic.mnemonic()}")
print(f"BIP39 Language {bip39_mnemonic.language()}")
print(f"BIP39 Word {bip39_mnemonic.word()}")

# Generate BIP39 Seed from mnemonic
seed: str = BIP39Seed.generate(
    mnemonic=bip39_mnemonic.mnemonic(), passphrase=None
)
bip39_seed: BIP39Seed = BIP39Seed(seed=seed)
print(f"BIP39 Seed {bip39_seed.seed()}")

# Initialize BIP141 HD
bip141_hd: BIP141HD = BIP141HD(
    ecc=Cryptocurrency.ECC, semantic="P2WPKH"
)
# Update BIP141 HD root keys from seed
bip141_hd.from_seed(
    seed=bip39_seed
)

# bip141_hd.from_semantic(semantic="P2WPKH-In-P2SH")
# bip141_hd.from_semantic(semantic="P2WSH")
# bip141_hd.from_semantic(semantic="P2WSH-In-P2SH")

# Dump root keys
print("BIP141 Semantic:", bip141_hd.semantic())
print("BIP141 Root XPrivate Key:", bip141_hd.root_xprivate_key())
print("BIP141 Root XPublic Key:", bip141_hd.root_xpublic_key())
print("BIP141 Root Private Key:", bip141_hd.root_private_key())
print("BIP141 Root Chain Code:", bip141_hd.root_chain_code())
print("BIP141 Root Public Key:", bip141_hd.root_public_key())

# Initialize Custom derivation
custom_derivation: CustomDerivation = CustomDerivation(
    path="m/49'/0'/0'/0/0"
)

# Update current BIP141 HD derivation
bip141_hd.from_derivation(
    derivation=custom_derivation
)

# Dump derived keys
print("BIP141 XPrivate Key:", bip141_hd.xprivate_key())
print("BIP141 XPublic Key:", bip141_hd.xpublic_key())
print("BIP141 Private Key:", bip141_hd.private_key())
print("BIP141 WIF:", bip141_hd.wif())
print("BIP141 Chain Code:", bip141_hd.chain_code())
print("BIP141 Public Key:", bip141_hd.public_key())
print("BIP141 Uncompressed:", bip141_hd.uncompressed())
print("BIP141 Compressed:", bip141_hd.compressed())
print("BIP141 Hash:", bip141_hd.hash())
print("BIP141 Depth:", bip141_hd.depth())
print("BIP141 Path:", bip141_hd.path())
print("BIP141 Index:", bip141_hd.index())
print("BIP141 Indexes:", bip141_hd.indexes())
print("BIP141 Fingerprint:", bip141_hd.fingerprint())
print("BIP141 Parent Fingerprint:", bip141_hd.parent_fingerprint())
print("BIP141 Address:", bip141_hd.address(
    script_address_prefix=Cryptocurrency.NETWORKS.MAINNET.SCRIPT_ADDRESS_PREFIX,
    hrp=Cryptocurrency.NETWORKS.MAINNET.HRP,
    witness_version=Cryptocurrency.NETWORKS.MAINNET.WITNESS_VERSIONS.P2WSH
))