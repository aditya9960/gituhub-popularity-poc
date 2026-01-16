from fastapi import APIRouter
from typing import Optional


router = APIRouter(prefix="/urls", tags=["urls-v1"])

@router.get("/popular")
def get_popular_repos(language: Optional[str] = None, created_after: Optional[str] = None):
    print("I am here")
    return [{"Result": "Success"}]

