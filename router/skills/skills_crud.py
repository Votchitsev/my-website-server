from fastapi import APIRouter

from database.database import SessionLocal
from database.schemas import Skill
from router.skills.create import create
from router.skills.get import get


router = APIRouter(
    prefix = '/skill'
)


@router.post('/')
def create_skill(data: Skill):
    create(SessionLocal(), data)


@router.get('/')
def get_skill(lang: str, edu_id: int):
    return get(SessionLocal(), lang, edu_id)
    