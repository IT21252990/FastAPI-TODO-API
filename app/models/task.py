from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer,primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    is_completed = Column(Boolean, default=False)

    # ForeignKey linked to the user
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"),nullable=False)

    # Relationship: many tasks --> one user
    owner = relationship("User", back_populates="tasks")