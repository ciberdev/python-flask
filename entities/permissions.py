from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from entities import Base

class Permission(Base):
    __tablename__ = "tf_permissions"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    permission_name: Mapped[str]