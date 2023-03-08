#!/usr/bin/env python3
'''BasicAuth class'''
import re
import base64
from .auth import Auth
from typing import TypeVar


class BasicAuth(Auth):
    '''Implementation of Basic Authorization'''

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        '''Returning the Base64 part of the Authorization header'''
        if type(authorization_header) == str:
            pattern = r'Basic (?P<token>.+)'
            field_match = re.fullmatch(pattern, authorization_header.strip())
            if field_match is not None:
                return field_match.group('token')
        return None
        token = authorization_header.split(" ")[-1]
        return token

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """
        Decode a Base64-encoded string
        """
        if base64_authorization_header is None or \
           type(base64_authorization_header) != str:
            return None

        try:
            return base64.b64decode(base64_authorization_header).\
                decode('utf-8')
        except Exception:
            return None
