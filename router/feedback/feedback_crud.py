from fastapi import APIRouter

from database.database import SessionLocal
from database.schemas import Feedback
from router.feedback.create import create


router = APIRouter(
    prefix = '/feedback'
)


@router.post('/')
def create_feedback(data: Feedback):
    create(SessionLocal(), data)


@router.get('/')
def get_feedbaack():
    pass


@router.delete('/')
def delete_feedback(id):
    pass