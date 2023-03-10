from sqlalchemy.orm import Session
from datetime import datetime

from database.models import Contact
from router.get_language_id import get_language_id
from router.row_is_created import row_is_created


def create(db: Session, data):
    language_id = get_language_id(data.language)

    if row_is_created(db, language_id, Contact):
        db.query(Contact).filter(Contact.language_id == language_id).\
            update({
              "name": data.name,
              "burth_date": datetime.strptime(data.burth_date, '%Y-%m-%d'),
              "city": data.city,
              "email": data.email,
              "phone": data.phone,
              "current_job": data.current_job,
              "is_active": data.is_active,
            })
        db.commit()
        db.close()
        return
    
    contact = Contact(
        name = data.name,
        burth_date = datetime.strptime(data.burth_date, '%Y-%m-%d'),
        city = data.city,
        email = data.email,
        phone = data.phone,
        current_job = data.current_job,
        language_id = language_id,
        is_active = data.is_active,
    )

    db.add(contact)

    db.commit()

    db.close()
    