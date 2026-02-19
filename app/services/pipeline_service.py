from sqlalchemy.orm import Session
from datetime import datetime

from app.models.pipeline_run import PipelineRun, PipelineStatus


def create_pipeline_run(db: Session, name: str, user_id: int):
    pipeline = PipelineRun(
        name=name,
        created_by_id=user_id,
        status=PipelineStatus.pending
    )

    db.add(pipeline)
    db.commit()
    db.refresh(pipeline)

    return pipeline


def start_pipeline(db: Session, pipeline: PipelineRun):
    pipeline.status = PipelineStatus.running
    pipeline.started_at = datetime.utcnow()

    db.commit()
    db.refresh(pipeline)

    return pipeline


def finish_pipeline(db: Session, pipeline: PipelineRun, success: bool):
    pipeline.status = (
        PipelineStatus.success if success else PipelineStatus.failed
    )
    pipeline.finished_at = datetime.utcnow()

    db.commit()
    db.refresh(pipeline)

    return pipeline