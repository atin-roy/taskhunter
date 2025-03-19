import argparse
from task_manager import add_task, list_tasks, mark_task_done, delete_task
from database import initialize_db

# Initialize database
initialize_db()

parser = argparse.ArgumentParser(description="CLI Task Manager")
parser.add_argument(
    "action", choices=["add", "list", "done", "delete"], help="Action to perform"
)
parser.add_argument("--title", type=str, help="Title of the task (for 'add' command)")
parser.add_argument(
    "--desc", type=str, help="Description of the task (for 'add' command)"
)
parser.add_argument("--id", type=int, help="Task ID (for 'done' and 'delete' commands)")


args = parser.parse_args()

if args.action == "add":
    if args.title:
        add_task(args.title, args.desc or "")
        print("Task '{}' added successfully!".format(args.title))
    else:
        print("Error: --title is required for adding a task.")

elif args.action == "list":
    tasks = list_tasks()
    if tasks:
        for task in tasks:
            print("[{}] {} - {} ({})".format(task[0], task[1], task[3], task[4]))
    else:
        print("No tasks found.")

elif args.action == "done":
    if args.id:
        mark_task_done(args.id)
        print(f"Task {args.id} marked as done.")
    else:
        print("Error: --id is required for marking a task as done.")

elif args.action == "delete":
    if args.id:
        delete_task(args.id)
        print(f"Task {args.id} deleted.")
    else:
        print("Error: --id is required for deleting a task.")
