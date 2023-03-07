#!/usr/bin/env python3
'''Auth class'''
from flask import request
from typing import (List, TypeVar)


class Auth:
    '''API authentication'''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''Determining whether a given path requires authentication or not'''
        if path is None:
            return True
        if excluded_paths is None:
            return True
        path = path + '/' if path[-1] != '/' else path
        if path not in excluded_paths:
            return True
        else:
            return False

    def authorization_header(self, request=None) -> str:
        '''Returning the authorization header from a request object'''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''Returning a User instance info from a request object'''
        return None
