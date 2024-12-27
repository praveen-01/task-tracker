class Task():
    def __init__(self,id,description,status,created_at,updated_at):
        self.id = id
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at
        self.status = status
    
    def dict_val(self):
        return {"id": self.id,
                "description": self.description,
                "created_at": self.created_at,
                "updated_at": self.updated_at,
                "status": self.status}

    def to_obj(dict):
        return Task(id=dict["id"],description=dict["description"],status = dict["status"],created_at=dict["created_at"],updated_at=dict["updated_at"])