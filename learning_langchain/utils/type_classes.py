from pydantic import BaseModel, Field


class Person_Request(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Andrew NG",
            }
        }
