from secrets import secret

import pyperclip
from todoist_api_python.api import TodoistAPI


def main():
    api = TodoistAPI(secret)
    try:
        tasks = api.get_tasks()
    except Exception as error:
        print(error)
    try:
        task = api.add_task(pyperclip.paste())
    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()
