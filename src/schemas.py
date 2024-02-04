from datetime import datetime
from pydantic import BaseModel


class WorkDayDuration(BaseModel):
    at: datetime
    project_name: str
    duration: int
