from classes import User_, Task_
from db_connect import get_db
import re

def main():
    #print("Add user: -add user <name> <surname> <age> <position>")
    #print("Delete user: -delete user <name> <surname>")
    #print("Exit: -exit")
    #print("Assign task: -asgn task <name> <surname> <\"taskname>\"")
    #print()
    #print("Create task: -create task <\"example name\": <\"discription\">")
    #print("Delete task: -delete task <\"name\">")
    #print()

    start = True

    while start:
        command = input(">")
        try:
            if "-add user " in command:
                user_attribute = command.split()[2:]
                user = User_(name=user_attribute[0], surname=user_attribute[1], age=user_attribute[2], position=user_attribute[3])
                with next(get_db()) as db:
                    user.create_user(db=db)
            elif "-delete user " in command:
                user_attribute = command.split()[2:]
                user = User_(name=user_attribute[0], surname=user_attribute[1])
                with next(get_db()) as db:
                    user.delete_user(db=db)
            elif "-asgn task " in command:
                asgn_attribute = command.split()[2:]
                user = User_(name=asgn_attribute[0], surname=asgn_attribute[1])
                task = Task_(name=(re.search(r"\".+.\"", command).group(0).replace("\"", "")))
                with next(get_db()) as db:
                    user.assign_task(task_name=task, db=db)

            elif "-create task " in command:
                task_attribute = command[13:].split(": ")
                task = Task_(name=task_attribute[0].replace("\"", ""), discription=task_attribute[-1].replace("\"", ""))
                with next(get_db()) as db:
                    task.create_task(db=db)
            elif "-delete task " in command:
                task_attribute = command.split()[2:]
                task = Task_(name=(re.search(r"\".+.\"", command).group(0).replace("\"", "")))
                with next(get_db()) as db:
                    task.delete_task(db=db)

            elif command == "-exit":
                start = False
            else:
                print("[-] Неизвестная команда")

        except Exception as e:
            print(f"[-] Error: {e}")
        


if __name__ == "__main__":
    main()
    
    