from fastapi import APIRouter

from database.database import SessionLocal
from database.schemas import EducationCompany
from router.education_company.create import create
from router.education_company.get import get
from router.education_company.delete import delete


router = APIRouter(
  prefix = '/edu'
)


@router.post('/')
def create_edu(data: EducationCompany):
    create(SessionLocal(), data)


@router.get('/')
def get_edu(lang: str):
    return get(SessionLocal(), lang)


@router.delete('/')
def delete_edu(id: int):
    delete(SessionLocal(), id)
    