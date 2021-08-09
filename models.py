from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import declarative_base, relationship

# from sqlalchemy.orm import selectinload


Base = declarative_base()


class Connection(Base):
    __tablename__ = "connection"
    id = Column(Integer, primary_key=True)
    # user_id = Column(Integer, ForeignKey('user.id'))
    # group_id = Column(Integer, ForeignKey('group.id'))
    create_date = Column(DateTime, server_default=func.now())
    user = relationship(
        "User", back_populates="connection", lazy="selectin"
    )  # uselist=False,
    group = relationship(
        "Group", back_populates="connection", lazy="selectin"
    )  # uselist=False,

    # __mapper_args__ = {"eager_defaults": True}


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    user = Column(String)
    connection_id = Column(Integer, ForeignKey("connection.id"))
    connection = relationship("Connection", back_populates="user", lazy="selectin")

    # def __repr__(self):
    #     return f"<{self.user}>"


class Group(Base):
    __tablename__ = "group"
    id = Column(Integer, primary_key=True)
    vk_url = Column(String)
    connection_id = Column(Integer, ForeignKey("connection.id"))
    connection = relationship("Connection", back_populates="group", lazy="selectin")

    # def __repr__(self):
    #     return f"<{self.vk_url}>"
