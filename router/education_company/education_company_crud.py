from fastapi import APIRouter

from database.database import SessionLocal
from database.schemas import EducationCompany
from router.education_company.create import create


router = APIRouter(
  prefix = '/edu'
)


@router.post('/')
def create_edu(data: EducationCompany):
    create(SessionLocal(), data)
