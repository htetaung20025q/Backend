from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())


class SavedFile(Base):
    __tablename__ = "saved_files"
    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    file_name = Column(String, nullable=False)
    encrypted_content = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())


class ReceivedFile(Base):
    __tablename__ = "received_files"
    id = Column(Integer, primary_key=True, index=True)
    receiver_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    sender_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    file_name = Column(String, nullable=False)
    encrypted_content = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())
