from sqlalchemy.orm import Session

from database.models import AboutMe
from database.models import Language


def get(db: Session, lang):
    query_response = db.query(AboutMe).join(Language).filter(Language.name == lang).first()

    return {
        "text": query_response.text,
    }