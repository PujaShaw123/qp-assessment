# General Imports

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Response, Body

from ..controllers import grocery_controller

# Custom Imports
from ..database import get_db_connection
from ..validators.grocery_filter_model import GroceryFilter, UserOrder

# Initializing extraction router instance
router = APIRouter()

@router.post("/admin/items")
def add_grocery_items(
    grocery: GroceryFilter,
    response: Response,
    db: Session = Depends(get_db_connection)
):
    """API to fetch grocery items"""
    return grocery_controller.add_grocery_items(grocery, response, db)


@router.get("/admin/items")
def view_grocery_items(
    response: Response,
    db: Session = Depends(get_db_connection)
):
    """API to fetch grocery items"""
    return grocery_controller.view_grocery_items(response, db)


@router.delete("/admin/items/{item_id}")
def remove_grocery_items(
    item_id: str,
    response: Response,
    db: Session = Depends(get_db_connection)
):
    """API to remove grocery items"""
    return grocery_controller.remove_grocery_items(item_id, response, db)



@router.put("/admin/items/{item_id}")
def update_grocery_items(
    item_id: str,
    response: Response,
    payload: dict = Body(...),
    db: Session = Depends(get_db_connection)
):
    """API to update grocery items"""
    return grocery_controller.update_grocery_items(item_id, payload, response, db)


@router.put("/admin/items/{item_id}/inventory")
def manage_inventory(
    item_id: str,
    quantity: str,
    response: Response,
    db: Session = Depends(get_db_connection)
):
    """API to update grocery items"""
    return grocery_controller.manage_inventory(item_id, quantity, response, db)


@router.get("/user/items")
def view_grocery_items(
    response: Response,
    db: Session = Depends(get_db_connection)
):
    """API to fetch grocery items"""
    return grocery_controller.view_grocery_items_users(response, db)


@router.post("/user/{user_id}/orders")
def place_order(
    user_id: str,
    order: UserOrder,
    response: Response,
    db: Session = Depends(get_db_connection)
):
    """API to place order for grocery items"""
    return grocery_controller.place_order(user_id, order, response, db)
