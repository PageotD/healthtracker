from pydantic import BaseModel

class User(BaseModel):
    uuid: str
    user_id: str
    user_name: str

class Weight(BaseModel):
    uuid: str
    user_id: str
    measurement_datetime: str
    weight_value: float

class Sleep(BaseModel):
    uuid: str
    user_id: str
    start_datetime: str
    end_datetime: str

class Activity(BaseModel):
    uuid: str
    user_id: str
    start_datetime: str
    end_datetime: str