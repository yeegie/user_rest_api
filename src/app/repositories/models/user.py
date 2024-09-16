from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    fio = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    role_id = Column(Integer, ForeignKey("roles.id"))
    role = relationship("Role")

    def __repr__(self) -> str:
        return f"[{self.id}] User\nfio={self.fio}\nemail={self.email}\nrole={self.role.name}"
