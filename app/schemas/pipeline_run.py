from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from enum import Enum


class PipelineStatus(str, Enum):
    pending = "pending"
    running = "running"
    success = "success"
    failed = "failed"


class PipelineRunBase(BaseModel):
    name: str


class PipelineRunCreate(PipelineRunBase):
    pass


class PipelineRunResponse(PipelineRunBase):
    id: int
    status: PipelineStatus
    started_at: Optional[datetime]
    finished_at: Optional[datetime]
    created_at: datetime
    created_by_id: Optional[int]

    class Config:
        from_attributes = True