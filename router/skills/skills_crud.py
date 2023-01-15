from fastapi import APIRouter

from database.database import SessionLocal
from database.schemas import Skill, EducationCompany


router = APIRouter(
    prefix = '/skills'
)


@router.post('/')
def create_skill(data: Skill):
    pass
