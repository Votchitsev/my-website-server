from fastapi import APIRouter
from pydantic import BaseModel

from database.schemas import AboutMe
from database.database import SessionLocal
from router.about_me.create import create


router = APIRouter(
  prefix = '/about_me'
)


@router.post('/')
def create_about_me_text(data: AboutMe):
    create(SessionLocal(), data)
