import hashlib
import os
from typing import Union

# from dotenv import load_dotenv

# load_dotenv("/Users/gcarruthers/2020fa-pset-1-GCarruthers/environment.env")


def get_csci_salt() -> bytes:
    """Returns the appropriate salt for CSCI E-29
    :return: bytes representation of the CSCI salt
    """
    # Hint: use os.environment and bytes.fromhex
    csci = os.environ["CSCI_SALT"]

    return bytes.fromhex(csci)


def hash_str(some_val: Union[str, bytes], salt: Union[str, bytes] = "") -> bytes:
    """Converts strings to hash digest
    See: https://en.wikipedia.org/wiki/Salt_(cryptography)
    :param some_val: thing to hash, can be str or bytes
    :param salt: Add randomness to the hashing, can be str or bytes
    :return: sha256 hash digest of some_val with salt, type bytes
    """

    try:
        # make sure data type is bytes and if not encode to bytes
        if type(salt) != bytes:
            salt = salt.encode()
        if type(some_val) != bytes:
            some_val = some_val.encode()

        # return encoded value
        return hashlib.sha256(salt + some_val).digest()
    except TypeError:
        raise TypeError("Inputs need to be either strings or bytes.")


def get_user_id(username: str) -> str:
    salt = get_csci_salt()
    return hash_str(username.lower(), salt=salt).hex()[:8]
