#!/usr/bin/env python3
"""Basic Auth module
"""
from .auth import Auth
from base64 import b64decode
from models.user import User


class BasicAuth(Auth):
    """Implement Basic Authorization protocol methods
    """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Extracts the Base64 part of the Base64 part of the Authorization header for a Basic Authorization
        """
        if authorization_header is None or not isinstance(authorization_header, str):
            return None
        
        prefix = "Basic "
        if not authorization_header.startswith(prefix):
            return None
        
        return authorization_header[len(prefix):]
    
    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """Decode a base64 encoded string
        """
        if base64_authorization_header is None:
            return None
        
        if not isinstance(base64_authorization_header, str):
            return None
        
        try:
            b64_byte_string = base64_authorization_header.encode("utf-8")
            b64_decoded_string = b64decode(b64_byte_string)
            return b64_decoded_string.decode("utf-8")
        except Exception as e:
            return None
        
    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> tuple[str, str]:
        """Returns user email and password from base64 decoded value
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        
        delimeter = ":"
        if delimeter not in decoded_base64_authorization_header:
            return (None, None)
        user_credentials = decoded_base64_authorization_header.split(delimeter)
        user_email = user_credentials[0]
        user_pwd = delimeter.join(user_credentials[1:])
        return (user_email, user_pwd)
    
    def user_object_from_credentials(self, user_email, user_pwd) -> User:
        """Return a user instance based on the email and password
        """
        if user_email is None or user_pwd is None:
            return None
        
        if not isinstance(user_email, str):
            return None
        
        if not isinstance(user_pwd, str):
            return None
        
        user = User.find(email=user_email, password=user_pwd)
        if not user:
            return None
        return user
    
    def current_user(self, request=None) -> User:
        """Returns a user instance based on the received request
        """
        authorization_header = self.authorization_header(request)
        if authorization_header is not None:
            base64_authorization_header = self.extract_base64_authorization_header(authorization_header)
            if base64_authorization_header is not None:
                decoded_base64_authorization_header = self.decode_base64_authorization_header(base64_authorization_header)
                if decoded_base64_authorization_header is not None:
                    user_credentials = self.extract_user_credentials(decoded_base64_authorization_header)
                    if user_credentials[0] is not None:
                        user_email = user_credentials[0]
                        user_pwd = user_credentials[1]
                        return self.user_object_from_credentials(user_email, user_pwd)
        return None