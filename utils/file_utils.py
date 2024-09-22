import json
import os

json_file_path = 'tasks.json'


def get_latest_id():
    # Read the JSON file
    try:
        with open(json_file_path, 'r') as file:
            try:
                data = json.load(file)
                return data["latest_id"]
            except json.JSONDecodeError:
                return 0
            except Exception as e:
                return 0
    except Exception as e:
        return 0


def get_json_file_content(existing_data, task):
    id = get_latest_id()
    task.id = id + 1
    print(f"Added task: {task.to_dict()}")
    existing_data.append(task.to_dict())
    return {
        "latest_id": id + 1,
        "task_list": existing_data
    }


def add_task_to_file(task):
    # Read the existing data from the JSON file
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as file:
            try:
                json_data = json.load(file)
            except json.JSONDecodeError:
                json_data = {
                    "latest_id": 0,
                    "task_list": []
                }  # Initialize data as an empty list if file is empty or invalid
    else:
        json_data = {
            "latest_id": 0,
            "task_list": []
        }  # If the file does not exist, start with an empty list

    if json_data["task_list"] == None:
        existing_data = []
    else:
        existing_data = json_data["task_list"]
    # existing_data.append(json.dumps(task.to_dict()))
    json_content = get_json_file_content(existing_data, task)
    # Write the updated data back to the JSON file
    with open(json_file_path, 'w') as file:
        json.dump(json_content, file, indent=4)

    # print(f"Added user: {task}")
