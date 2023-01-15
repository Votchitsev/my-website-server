from fastapi import HTTPException
from sqlalchemy.orm import Session

from database.models import Feedback


def get(db: Session):
    query_response = db.query(Feedback).all()

    if query_response:
        return {
            "feedback": query_response
        }

    raise HTTPException(status_code=404, detail="Feedback not found")
    