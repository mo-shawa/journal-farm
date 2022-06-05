from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId


class ObjectIdStr(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError(f"{v} is not a valid ObjectId")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="str")


class JournalEntry(BaseModel):
    title: str
    body: str
    # date: str
    sentiment: str
    probability: float
    # user_id: int

    # class Config:
    #     orm_mode = True

# class
