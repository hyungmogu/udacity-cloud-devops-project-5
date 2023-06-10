from datetime import datetime
from sqlmodel import SQLModel, Field

class ConvertedImage(SQLModel, table=True):
    id:int = Field(default=None, primary_key=True)
    url:str
    converted_format:str

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "url": "AWS_S3_URL_GOES_HERE",
                "converted_format": "jpg"
            }
        }
