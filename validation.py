import hashlib

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
