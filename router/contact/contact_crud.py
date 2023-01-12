from fastapi import APIRouter

from database.database import SessionLocal
from router.contact.create import create
from router.contact.get import get


router = APIRouter(
  prefix = '/contact'
)


@router.post('/')
def create_contact(data):
    create(SessionLocal(), data)

@router.get('/')
def get_contact(lang: str):
    return get(SessionLocal(), lang)
    