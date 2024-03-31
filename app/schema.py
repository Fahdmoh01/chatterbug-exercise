from fastapi import HTTPException, status
from pydantic import BaseModel, Field, validator
from typing import Optional


class PasswordFields(BaseModel):
    length: int = Field(default=8)
    symbols: Optional[bool] = Field(default=True)
    digits: Optional[bool] = Field(default=True)
    lowercase: Optional[bool] = Field(default=True)
    uppercase: Optional[bool] = Field(default=True)

    @validator("length")
    def verify_length(cls, lengthCheck: int):
        """Error handling for invalid length inputs"""
        if not (isinstance(lengthCheck, int)) or lengthCheck <= 8:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail={
                    "error": "length must be a positive integer greater than or equal to 8"
                },
            )
        return lengthCheck
