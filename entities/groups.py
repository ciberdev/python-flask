from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from entities import Base

class Group(Base):
     __tablename__ = "_tf_groups"
     
     id: Mapped[int] = mapped_column(primary_key=True)
     group_name: Mapped[str]
    