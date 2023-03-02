#!/usr/bin/env python3
'''Password Encryption'''

import bcrypt


def hash_password(password: str) -> bytes:
    '''Password generation'''
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
