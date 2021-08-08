from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import declarative_base, relationship

# from sqlalchemy.orm import selectinload


Base = declarative_base()


class Connection(Base):
    __tablename__ = "connection"
    id = Column(Integer, primary_key=True)
    # user_id = Column(ForeignKey("user.id"), primary_key=True)
    # group_id = Column(ForeignKey("vk_group.id"), primary_key=True)
    create_date = Column(DateTime, server_default=func.now())
    # group = relationship("VkGroup", secondary="connection_group")
    user = relationship("User", back_populates="connection", uselist=False)
    group = relationship("Group", back_populates="connection", uselist=False)

    # __mapper_args__ = {"eager_defaults": True}


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    user = Column(String)
    # connection = Column(ForeignKey("connection.id"))
    # groups = relationship("Connection", back_populates="user")
    connection_id = Column(Integer, ForeignKey("connection.id"))

    # many-to-one side remains, see tip below
    connection = relationship("Connection", back_populates="user")


class Group(Base):
    __tablename__ = "group"
    id = Column(Integer, primary_key=True)
    vk_url = Column(String)
    connection_id = Column(Integer, ForeignKey("connection.id"))

    # many-to-one side remains, see tip below
    connection = relationship("Connection", back_populates="group")
