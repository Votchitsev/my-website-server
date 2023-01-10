from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Text
from sqlalchemy.orm import relationship, validates

from .database import Base

class Language(Base):
    __tablename__ = 'language'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    about_me_text = relationship('about_me')
    contact_text = relationship('contact')
    education_company_text = ('education_company')
    skills_text = ('skills')


    # @validates('name')
    # def validate_name(self, _, name):
    #     if name != 'ru' or name != 'en':
    #         raise ValueError('Unexpected language name. Please, choose one of "en" or "ru"')
    #     return name


class AboutMe(Base):
    __tablename__ = 'about_me'

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    language_id = Column(String, ForeignKey('language.id'))
    is_active = Column(Boolean, default=True)


class Contact(Base):
    __tablename__ = 'contact'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    burth_date = Column(Date)
    city = Column(String)
    email = Column(String)
    phone = Column(String)
    current_job = Column(String)
    language_id = Column(Integer, ForeignKey('language.id'))
    is_active = Column(Boolean, default=True)


class EducationCompany(Base):
    __tablename__ = 'education_company'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    start_education_date = Column(Date)
    finish_education_date = Column(Date)
    logo = Column(String)
    language_id = Column(Integer, ForeignKey('language.id'))

    skills = relationship('skills')


class Skills(Base):
    __tablename__ = 'skills'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    education_company_id = (Integer, ForeignKey('education_company.id'))
    language = (Integer, ForeignKey('language.id'))


class Feedback(Base):
    __tablename__ = 'feedback'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    name = Column(String)
    email = Column(String)
    message = Column(Text)