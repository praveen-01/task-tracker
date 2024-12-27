import datetime
import sys
import json
from task import Task
from tabulate import tabulate

def now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def load_tasks():
    try:
        with open("storage_tasks.json","x") as file:
            json.dump([],file)
            return []
    except FileExistsError:
        with open("storage_tasks.json","r") as file:
            data = json.load(file)
            return [Task.to_obj(item) for item in data]

def update_storage(file_data):
    file_data = [Task.dict_val(item) for item in file_data]
    with open("storage_tasks.json","w") as file:
        json.dump(file_data,file,indent=4)
    
def add_message(desc):
    desc = " ".join(desc)
    file_data = load_tasks()
    id = max(task.id for task in file_data)+1 if file_data else 1
    record = Task(id,desc,"To-do",now(),now())
    file_data.append(Task.to_obj(record.dict_val()))
    update_storage(file_data)

def get_index(id,file_data):
    idx = None
    for idx,item in enumerate(file_data):
        print(item.id)
        if item.id == id:
            return idx
    return idx

def update_desc(id,desc):
    file_data = load_tasks()
    idx = get_index(id,file_data)
    if idx is None:
        print("Invalid id. Please select a valid task Id from the below tasks....")
        list()
    else:
        file_data[idx].description = desc
        file_data[idx].updated_at = now()
        update_storage(file_data)

def update_status(id,new_status):
    file_data = load_tasks()
    idx = get_index(id,file_data)
    if idx is None:
        print("Invalid id. Please select a valid task Id from the below tasks....")
        list()
    else:
        file_data[idx].status = new_status
        file_data[idx].updated_at = now()
        update_storage(file_data)

def delete_task(id):
    file_data = load_tasks()
    idx = get_index(id,file_data)
    if idx is None:
        print("Invalid id.Please select a valid task Id from the below tasks....")
        list()
    else:
        del file_data[idx]
        update_storage(file_data)

def list(status=None):
    file_data = load_tasks()
    headers = ["id","description","Status","Created At","Updated At"]
    to_display = []
    for item in file_data:
        to_append = [item.id,item.description,item.status,item.created_at,item.updated_at]
        if status is not None:
            if item.status == status:
                to_display.append(to_append)
        else:
            to_display.append(to_append)
        
    table = tabulate(to_display,headers=headers,tablefmt="grid")
    print(table)
        

def help_message():
    help_str = """Task Tracker takes instructions in the below mentioned format:
    task-tracker <option> <parameters>

    options
        
        add [description of task] 
        
        update [id] [new description of the task]
        
        list 
        
        modify [id of the task] [status of the task]
        
        delete [id of the task]
        
        help 
    """
    print(help_str)
    
def main():
    if len(sys.argv)<=1:
        print("Invalid parameters.Please provide valid parameters...")
        help_message()
    else:
        command = sys.argv[1].strip()
        if command == "add":
            descrption = sys.argv[2:]
            if not descrption:
                print("Please provide a valid descripton")
            add_message(descrption)
        elif command == "list":
            if len(sys.argv)>2:
                status = sys.argv[2]
            else:
                status=None
            list(status)
        elif command == "update":
            if len(sys.argv)<4:
                print("Invalid format. usage: update <id> <new_description>")
            else:
                update_desc(int(sys.argv[2])," ".join(sys.argv[3:]))
        elif command == "delete":
            if len(sys.argv)<3:
                print("Invalid format. usage: delete <id>")
            else:
                delete_task(int(sys.argv[2]))
        elif command == "modify":
            if len(sys.argv)<4:
                print("Invalid format. usage: update <id> <new_description>")
            else:
                update_status(int(sys.argv[2])," ".join(sys.argv[3:]))
        else:
            help_message()
if __name__ == "__main__":
    main()