from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base


class Role(Base):
    __tablename__ = 'roles'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    users = relationship('User')

    def __repr__(self):
        return f"[{self.id}] Role\nname={self.name}"
