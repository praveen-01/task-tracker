import sys
from task import Processor
    
def main():
    task_tracker = Processor()
    if len(sys.argv)<=1:
        print("Invalid parameters.Please check below for usage...")
        task_tracker.help_message()
    else:
        command = sys.argv[1].strip()
        if command == "add":
            descrption = sys.argv[2:]
            if not descrption:
                print("Please provide a valid descripton. Usage: task-tracker-cli add <desc>")
            task_tracker.add_message(descrption)
        elif command == "list":
            status=None
            if len(sys.argv)>2:
                status = sys.argv[2]
            task_tracker.list(status)
        elif command == "update":
            if len(sys.argv)<4:
                print("Invalid format. Usage: task-tracker-cli update <id> <new_description>")
            else:
                task_tracker.update_desc(int(sys.argv[2])," ".join(sys.argv[3:]))
        elif command == "delete":
            if len(sys.argv)<3:
                print("Invalid format. usage: task-tracker-cli delete <id>")
            else:
                task_tracker.delete_task(int(sys.argv[2]))
        elif command == "modify":
            if len(sys.argv)<4:
                print("Invalid format. usage: task-tracker-cli update <id> <new_description>")
            else:
                task_tracker.update_status(int(sys.argv[2])," ".join(sys.argv[3:]))
        else:
            task_tracker.help_message()

if __name__ == "__main__":
    main()