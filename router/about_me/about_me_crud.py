from fastapi import APIRouter

from database.schemas import AboutMe
from database.database import SessionLocal
from router.about_me.create import create
from router.about_me.get import get


router = APIRouter(
  prefix = '/about_me'
)


@router.post('/')
def create_about_me_text(data: AboutMe):
    create(SessionLocal(), data)


@router.get('/')
def get_about_me_text(lang: str):
    return get(SessionLocal(), lang)
