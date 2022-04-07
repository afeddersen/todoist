import pyperclip
import todoist

api = todoist.TodoistAPI(todoist_api_key)
api.sync()
item = api.items.add(pyperclip.paste())
api.commit()
