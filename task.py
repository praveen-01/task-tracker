import json,datetime,os
from tabulate import tabulate

task_file_path = os.path.expanduser("~/storage_tasks.json")
class Tasktracker():
    def __init__(self,id,description,status,created_at,updated_at):
        self.id = id
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at
        self.status = status
    
    def dict_val(self):
        return { "id": self.id,
                "description": self.description,
                "created_at": self.created_at,
                "updated_at": self.updated_at,
                "status": self.status } 

    def to_obj(dict):
        return Tasktracker(id=dict["id"],description=dict["description"],status = dict["status"],created_at=dict["created_at"],updated_at=dict["updated_at"])

class Processor():
    def __init__(self):
        self.file_data = self.load_tasks()

    def now(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def load_tasks(self):
        try:
            with open(task_file_path) as file:
                data = json.load(file)
                return [Tasktracker.to_obj(item) for item in data]
        except FileNotFoundError:
            return []

    def update_storage(self):
        file_data = [Tasktracker.dict_val(item) for item in self.file_data]
        with open(task_file_path,"w") as file:
            json.dump(file_data,file,indent=4)

    def add_message(self,desc):
        desc = " ".join(desc)
        id = max(task.id for task in self.file_data)+1 if self.file_data else 1
        record = Tasktracker(id,desc,"To-do",self.now(),self.now())
        self.file_data.append(Tasktracker.to_obj(record.dict_val()))
        self.update_storage()

    def get_index(self,id):
        for idx,item in enumerate(self.file_data):
            if item.id == id:
                return idx
        return None

    def update_desc(self,id,desc):
        idx = self.get_index(id)
        if idx is None:
            print("Invalid id. Please select a valid task Id from the below tasks....")
            list()
        else:
            self.file_data[idx].description = desc
            self.file_data[idx].updated_at = self.now()
            self.update_storage()

    def update_status(self,id,new_status):
        idx = self.get_index(id)
        if idx is None:
            print("Invalid id. Please select a valid task Id from the below tasks....")
            self.list()
        else:
            self.file_data[idx].status = new_status
            self.file_data[idx].updated_at = self.now()
            self.update_storage()

    def delete_task(self,id):
        idx = self.get_index(id)
        if idx is None:
            print("Invalid id.Please select a valid task Id from the below tasks....")
            self.list()
        else:
            print(idx)
            del self.file_data[idx]
            self.update_storage()

    def list(self,status=None):
        headers = ["id","description","Status","Created At","Updated At"]
        to_display = []
        for item in self.file_data:
            to_append = [item.id,item.description,item.status,item.created_at,item.updated_at]
            if status is not None:
                if item.status == status:
                    to_display.append(to_append)
            else:
                to_display.append(to_append)
            
        table = tabulate(to_display,headers=headers,tablefmt="grid")
        print(table)
            

    def help_message(self):
        help_str = """Task Tracker
        Syntax
            task-tracker <option> <parameters>

        options
            
            - add <description of task>
                Add a new task with specified description into task tacker 
            
            - update <id> <new description of the task>
                Update the description of a existing task with its id
            
            - list <status>(Optional)
                List tasks with the specified status. If no status is provided, all tasks are displayed.
            
            - modify <id> <status of the task>
                Modify the status of a task by its ID.

            - delete <id>
                Delete a task by its ID.

            - help
                Display this help message.
        """
        print(help_str)