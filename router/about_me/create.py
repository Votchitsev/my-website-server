from sqlalchemy.orm import Session

from database.models import AboutMe


def about_me_is_created(db: Session, language_id):
    result = db.query(AboutMe).filter(AboutMe.language_id == language_id).all()

    if len(result) > 0:
        return True
    
    return False


def create(db: Session, data):
    language_id = int

    if data.language == 'ru':
        language_id = 1
    
    if data.language == 'en':
        language_id = 2


    if about_me_is_created(db, language_id):
        db.query(AboutMe).filter(AboutMe.language_id == language_id).\
            update({
              "text": data.text,
              "is_active": data.is_active  
            })
        db.commit()
        return

    about_me = AboutMe(
        text = data.text,
        language_id = language_id,
        is_active = data.is_active
    )

    db.add(about_me)

    db.commit()
