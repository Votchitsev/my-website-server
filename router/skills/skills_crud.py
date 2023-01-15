from fastapi import APIRouter

from database.database import SessionLocal
from database.schemas import Skill
from router.skills.create import create


router = APIRouter(
    prefix = '/skill'
)


@router.post('/')
def create_skill(data: Skill):
    create(SessionLocal(), data)
