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
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returning session id"""
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id, None)
