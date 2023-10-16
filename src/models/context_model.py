"""Context Model"""

# General Imports
from pydantic import BaseModel


class Context(BaseModel):
    """Class for context model"""

    client_id: str
    user_id: str

    def get_client_id(self):
        """Function to return client id"""
        return self.client_id


    def get_user_id(self):
        """Function to return user id"""
        return self.user_id
