# todoist
Personal automation for Todoist

1. You'll need the BetterTouchTool. I hadn't heard of this before but if you're a Mac user I encourage you to check it out - https://folivora.ai/
2. You'll need an API key from todoist. You can find this under your account -> integrations.
3. Create a Python script.

```
import pyperclip
import todoist

api = todoist.TodoistAPI('<api_key>')
api.sync()
item = api.items.add(pyperclip.paste())
api.commit()
```

4. Use the BetterTouchTool to map a custom keyboard shortcut to this Python script. I set it up to execute a shell script but there are many ways to do it.
