"""Default Router"""

# General Imports
from fastapi import APIRouter, Response, status

# Custom Imports
from . import grocery_router


router = APIRouter()


@router.get(f"/health")
def health(
    response: Response = None,
):
    """Used in health check of a service"""
    response.status_code = status.HTTP_200_OK
    return "Successful"


# Compliance router
router.include_router(router=grocery_router.router)
