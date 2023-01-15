from sqlalchemy.orm import Session

from database.models import AboutMe
from router.row_is_created import row_is_created
from router.get_language_id import get_language_id


def create(db: Session, data):
    language_id = get_language_id(data.language)

    if row_is_created(db, language_id, AboutMe):
        db.query(AboutMe).filter(AboutMe.language_id == language_id).\
            update({
              "text": data.text,
              "is_active": data.is_active  
            })
        db.commit()
        db.close()
        return

    about_me = AboutMe(
        text = data.text,
        language_id = language_id,
        is_active = data.is_active
    )

    db.add(about_me)

    db.commit()

    db.close()
