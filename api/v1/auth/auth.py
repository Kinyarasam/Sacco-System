#!/usr/bin/env python3
""" Definition of class Auth
"""

import os
import typing


class Auth:
    """ Manages the API authentication
    """

    def require_auth(self, path: str, excluded_paths: typing.List[str]) -> bool:
        """ Determines whether a given path requires authentication or not

        Args:
            path (str): URL path to be checked.
            excluded_paths (List): List of paths that do not require authentication.

        Returns:
            True if path is not in excluded_paths, else False
        """
        if path is None:
            return True

        if excluded_paths is None or excluded_paths == []:
            return True

        if path in excluded_paths:
            return False

        for i in excluded_paths:
            if i.startswith(path) or path.startswith(i):
                return False

            if i[-1] == '*':
                if path.startswith(i[:-1]):
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Returns the authorization header from a request object
        """
        if request is None:
            return
        header = request.headers.get('Authorization')
        if header is None:
            return None

        return header

    def current_user(self, request=None) -> typing.TypeVar('User'):
        """ Returns a User instance from information from a request object
        """
        return None

    def session_cookie(self, request=None):
        """Returns a cookie from a request.
        Args:
            request: request object
        Returns:
            value of _my_session_id cookiefrom request object
        """
        if request is None:
            return None

        session_name = os.getenv('SESSION_NAME')
        return request.cookies.get(session_name)
