from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine, Text
from sqlalchemy.orm import sessionmaker, relationship

sinc_engine = create_engine("postgresql+psycopg2://postgres:vjnjh421@localhost/task_manager_db")
sync_session = sessionmaker(bind=sinc_engine)


BASE = declarative_base()

class User(BASE):
    __tablename__ = "User_data"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    surname = Column(String, index=True)
    age = Column(Integer, index=True)
    position = Column(String, index=True)

    tasks = relationship("Task", back_populates="owner")

class Task(BASE):
    __tablename__ = "Task_data"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    discription = Column(Text)
    complition_time_start = Column(DateTime, index=True)
    complition_time_end = Column(DateTime, index=True)
    complited = Column(String, index=True, default="In Process")

    user_id = Column(Integer, ForeignKey("User_data.id"))

    owner = relationship("User", back_populates="tasks")

def get_db():
    db = sync_session()
    try:
        yield db
    finally:
        db.close()