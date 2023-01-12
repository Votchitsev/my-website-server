from sqlalchemy.orm import Session

from database.models import Contact
from router.get_language_id import get_language_id
from router.row_is_created import row_is_created


def create(db: Session, data):
    language_id = get_language_id

    if row_is_created(db, language_id, Contact):
        db.query(Contact).filter(Contact.language_id == language_id).\
            update({
              "name": data.name,
              "burth_date": data.burth_date,
              "city": data.city,
              "email": data.email,
              "phone": data.phone,
              "current_job": data.current_job,
              "is_active": data.is_active,
            })
        db.commit()
        return
    
    contact = Contact(
        name = data.name,
        burth_date = data.burth_date,
        city = data.city,
        email = data.email,
        phone = data.phone,
        current_job = data.current_job,
        is_active = data.is_active,
    )

    db.add(contact)

    db.commit()
    