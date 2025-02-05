"""
Это система для управления проектами, с возможностью создания задач, 
назначения их пользователям, отслеживания статуса выполнения. 
Это может быть полезным инструментом в работе или на практике.
"""
from db_connect import User, Task
from datetime import datetime
from sqlalchemy import and_

class Task_:
    def __init__(self, name: str, discription: str | None = None):
        self.name = name
        self.discription = discription
        self.complition_time_start = datetime.now()
        self.complition_time_end = None

    def create_task(self, db):
        try:
            task_data = Task(
                name=self.name,
                discription=self.discription,
                complition_time_start=self.complition_time_start,
                complition_time_end=self.complition_time_end
            )
            db.add(task_data)
            db.commit()
            db.refresh(task_data)
            print("[+] Задача создана")
        except Exception as e:
            print("[-] Такое имя задачи уже существует")
    
    def get_task(self, db):
        try:
            return db.query(Task).filter(Task.name == self.name).first()
        except Exception as e:
            print("[-] Такой задачи не существует")

    def delete_task(self, db):
        task = self.get_task(db=db)
        if task:
            db.delete(task)
            db.commit()
            print(f"[+] Задача {self.name} удалёна")
        else:
            print("[-] Задача не найдена")

class User_:
    def __init__(self, name: str, surname: str, age: int|None = None, position: str|None = None):
        self.name = name
        self.surname = surname
        self.age = age
        self.position = position
        self.tasks = []
    
    def create_user(self, db):
        user_data = User(
            name=self.name,
            surname=self.surname,
            age=self.age,
            position=self.position
        )
        db.add(user_data)
        db.commit()
        db.refresh(user_data)
        print("[+] Пользователь создан")

    def delete_user(self, db):
        user = self.get_user(db=db)
        if user:
            db.delete(user)
            db.commit()
            print(f"[+] Пользователь {self.name} {self.surname} удалён")
        else:
            print("[-] Пользователь не найден")

    def assign_task(self, db, task_name: Task_):
        try:
            task = task_name.get_task(db=db)
            user = self.get_user(db=db)
            task.owner = user
            db.commit()
            db.refresh(user)
            print("[+] Задача добавлена")
        except Exception as e:
            print("[-] Такой задачи не существует")

    def get_user(self, db):
        try:
            return db.query(User).filter(and_(User.name == self.name, User.surname == self.surname)).first()
        except Exception as e:
            print("[-] Такого пользователя не существует")
