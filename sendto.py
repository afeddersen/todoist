from pprint import pprint
from secrets import todoist_api_key

import pyperclip
from todoist_api_python.api import TodoistAPI


def main():
    api = TodoistAPI(todoist_api_key)
    try:
        tasks = api.get_tasks()
        pprint(tasks)
    except Exception as error:
        print(error)
    try:
        new_task = api.add_task(pyperclip.paste())
    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()
