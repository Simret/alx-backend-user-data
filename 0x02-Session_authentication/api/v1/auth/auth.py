#!/usr/bin/env python3
'''Auth class'''
import os
from flask import request
from typing import (List, TypeVar)


class Auth:
    '''API authentication'''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''Determining whether a given path requires authentication or not'''
        if path is None:
            return True
        elif excluded_paths is None or excluded_paths == []:
            return True
        elif path in excluded_paths:
            return False
        else:
            for i in excluded_paths:
                if i.startswith(path):
                    return False
                if path.startswith(i):
                    return False
                if i[-1] == "*":
                    if path.startswith(i[:-1]):
                        return False
        return True

    def authorization_header(self, request=None) -> str:
        '''Returning the authorization header from a request object'''
        if request is None and request.headers.get("Authorization") is None:
            return None
        else:
            return request.headers.get("Authorization")

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''Returning a User instance info from a request object'''
        return None

    def session_cookie(self, request=None):
        """Returns a cookie from a request"""
        if request is None:
            return None
        session_name = os.getenv('SESSION_NAME')
        return request.cookies.get(session_name)
