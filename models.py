from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import declarative_base, relationship

# from sqlalchemy.orm import selectinload


Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    user = Column(String)
    # connection_id = Column(Integer, ForeignKey("connection.id"))
    # connection = relationship("Connection", backref='user', lazy="immediate")  # back_populates="user",
    connection_u = relationship("Connection", lazy="selectin")

    # def __repr__(self):
    #     return f"<{self.user}>"


class Group(Base):
    __tablename__ = "group"
    id = Column(Integer, primary_key=True)
    vk_url = Column(String)
    # connection_id = Column(Integer, ForeignKey("connection.id"))
    connection_g = relationship(
        "Connection", lazy="selectin"
    )  # ,  backref='group', lazy="immediate")

    # def __repr__(self):
    #     return f"<{self.vk_url}>"


class Connection(Base):
    __tablename__ = "connection"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    group_id = Column(Integer, ForeignKey("group.id"))
    create_date = Column(DateTime, server_default=func.now())
    user = relationship("User", backref="user_u", lazy="selectin")  # uselist=False,
    group = relationship(
        "Group", backref="group_g", lazy="selectin"
    )  # uselist=False, back_populates
    #
    # # __mapper_args__ = {"eager_defaults": True}
