from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from entities.base import Base
import datetime


class UserType(Base):
    __tablename__ = "tf_user_type"
    
    idtype : Mapped[int] = mapped_column(primary_key=True)
    utype_name: Mapped[str]
    
    users: Mapped[List["User"]] = relationship("User", back_populates ="userType")

class User(Base):
    __tablename__ = "tf_user"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_name : Mapped[str]
    email_address: Mapped[str]
    password: Mapped[str]
    first_name: Mapped[str]
    last_name : Mapped[str]
    created: Mapped[datetime.date]
    
    # Llave foranea al objeto TipoUsuario
    idtype: Mapped[int] = mapped_column(ForeignKey("tf_user_type.idtype"))   
    # Campo que representa la relacion con el objeto Usuario
    userType: Mapped["UserType"] = relationship("UserType", back_populates = "users")    