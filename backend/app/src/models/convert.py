from datetime import datetime
from sqlmodel import SQLModel, Field

class ConvertedImage(SQLModel, table=True):
    url:str
    converted_format:str

    class Config:
        schema_extra = {
            "example": {
                "url": "AWS_S3_URL_GOES_HERE",
                "converted_format": "jpg"
            }
        }
