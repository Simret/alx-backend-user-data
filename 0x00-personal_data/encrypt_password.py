#!/usr/bin/env python3
'''Password Encryption'''

import bcrypt


def hash_password(password: str) -> bytes:
    '''Password generation'''
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''Checking if password matches'''
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
