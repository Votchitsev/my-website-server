from fastapi import APIRouter

from database.database import SessionLocal
from database.schemas import EducationCompany
from router.education_company.create import create
from router.education_company.get import get


router = APIRouter(
  prefix = '/edu'
)


@router.post('/')
def create_edu(data: EducationCompany):
    create(SessionLocal(), data)


@router.get('/')
def get_edu(data: EducationCompany, lang: str):
    get(SessionLocal(), lang)
