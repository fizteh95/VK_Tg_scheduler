from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import declarative_base, relationship

# from sqlalchemy.orm import selectinload


Base = declarative_base()


class Connections(Base):
    __tablename__ = "connection"
    user_id = Column(ForeignKey("user.id"), primary_key=True)
    group_id = Column(ForeignKey("vk_group.id"), primary_key=True)
    create_date = Column(DateTime, server_default=func.now())
    group = relationship("VkGroup", back_populates="user")
    user = relationship("User", back_populates="vk_group")


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    user = Column(String)
    groups = relationship("Connection", back_populates="user")


class VkGgroup(Base):
    __tablename__ = "vk_group"
    id = Column(Integer, primary_key=True)
    vk_url = Column(String)
    users = relationship("Connection", back_populates="group")
