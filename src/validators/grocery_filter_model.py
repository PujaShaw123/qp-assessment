"""Grocery Filter Validation File"""

# General Imports
from pydantic import BaseModel
from typing import List


class GroceryFilter(BaseModel):

    name: str
    price: str
    quantity: str


class Order(BaseModel):

    item_id: str
    quantity: str


class UserOrder(BaseModel):
    items: List[Order]
