from typing import List, Union

from pydantic import BaseModel, validator

    
class AboutMe(BaseModel):
    text: str
    language: str
    is_active: bool

    @validator('language')
    def validate_language(cls, value):
        if value != 'ru' and value != 'en':
            raise ValueError('Unexpected language name. Please, choose one of en or ru')
        return value
