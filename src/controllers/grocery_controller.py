"""grocery Controller File"""

# General Imports
import uuid
from fastapi import Response, status
from sqlalchemy.orm import Session

# Custom Imports
from ..managers import grocery_manager
from ..exceptions.app_exceptions import ValidationError
from ..validators.grocery_filter_model import GroceryFilter, UserOrder


def add_grocery_items(req: GroceryFilter, res: Response, db: Session):
    """Function to list all collateral types of a product type"""
    try:

       grocery_record = {
            "item_id": f"N-{uuid.uuid4().hex[:10]}".upper(),
            "name": req.name,
            "price": req.price,
            "quantity": req.quantity

        }
       print(f"Grocery record: {grocery_record}")

       grocery_manager.add_grocery(db, grocery_record)

       db.commit()
       return "Item added successfully"

    except Exception as e:
        res.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        if isinstance(e, ValidationError):
            res.status_code = status.HTTP_400_BAD_REQUEST
            return "Failed to create an item"

        return "Failed to create an item"


def view_grocery_items(res: Response, db: Session):
    """Function to list grocery item"""
    try:

        items = grocery_manager.get_grocery_items(db)

        if len(items) == 0:
            return "No items present in grocery"

        return items

    except Exception as e:
        res.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        if isinstance(e, ValidationError):
            res.status_code = status.HTTP_400_BAD_REQUEST
            return "Failed to list items"

        return "Failed to list items"



def remove_grocery_items(item_id: str, res: Response, db: Session):
    """Function to remove grocery item"""
    try:

        item = grocery_manager.item_exists(db, item_id)
        if len(item) == 0:
            return "Item is not present"

        items = grocery_manager.remove_grocery(db,item_id)


        db.commit()

        return "Successfully removed an item from grocery"

    except Exception as e:
        res.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        if isinstance(e, ValidationError):
            res.status_code = status.HTTP_400_BAD_REQUEST
            return "Failed to remove items"

        return "Failed to remove items"





def update_grocery_items(item_id: str, payload: dict, res: Response, db: Session):
    """Function to update grocery item"""
    try:

        item = grocery_manager.item_exists(db, item_id)
        if len(item) == 0:
            return "Item is not present"

        update_grocery_details = {}
        for key, value in payload.items():
            update_grocery_details.update({key:value})


        grocery_manager.update_grocery_entry(db, item_id, update_grocery_details)

        db.commit()

        return "Successfully updated grocery details"

    except Exception as e:
        res.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        if isinstance(e, ValidationError):
            res.status_code = status.HTTP_400_BAD_REQUEST
            return "Failed to update items"

        return "Failed to update items"




def manage_inventory(item_id: str, quantity: str, res: Response, db: Session):
    """Function to manage inventory"""
    try:

        item = grocery_manager.item_exists(db, item_id)
        if len(item) == 0:
            return "Item is not present"

        update_grocery_details = {"quantity": quantity}



        grocery_manager.update_grocery_entry(db, item_id, update_grocery_details)

        db.commit()

        return "Successfully updated inventory details"

    except Exception as e:
        res.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        if isinstance(e, ValidationError):
            res.status_code = status.HTTP_400_BAD_REQUEST
            return "Failed to update inventory"

        return "Failed to update inventory"





def view_grocery_items_users(res: Response, db: Session):
    """Function to list grocery item"""
    try:

        grocery_list = grocery_manager.get_grocery_items(db)

        if len(grocery_list) == 0:
            return "No items present in grocery"

        grocery_items = []
        for item in grocery_list:

            grocery = {}
            grocery.update({"name": item["name"]})
            grocery.update({"price": item["price"]})


            grocery_items.append(grocery)


        return grocery_items

    except Exception as e:
        res.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        if isinstance(e, ValidationError):
            res.status_code = status.HTTP_400_BAD_REQUEST
            return "Failed to list items"

        return "Failed to list items"


def place_order(user_id: str, order: UserOrder, res: Response, db: Session):
    """Function to place order for grocery item"""
    try:

        grocery_items = order.items
        total_price = 0
        order_id = f"N-{uuid.uuid4().hex[:10]}".upper()
        for item_details in grocery_items:

            order_details = {
                "order_id": order_id,
                "item_id": item_details.item_id,
                "quantity": item_details.quantity

            }


            grocery_manager.create_order(db, order_details)
            print ("Order Created successfully")


            grocery_details = grocery_manager.fetch_grocery_details(db, item_details.item_id)

            update_grocery_details = {"quantity": int(grocery_details["quantity"] ) - int(item_details.quantity)}
            grocery_manager.update_grocery_entry(db, item_details.item_id, update_grocery_details)

            print ("Grocery Details updated successfully")


            total_price = total_price +(float(grocery_details["price"]) * int(item_details.quantity))



        user_order_details = {
            "user_id": user_id,
            "order_id": order_id

        }

        grocery_manager.create_user_order(db, user_order_details)

        db.commit()
        return (f"Order placed successfully and total bill for the grocery items: {total_price}")

    except Exception as e:
        res.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        if isinstance(e, ValidationError):
            res.status_code = status.HTTP_400_BAD_REQUEST
            return "Failed to place an order"

        return "Failed to place an order"
