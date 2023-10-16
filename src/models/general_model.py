"""General Models"""

# General Imports

from sqlalchemy import (Column, String, ForeignKey)

# Custom Imports
from ..database import Base




class Grocery(Base):
    """ Table to store grocery details"""
    __tablename__ = "grocery"

    item_id = Column(String(32), primary_key=True)
    name = Column(String(32))
    price = Column(String(32))
    quantity = Column(String(32))


class OrderItem(Base):
    __tablename__ = "order_item"

    order_id = Column(String(32), primary_key=True)
    item_id = Column(String(32), ForeignKey("grocery.item_id"), primary_key=True)
    quantity = Column(String(32))



class UserOrder(Base):
    __tablename__ = "user_order"

    user_id = Column(String(32), ForeignKey("user.user_id"), primary_key=True)
    order_id = Column(String)



class User(Base):
    __tablename__ = "user"

    user_id = Column(String(32), primary_key=True)
    user_name = Column(String(32))
