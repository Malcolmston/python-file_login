import hashlib
import re

def hide_password(password = None, salt = ''):
    '''
    using hashlib this function will hash a password

    Inputs:
        password (str | None): a user's password'
        salt (str): for admin users to be able to salt their pasword
    Returns:
        hashed-password (str | None): a user's hashed password'

    '''
        # Encoding the password
    hashed = hashlib.sha256((salt + password).encode())

    return str( hashed.hexdigest() )


def is_valid_Email(email = None):
    # thnks to https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/# for reqex
    regex = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"

    return bool(re.fullmatch(regex, email))


def is_valid_Password(password = None):
    regex = r"([A-Z]{1,9})+([a-z]{7,19})+([0-9]{2,7})"

    return bool(re.fullmatch(regex, password))

