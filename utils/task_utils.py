import json

from model.Task import Task
from time import gmtime, strftime

from utils.file_utils import add_task_to_file, json_file_path


def add_task(description=""):
    task = Task(
        id=1,
        description=description,
        status="todo",
        created_at=strftime("%Y-%m-%d %H:%M:%S", gmtime()),
        updated_at=strftime("%Y-%m-%d %H:%M:%S", gmtime())
    )
    add_task_to_file(task)


def update_task(task_id, description):
    # Read the existing JSON data
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    task = [task_itr for task_itr in data["task_list"] if task_itr["id"] == int(task_id)]
    task_list = [task_itr for task_itr in data["task_list"] if task_itr["id"] != int(task_id)]

    if task[0] is not None:
        task[0]["description"] = description
        task[0]["updated_at"] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        task_list.append(task[0])
        json_content = {
            "latest_id": data["latest_id"],
            "task_list": task_list
        }

        with open(json_file_path, 'w') as file:
            json.dump(json_content, file, indent=4)


def delete_task(task_id):
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    task_list = [task_itr for task_itr in data["task_list"] if task_itr["id"] != int(task_id)]

    json_content = {
        "latest_id": data["latest_id"],
        "task_list": task_list
    }

    with open(json_file_path, 'w') as file:
        json.dump(json_content, file, indent=4)


def list_task():
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    [print(task_itr) for task_itr in data["task_list"]]


def list_task_by_status(status):
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    [print(task_itr) for task_itr in data["task_list"] if task_itr["status"] == status]


def update_task_generic(task_id, field_name, field_value):
    # Read the existing JSON data
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    task = [task_itr for task_itr in data["task_list"] if task_itr["id"] == int(task_id)]
    task_list = [task_itr for task_itr in data["task_list"] if task_itr["id"] != int(task_id)]

    if task[0] is not None:
        task[0][field_name] = field_value
        task[0]["updated_at"] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        task_list.append(task[0])
        json_content = {
            "latest_id": data["latest_id"],
            "task_list": task_list
        }

        with open(json_file_path, 'w') as file:
            json.dump(json_content, file, indent=4)
