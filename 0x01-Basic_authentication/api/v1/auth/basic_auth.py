#!/usr/bin/env python3
'''BasicAuth class'''
import re
from .auth import Auth


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
