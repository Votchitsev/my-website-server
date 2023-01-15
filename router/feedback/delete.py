from fastapi import HTTPException
from sqlalchemy.orm import Session

from database.models import Feedback


def delete(db: Session, id):
    feedback = db.query(Feedback).filter(Feedback.id == id)

    if feedback:
        feedback.delete()
        db.commit()
        return

    raise HTTPException(status_code=404, detail="feedback not found")
    