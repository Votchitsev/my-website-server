from sqlalchemy.orm import Session

from . import models

def is_languages(db: Session):
    languages = db.query(models.Language).all()
    if len(languages):
        return True

def create_languages(db: Session):
    if not is_languages(db):
        ru = models.Language(name='ru')
        db.add(ru)

        en = models.Language(name='en')
        db.add(en)

        db.commit()
