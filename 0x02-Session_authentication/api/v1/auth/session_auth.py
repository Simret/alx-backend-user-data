#!/usr/bin/env python3
"""SessionAuth"""
from typing import Dict
from .auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """Implementing Session Authorization"""
    user_id_by_session_id: Dict[str, str] = {}

    def create_session(self, user_id: str = None) -> str:
        """creating a session id for a user_id"""
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        return session_id
