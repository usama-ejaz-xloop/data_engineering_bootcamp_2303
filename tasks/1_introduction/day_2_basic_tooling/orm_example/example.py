import random
from sqlalchemy import Column, Integer, String, create_engine, select
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()


class TODOItem(Base):  # type: ignore
    __tablename__ = "todo_item"

    id = Column(Integer, primary_key=True)
    content = Column(String(3000))

    def __repr__(self):
        return f"TODOItem(id={self.id}, content={self.content})"


engine = create_engine("sqlite:///db.sqlite3", echo=True)
Base.metadata.create_all(engine)


with Session(engine) as session:
    todo_item = TODOItem(content=f"Example (random number={random.randint(1, 1000)})")
    session.add(todo_item)
    session.commit()

    todo_items = select(TODOItem)
    for todo_item in session.scalars(todo_items):
        print(todo_item)
