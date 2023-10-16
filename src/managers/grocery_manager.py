"""Grocery Manager File"""

# General Imports
from sqlalchemy.orm import Session

from ..models.general_model import (
  Grocery, OrderItem, UserOrder
)
from ..helpers import db_utils


def add_grocery(db: Session, grocery_details: dict):
    """Query to insert grocery details"""

    grocery = Grocery(
        item_id = grocery_details["item_id"],
        name = grocery_details["name"],
        price = grocery_details["price"],
        quantity = grocery_details["quantity"],
    )

    db.add(grocery)
    db.flush()

    return grocery


def get_grocery_items(db: Session):
    """Query to fetch all grocery items"""
    data = (
        db.query(
           Grocery.item_id,
           Grocery.name,
           Grocery.price,
           Grocery.quantity
        )

    )
    return db_utils.to_array(data)


def item_exists(db, item_id):
    """Query to check item id exists or not"""
    data = (
        db.query(
            Grocery.item_id
        )
        .filter(
            Grocery.item_id == item_id
        )
        .all()
    )

    return db_utils.to_array(data)


def remove_grocery(db: Session, item_id:str):
    """Query to insert note details"""

    item = db.query(Grocery).filter(Grocery.item_id == item_id).first()
    db.delete(item)


def update_grocery_entry(db, item_id, update_dict):
    """Query to update item details"""

    row_count = (
        db.query(Grocery)
        .filter(Grocery.item_id == item_id)
        .update(update_dict, synchronize_session = "fetch")
    )

    # Flush the update operation to database
    db.flush()

    return row_count


def create_order(db: Session, order_details: dict):
    """Query to create order"""

    order = OrderItem(
        order_id = order_details["order_id"],
        item_id = order_details["item_id"],
        quantity = order_details["quantity"]
    )

    db.add(order)
    db.flush()

    return order


def create_user_order(db: Session, user_order_details: dict):
    """Query to map user and order"""

    user_order = UserOrder(
        user_id = user_order_details["user_id"],
        order_id = user_order_details["order_id"]

    )

    db.add(user_order)
    db.flush()

    return user_order


def fetch_grocery_details(db: Session, item_id: str):
    """Query to fetch grocery details"""
    data = (
        db.query(
           Grocery.item_id,
           Grocery.name,
           Grocery.price,
           Grocery.quantity
        )
        .filter(Grocery.item_id == item_id)

    )
    return db_utils.to_array(data)[0]
