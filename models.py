from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import selectinload


Base = declarative_base()

#
# class A(Base):
#     __tablename__ = "a"
#
#     id = Column(Integer, primary_key=True)
#     data = Column(String)
#     create_date = Column(DateTime, server_default=func.now())
#     bs = relationship("B")
#
#     # required in order to access columns with server defaults
#     # or SQL expression defaults, subsequent to a flush, without
#     # triggering an expired load
#     __mapper_args__ = {"eager_defaults": True}
#
#
# class B(Base):
#     __tablename__ = "b"
#     id = Column(Integer, primary_key=True)
#     a_id = Column(ForeignKey("a.id"))
#     data = Column(String)


class A(Base):
    __tablename__ = "a"
    id = Column(Integer, primary_key=True)
    data = Column(String)
    data2 = Column(String, server_default='Smth')
    create_date = Column(DateTime, server_default=func.now())


class B(Base):
    __tablename__ = "b"
    id = Column(Integer, primary_key=True)
    data = Column(String)
