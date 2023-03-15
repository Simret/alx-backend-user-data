#!/usr/bin/env python3
"""Auth Class for user attributes validation
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from db import DB
from user import User
import bcrypt


def _hash_password(password: str) -> str:
    """Takes in password string argument
    Returns bytes
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
