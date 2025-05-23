from sqlalchemy.orm import Mapped, mapped_column
import sqlalchemy as sa
from src.settings import Base
import datetime
from sqlalchemy import func
from typing_extensions import Annotated
class User(Base):
    id: Mapped[int] = mapped_column(primary_key=True, type_=sa.BIGINT)
    name: Mapped[str] = mapped_column(type_=sa.TEXT)

intpk = Annotated[int, mapped_column(primary_key=True)]

class UserMessages(Base):
    id: Mapped[int] = mapped_column(primary_key=True, type_=sa.BIGINT)
    chat_id: Mapped[int] = mapped_column(type_=sa.BIGINT)
    message:  Mapped[int] = mapped_column(type_=sa.TEXT)
    created_date: Mapped[datetime.datetime] = mapped_column(type_=sa.TIMESTAMP, server_default=func.CURRENT_TIMESTAMP())
    user_id: Mapped[intpk] = mapped_column(sa.ForeignKey('users_user.id'))