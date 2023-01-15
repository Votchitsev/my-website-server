from sqlalchemy.orm import Session
from datetime import datetime

from database.models import Feedback


def create(db: Session, data):
    feedback = Feedback(
        date = datetime.strptime(data.date, '%Y-%m-%d'),
        name = data.name,
        email = data.email,
        message = data.message,
    )

    db.add(feedback)

    db.commit()
    db.close()