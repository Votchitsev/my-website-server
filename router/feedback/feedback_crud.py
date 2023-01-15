from fastapi import APIRouter

from database.database import SessionLocal
from database.schemas import Feedback
from router.feedback.create import create
from router.feedback.get import get
from router.feedback.delete import delete


router = APIRouter(
    prefix = '/feedback'
)


@router.post('/')
def create_feedback(data: Feedback):
    create(SessionLocal(), data)


@router.get('/')
def get_feedbaack():
    return get(SessionLocal())


@router.delete('/')
def delete_feedback(id: int):
    delete(SessionLocal(), id)
    