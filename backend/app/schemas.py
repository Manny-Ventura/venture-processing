from pydantic import BaseModel, Field
from typing import Literal, Optional

class InspectionCreate(BaseModel):
    machine_id: str = Field(min_length=1)
    operator_id: str = Field(min_length=1)
    shift_number: Literal[1,2,3]
    vibration_level: Literal['normal', 'elevated', 'severe']
    temperature: Optional[float] = None
    notes: Optional[str] = None
