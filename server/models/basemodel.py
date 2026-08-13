"""
Base model for all database tables.
"""

from datetime import UTC, datetime
from uuid import UUID, uuid7

from sqlalchemy.orm import Mapped, mapped_column

from server.models.base import Base


class BaseModel(Base):
    """
    Base model for all database tables
    """

    __abstract__ = True

    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC)
    )
    id: Mapped[UUID] = mapped_column(default=uuid7, primary_key=True)
