from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer,String,select,update,delete
from sqlalchemy.orm import Mapped,mapped_column,DeclarativeBase


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class Submissions(Base):
    __tablename__ = "submissions"
    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    name:Mapped[str] = mapped_column(nullable=False)
    height:Mapped[int] = mapped_column(nullable=False)
    pyramid:Mapped[str] = mapped_column(nullable=False)
