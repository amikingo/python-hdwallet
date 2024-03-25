#!/usr/bin/env python3

from hdwallet.entropies.bip39 import (
    BIP39Entropy, BIP39_ENTROPY_STRENGTHS
)
from hdwallet.mnemonics.bip39 import (
    BIP39Mnemonic, BIP39_MNEMONIC_LANGUAGES
)
from hdwallet.seeds.bip39 import BIP39Seed
from hdwallet.cryptocurrencies import Bitcoin as Cryptocurrency
from hdwallet.derivations import BIP44Derivation
from hdwallet.hds import BIP44HD


# Generate BIP39 entropy
entropy: str = BIP39Entropy.generate(
    strength=BIP39_ENTROPY_STRENGTHS.ONE_HUNDRED_TWENTY_EIGHT
)
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

# Initialize BIP44 HD
bip44_hd: BIP44HD = BIP44HD(
    ecc=Cryptocurrency.ECC, coin_type=Cryptocurrency.COIN_TYPE, account=0, change="external-chain", address=0
)
# Update BIP44 HD root keys from seed
bip44_hd.from_seed(
    seed=bip39_seed
)

# Dump root keys
print("BIP44 Root XPrivate Key:", bip44_hd.root_xprivate_key())
print("BIP44 Root XPublic Key:", bip44_hd.root_xpublic_key())
print("BIP44 Root Private Key:", bip44_hd.root_private_key())
print("BIP44 Root Chain Code:", bip44_hd.root_chain_code())
print("BIP44 Root Public Key:", bip44_hd.root_public_key())

# Initialize BIP44 derivation
bip44_derivation: BIP44Derivation = BIP44Derivation(
    coin_type=Cryptocurrency.COIN_TYPE
)
bip44_derivation.from_account(account=0)
bip44_derivation.from_change(change="internal-chain")
bip44_derivation.from_address(address=0)

# Update current BIP44 HD derivation
bip44_hd.from_derivation(
    derivation=bip44_derivation
)
# Or update current BIP44 HD derivation by changing indexes
# bip44_hd.from_coin_type(coin_type=Cryptocurrency.COIN_TYPE)
# bip44_hd.from_account(account=0)
# bip44_hd.from_change(change="internal-chain")
# bip44_hd.from_address(address=0)

# Dump derived keys
print("BIP44 XPrivate Key:", bip44_hd.xprivate_key())
print("BIP44 XPublic Key:", bip44_hd.xpublic_key())
print("BIP44 Private Key:", bip44_hd.private_key())
print("BIP44 WIF:", bip44_hd.wif())
print("BIP44 Chain Code:", bip44_hd.chain_code())
print("BIP44 Public Key:", bip44_hd.public_key())
print("BIP44 Uncompressed:", bip44_hd.uncompressed())
print("BIP44 Compressed:", bip44_hd.compressed())
print("BIP44 Hash:", bip44_hd.hash())
print("BIP44 Depth:", bip44_hd.depth())
print("BIP44 Path:", bip44_hd.path())
print("BIP44 Index:", bip44_hd.index())
print("BIP44 Indexes:", bip44_hd.indexes())
print("BIP44 Fingerprint:", bip44_hd.fingerprint())
print("BIP44 Parent Fingerprint:", bip44_hd.parent_fingerprint())
print("BIP44 Address:", bip44_hd.address(
    public_key_address_prefix=Cryptocurrency.NETWORKS.MAINNET.PUBLIC_KEY_ADDRESS_PREFIX
))