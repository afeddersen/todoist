# Todoist Keyboard Shortcut -- macOS

Objective: Copy some text from anywhere in macOS and "paste" that text into [Todoist](https://todoist.com/) as a new task.

Step 1: [Download a free 45 day trial of the BetterTouchTool](https://folivora.ai/).  This is an app that allows you to customize various input devices on your Mac.  It's awesome and very powerful.  It's $10 for 2 years or $22 for a lifetime license.  The $10 app is yours to keep (i.e. it's not a subscription).

Step 2: Clone this repo.

Step 3. Create an API key/token for your Todoist account.  Click on your initials in the top right hand corner and click "integrations".  About halfway down the page you'll see an option to create and then copy your token.

Step 4.  Do what I did for secrets management or do something better.  I create a `secrets.py` file and add it to my `.gitignore`.  My API token goes in this file as the `secret = "xxxxxx" variable.  

Step 5.  Use the BetterTouchTool to create a new trigger / keyboard shortcut.  I chose `command` `/` because it didn't seem to be mapped to anything else.

Step 6.  Assign an action to the trigger / keyboard shortcut.  Look for "execute shell script or task".

Step 7.  Point the "script" field to the `sendto.sh` file in this repo.  Modify any paths to match your environment.

Step 8.  Finally, you need to set an environment variable because the PYTHONPATH environment variable is not available in the BTT shell script environment (as it's only set for your shell).  I manage Python with Homebrew so I set `PYTHONPATH=/opt/homebrew/lib/python3.10/site-packages`.

And that should be it... If you highlight some text and `command` `c` and then `command` `/` -- the highlighted text should now be in your todoist inbox.



