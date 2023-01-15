from sqlalchemy.orm import Session

from database.models import Feedback


def create(db: Session, data):
    feedback = Feedback(
        date = data.date,
        name = data.name,
        email = data.email,
        message = data.message,
    )

    db.add(feedback)

    db.commit()
    